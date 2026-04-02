"""
Chapter 7: Diffusion Models and Image Generation
- Noise schedules
- Stable Diffusion text-to-image
- Negative prompts and parameters
- Image-to-image
- ControlNet
- Batch generation with seeds
"""

# %% 1. Noise schedule visualization
import numpy as np
import matplotlib.pyplot as plt

T = 1000

# Linear schedule
beta_linear = np.linspace(1e-4, 0.02, T)
alpha_linear = np.cumprod(1 - beta_linear)

# Cosine schedule
s = 0.008
steps = np.arange(T + 1) / T
f = np.cos((steps + s) / (1 + s) * np.pi / 2) ** 2
alpha_cosine = f[1:] / f[0]

plt.figure(figsize=(8, 4))
plt.plot(alpha_linear, label="Linear")
plt.plot(alpha_cosine, label="Cosine")
plt.xlabel("Timestep")
plt.ylabel("Cumulative alpha (signal remaining)")
plt.title("Noise schedules")
plt.legend()
plt.tight_layout()
plt.savefig("noise_schedules.png", dpi=150)
plt.show()
print("Saved noise_schedules.png")

# %% 2. Text-to-image with Stable Diffusion
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1-base",
    torch_dtype=torch.float16,
)
pipe = pipe.to("cuda")

prompt = "A serene African village at sunset, digital art, highly detailed"
image = pipe(
    prompt,
    num_inference_steps=30,
    guidance_scale=7.5,
).images[0]

image.save("african_village.png")
print("Generated: african_village.png")

# %% 3. Negative prompts and parameters
image = pipe(
    prompt="Portrait of a scientist in a laboratory, photorealistic",
    negative_prompt="blurry, low quality, deformed, cartoon",
    num_inference_steps=50,
    guidance_scale=8.0,
    height=512,
    width=512,
).images[0]
image.save("scientist.png")
print("Generated: scientist.png")

# %% 4. Guidance scale comparison
guidance_values = [1, 5, 7.5, 12, 20]
prompt = "A futuristic city with flying cars, digital art"

fig, axes = plt.subplots(1, len(guidance_values), figsize=(20, 4))
for ax, gs in zip(axes, guidance_values):
    img = pipe(prompt, guidance_scale=gs, num_inference_steps=25,
               generator=torch.Generator("cuda").manual_seed(42)).images[0]
    ax.imshow(img)
    ax.set_title(f"guidance={gs}")
    ax.axis("off")
plt.tight_layout()
plt.savefig("guidance_comparison.png", dpi=150)
plt.show()
print("Saved guidance_comparison.png")

# %% 5. Image-to-image
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image

pipe_img2img = StableDiffusionImg2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1-base",
    torch_dtype=torch.float16,
).to("cuda")

# Create a simple test image (or load your own)
init_image = Image.new("RGB", (512, 512), color=(100, 150, 200))

strengths = [0.3, 0.5, 0.8]
for s in strengths:
    result = pipe_img2img(
        prompt="A beautiful watercolor painting of a landscape",
        image=init_image,
        strength=s,
        guidance_scale=7.5,
    ).images[0]
    result.save(f"img2img_strength_{s}.png")
    print(f"Generated: img2img_strength_{s}.png")

# %% 6. Batch generation with seed control
generator = torch.Generator("cuda").manual_seed(42)

prompts = ["A cat astronaut", "A dog scientist", "A bird musician"]
images = pipe(
    prompt=prompts,
    num_inference_steps=30,
    guidance_scale=7.5,
    generator=generator,
).images

for i, img in enumerate(images):
    img.save(f"batch_{i}.png")
    print(f"Generated: batch_{i}.png")

# %% 7. ControlNet (Canny edges)
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel

controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16
)
pipe_cn = StableDiffusionControlNetPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1-base",
    controlnet=controlnet,
    torch_dtype=torch.float16,
).to("cuda")

# Create simple edge image for demo
edges = Image.new("RGB", (512, 512), color=(0, 0, 0))
result = pipe_cn(
    prompt="A futuristic building, cyberpunk style, neon lights",
    image=edges,
    num_inference_steps=30,
).images[0]
result.save("controlnet_result.png")
print("Generated: controlnet_result.png")
