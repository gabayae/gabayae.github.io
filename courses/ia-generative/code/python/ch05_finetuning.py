"""
Chapter 5: Fine-tuning LLMs
- LoRA configuration
- QLoRA (4-bit quantization)
- Dataset preparation (Dolly)
- HuggingFace Trainer
- Evaluation
"""

# %% 1. LoRA configuration and parameter count
from peft import LoraConfig, get_peft_model, TaskType
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype="auto", device_map="auto"
)

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
)

peft_model = get_peft_model(model, lora_config)
peft_model.print_trainable_parameters()

# %% 2. QLoRA setup (4-bit quantization)
from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

model_q = AutoModelForCausalLM.from_pretrained(
    model_name, quantization_config=bnb_config, device_map="auto"
)
peft_model_q = get_peft_model(model_q, lora_config)
peft_model_q.print_trainable_parameters()

# %% 3. Load and prepare the Dolly dataset
from datasets import load_dataset

dataset = load_dataset("databricks/databricks-dolly-15k", split="train[:500]")
print(f"Dataset size: {len(dataset)}")
print(f"Columns: {dataset.column_names}")
print(f"\nExample:\n{dataset[0]}")

def format_instruction(example):
    if example["context"]:
        text = (f"### Instruction:\n{example['instruction']}\n\n"
                f"### Context:\n{example['context']}\n\n"
                f"### Response:\n{example['response']}")
    else:
        text = (f"### Instruction:\n{example['instruction']}\n\n"
                f"### Response:\n{example['response']}")
    return {"text": text}

formatted = dataset.map(format_instruction)
print(f"\nFormatted example:\n{formatted[0]['text'][:300]}")

# %% 4. Tokenize dataset
def tokenize(example):
    return tokenizer(
        example["text"], truncation=True, max_length=512, padding="max_length"
    )

tokenized = formatted.map(tokenize, remove_columns=formatted.column_names)
print(f"Tokenized columns: {tokenized.column_names}")

# %% 5. Fine-tune with Trainer
from transformers import TrainingArguments, Trainer, DataCollatorForLanguageModeling

training_args = TrainingArguments(
    output_dir="./tinyllama-dolly-lora",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    save_strategy="epoch",
    warmup_ratio=0.03,
    lr_scheduler_type="cosine",
    report_to="none",
)

trainer = Trainer(
    model=peft_model_q,
    args=training_args,
    train_dataset=tokenized,
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
)

print("\nStarting training...")
trainer.train()
print("Training complete!")

# %% 6. Save and test
peft_model_q.save_pretrained("./tinyllama-dolly-lora")
print("LoRA adapter saved.")

prompt = "### Instruction:\nExplain what a neural network is.\n\n### Response:\n"
inputs = tokenizer(prompt, return_tensors="pt").to(peft_model_q.device)
output = peft_model_q.generate(**inputs, max_new_tokens=100, temperature=0.7,
                                do_sample=True)
print("\nFine-tuned model output:")
print(tokenizer.decode(output[0], skip_special_tokens=True))

# %% 7. VRAM usage
if torch.cuda.is_available():
    print(f"\nMax VRAM used: {torch.cuda.max_memory_allocated() / 1e9:.2f} GB")
