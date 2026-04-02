"""
Chapter 9: Machine Learning with Julia
========================================
Comprehensive examples using MLJ.jl and Flux.jl.
Covers: iris classification, regression with MLJ, and MNIST with Flux.
"""

# ============================================================
# Part 1: MLJ.jl - Classical Machine Learning
# ============================================================

using MLJ
using DataFrames
using Statistics

println("=== MLJ.jl - Classical Machine Learning ===")

# --- Example 1: Iris Classification ---
println("\n--- Iris Classification ---")

# Load the iris dataset (built into MLJ)
iris = load_iris()
X_iris = select(DataFrame(iris), Not(:target))
y_iris = iris.target

println("Dataset size: $(size(X_iris))")
println("Classes: $(levels(y_iris))")
println("Class distribution: $(countmap(y_iris))")

# Split into train and test
train_idx, test_idx = partition(eachindex(y_iris), 0.7, shuffle=true, rng=42)
X_train = X_iris[train_idx, :]
X_test = X_iris[test_idx, :]
y_train = y_iris[train_idx]
y_test = y_iris[test_idx]

println("Train size: $(length(train_idx)), Test size: $(length(test_idx))")

# --- Decision Tree ---
println("\n--- Decision Tree Classifier ---")
Tree = @load DecisionTreeClassifier pkg=DecisionTree
tree_model = Tree(max_depth=4)

tree_mach = machine(tree_model, X_train, y_train)
fit!(tree_mach, verbosity=0)

y_pred_tree = predict_mode(tree_mach, X_test)
accuracy_tree = mean(y_pred_tree .== y_test)
println("Decision Tree Accuracy: $(round(accuracy_tree * 100, digits=1))%")

# --- Random Forest ---
println("\n--- Random Forest Classifier ---")
RF = @load RandomForestClassifier pkg=DecisionTree
rf_model = RF(n_trees=100, max_depth=5)

rf_mach = machine(rf_model, X_train, y_train)
fit!(rf_mach, verbosity=0)

y_pred_rf = predict_mode(rf_mach, X_test)
accuracy_rf = mean(y_pred_rf .== y_test)
println("Random Forest Accuracy: $(round(accuracy_rf * 100, digits=1))%")

# Probabilistic predictions
y_proba = predict(rf_mach, X_test)
println("First 3 probabilistic predictions:")
for i in 1:3
    println("  Sample $i: $(y_proba[i])")
end

# --- k-Nearest Neighbors ---
println("\n--- k-Nearest Neighbors ---")
KNN = @load KNNClassifier pkg=NearestNeighborModels
knn_model = KNN(K=5)

knn_mach = machine(knn_model, X_train, y_train)
fit!(knn_mach, verbosity=0)

y_pred_knn = predict_mode(knn_mach, X_test)
accuracy_knn = mean(y_pred_knn .== y_test)
println("KNN (K=5) Accuracy: $(round(accuracy_knn * 100, digits=1))%")

# --- Cross-validation ---
println("\n--- Cross-Validation ---")
cv = CV(nfolds=5, shuffle=true, rng=42)
rf_cv = evaluate(rf_model, X_iris, y_iris,
    resampling=cv,
    measure=[accuracy, multiclass_f1score],
    verbosity=0)

println("5-Fold CV Results (Random Forest):")
println("  Accuracy: $(round(rf_cv.measurement[1], digits=4)) +/- $(round(std(rf_cv.per_fold[1]), digits=4))")
println("  F1 Score: $(round(rf_cv.measurement[2], digits=4))")

# --- Hyperparameter Tuning ---
println("\n--- Hyperparameter Tuning ---")
rf_range = range(rf_model, :n_trees, lower=10, upper=200)
tuned_rf = TunedModel(
    model=rf_model,
    tuning=Grid(resolution=5),
    range=rf_range,
    resampling=CV(nfolds=3),
    measure=accuracy
)

tuned_mach = machine(tuned_rf, X_train, y_train)
fit!(tuned_mach, verbosity=0)

best_model = fitted_params(tuned_mach).best_model
println("Best n_trees: $(best_model.n_trees)")

y_pred_tuned = predict_mode(tuned_mach, X_test)
accuracy_tuned = mean(y_pred_tuned .== y_test)
println("Tuned RF Accuracy: $(round(accuracy_tuned * 100, digits=1))%")

# ============================================================
# Example 2: Regression
# ============================================================

println("\n--- Regression Example ---")

# Generate synthetic regression data
using Random
Random.seed!(42)

n_samples = 200
X_reg = DataFrame(
    x1 = randn(n_samples),
    x2 = randn(n_samples),
    x3 = randn(n_samples)
)
y_reg = 3.0 .* X_reg.x1 .- 2.0 .* X_reg.x2 .+ 0.5 .* X_reg.x3 .+ 0.3 .* randn(n_samples)

train_r, test_r = partition(eachindex(y_reg), 0.8, shuffle=true, rng=42)

# --- Linear Regression ---
println("\n--- Linear Regression ---")
LR = @load LinearRegressor pkg=MLJLinearModels
lr_model = LR()

lr_mach = machine(lr_model, X_reg[train_r, :], y_reg[train_r])
fit!(lr_mach, verbosity=0)

y_pred_lr = predict(lr_mach, X_reg[test_r, :])
rmse_lr = sqrt(mean((y_pred_lr .- y_reg[test_r]).^2))
r2_lr = 1 - sum((y_pred_lr .- y_reg[test_r]).^2) / sum((y_reg[test_r] .- mean(y_reg[test_r])).^2)
println("Linear Regression RMSE: $(round(rmse_lr, digits=4))")
println("Linear Regression R²: $(round(r2_lr, digits=4))")

# --- Ridge Regression ---
println("\n--- Ridge Regression ---")
Ridge = @load RidgeRegressor pkg=MLJLinearModels
ridge_model = Ridge(lambda=0.1)

ridge_mach = machine(ridge_model, X_reg[train_r, :], y_reg[train_r])
fit!(ridge_mach, verbosity=0)

y_pred_ridge = predict(ridge_mach, X_reg[test_r, :])
rmse_ridge = sqrt(mean((y_pred_ridge .- y_reg[test_r]).^2))
println("Ridge Regression RMSE: $(round(rmse_ridge, digits=4))")

# --- Model comparison ---
println("\n--- Model Comparison ---")
println("Results summary:")
println("  Decision Tree: $(round(accuracy_tree * 100, digits=1))% accuracy")
println("  Random Forest: $(round(accuracy_rf * 100, digits=1))% accuracy")
println("  KNN (K=5):     $(round(accuracy_knn * 100, digits=1))% accuracy")
println("  Linear Reg:    RMSE = $(round(rmse_lr, digits=4))")
println("  Ridge Reg:     RMSE = $(round(rmse_ridge, digits=4))")

# ============================================================
# Part 2: Flux.jl - Deep Learning
# ============================================================

using Flux
using Flux: onehotbatch, onecold, crossentropy, throttle
using MLDatasets

println("\n=== Flux.jl - Deep Learning ===")

# --- Example: MNIST Digit Classification ---
println("\n--- MNIST Digit Classification ---")

# Load MNIST data
train_data = MLDatasets.MNIST(:train)
test_data = MLDatasets.MNIST(:test)

# Prepare training data
x_train = reshape(train_data.features, 28*28, :)  # flatten to 784 x N
y_train_labels = train_data.targets
y_train_oh = onehotbatch(y_train_labels, 0:9)

# Prepare test data
x_test = reshape(test_data.features, 28*28, :)
y_test_labels = test_data.targets
y_test_oh = onehotbatch(y_test_labels, 0:9)

println("Training set: $(size(x_train, 2)) images")
println("Test set: $(size(x_test, 2)) images")
println("Input dimension: $(size(x_train, 1))")

# Convert to Float32 for efficiency
x_train = Float32.(x_train)
x_test = Float32.(x_test)

# --- Simple MLP ---
println("\n--- Multi-Layer Perceptron ---")
model = Chain(
    Dense(784, 256, relu),
    Dropout(0.2),
    Dense(256, 128, relu),
    Dropout(0.2),
    Dense(128, 10),
    softmax
)

println("Model architecture:")
println(model)
println("Parameters: $(sum(length, Flux.params(model)))")

# Loss function
loss(x, y) = crossentropy(model(x), y)

# Optimizer
opt = Flux.setup(Adam(0.001), model)

# Training loop
println("\nTraining...")
batch_size = 128
n_epochs = 5

for epoch in 1:n_epochs
    # Mini-batch training
    n_batches = size(x_train, 2) ÷ batch_size
    epoch_loss = 0.0

    for i in 1:n_batches
        idx = ((i-1)*batch_size+1):(i*batch_size)
        x_batch = x_train[:, idx]
        y_batch = y_train_oh[:, idx]

        grads = Flux.gradient(model) do m
            crossentropy(m(x_batch), y_batch)
        end

        Flux.update!(opt, model, grads[1])
        epoch_loss += crossentropy(model(x_batch), y_batch)
    end

    # Evaluate on test set (sample for speed)
    test_pred = onecold(model(x_test[:, 1:1000]), 0:9)
    test_acc = mean(test_pred .== y_test_labels[1:1000])

    println("Epoch $epoch/$n_epochs - Loss: $(round(epoch_loss/n_batches, digits=4)) - Test Acc: $(round(test_acc*100, digits=1))%")
end

# Final evaluation
println("\n--- Final Evaluation ---")
y_pred_final = onecold(model(x_test), 0:9)
final_accuracy = mean(y_pred_final .== y_test_labels)
println("Final Test Accuracy: $(round(final_accuracy * 100, digits=2))%")

# Per-class accuracy
println("\nPer-class accuracy:")
for digit in 0:9
    mask = y_test_labels .== digit
    class_acc = mean(y_pred_final[mask] .== digit)
    println("  Digit $digit: $(round(class_acc * 100, digits=1))% ($(sum(mask)) samples)")
end

# --- Convolutional Neural Network ---
println("\n--- Convolutional Neural Network ---")

# Reshape for CNN (height x width x channels x batch)
x_train_cnn = reshape(x_train, 28, 28, 1, :)
x_test_cnn = reshape(x_test, 28, 28, 1, :)

cnn_model = Chain(
    Conv((3, 3), 1 => 16, relu, pad=1),
    MaxPool((2, 2)),
    Conv((3, 3), 16 => 32, relu, pad=1),
    MaxPool((2, 2)),
    Flux.flatten,
    Dense(32 * 7 * 7, 128, relu),
    Dropout(0.3),
    Dense(128, 10),
    softmax
)

println("CNN architecture:")
println(cnn_model)
println("CNN parameters: $(sum(length, Flux.params(cnn_model)))")

# Train CNN (abbreviated for demonstration)
opt_cnn = Flux.setup(Adam(0.001), cnn_model)

println("\nTraining CNN (3 epochs)...")
for epoch in 1:3
    n_batches = min(100, size(x_train_cnn, 4) ÷ batch_size)  # limit batches for demo

    for i in 1:n_batches
        idx = ((i-1)*batch_size+1):(i*batch_size)
        x_batch = x_train_cnn[:, :, :, idx]
        y_batch = y_train_oh[:, idx]

        grads = Flux.gradient(cnn_model) do m
            crossentropy(m(x_batch), y_batch)
        end

        Flux.update!(opt_cnn, cnn_model, grads[1])
    end

    # Quick test evaluation
    test_pred_cnn = onecold(cnn_model(x_test_cnn[:, :, :, 1:500]), 0:9)
    test_acc_cnn = mean(test_pred_cnn .== y_test_labels[1:500])
    println("Epoch $epoch/3 - Test Acc: $(round(test_acc_cnn*100, digits=1))%")
end

println("\nAll machine learning examples complete.")
