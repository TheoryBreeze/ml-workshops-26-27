import numpy as np


def load_mnist_0_and_1():
    filepath = "mnist.npz" # donwloaded from 

    with np.load(filepath) as data:
        x_train, y_train = data["x_train"], data["y_train"]
        x_test, y_test = data["x_test"], data["y_test"]

    # Filter 0 and 1 for train set
    train_mask = (y_train == 0) | (y_train == 1)
    X_train = x_train[train_mask].reshape(-1, 784).astype(np.float32) / 255.0
    y_train = y_train[train_mask]

    # Filter 0 and 1 for test set
    test_mask = (y_test == 0) | (y_test == 1)
    X_test = x_test[test_mask].reshape(-1, 784).astype(np.float32) / 255.0
    y_test = y_test[test_mask]

    return X_train, y_train, X_test, y_test


# 1. Load Data
X_train, y_train, X_test, y_test = load_mnist_0_and_1()

# 2. Compute weights from training data
mean_1 = np.mean(X_train[y_train == 1], axis=0)
mean_0 = np.mean(X_train[y_train == 0], axis=0)

w_raw = mean_1 - mean_0
w_norm = (w_raw - np.min(w_raw)) / (np.max(w_raw) - np.min(w_raw))

# 3. Compute raw dot-product scores (y = X . w)
train_scores = np.dot(X_train, w_norm)
test_scores = np.dot(X_test, w_norm)

# 4. Midpoint Decision Threshold
mean_score_0 = np.mean(train_scores[y_train == 0])
mean_score_1 = np.mean(train_scores[y_train == 1])
threshold = (mean_score_0 + mean_score_1) / 2.0

test_preds = (test_scores >= threshold).astype(int)
test_acc = np.mean(test_preds == y_test) * 100

# Print Results
print("--- Model Accuracy Results ---")
print(f"Number of test images (0s and 1s): {len(y_test)}")
print(f"Average score for digit 0: {mean_score_0:.2f}")
print(f"Average score for digit 1: {mean_score_1:.2f}")
print(f"Midpoint Threshold:        {threshold:.2f}")
print(f"Test Accuracy:             {test_acc:.2f}%\n")

# Export the normalized weights to a file
np.save("weights.npy", w_norm)
print("Normalized weights successfully exported to 'weights.npy'")