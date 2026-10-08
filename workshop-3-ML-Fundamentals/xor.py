import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# 1. Dataset
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]], dtype=np.float32)

Y = np.array([[0],
              [1],
              [1],
              [0]], dtype=np.float32)

# 2. Activation functions
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_derivative(a):
    """Derivative of sigmoid given activation a = sigmoid(z)."""
    return a * (1.0 - a)

# 3. Model Initialization
input_dim = 2
hidden_dim = 2
output_dim = 1

# Random weight initialization (Xavier/Glorot uniform initialization)
W1 = np.random.uniform(-1.0, 1.0, (input_dim, hidden_dim))
b1 = np.zeros((1, hidden_dim))

W2 = np.random.uniform(-1.0, 1.0, (hidden_dim, output_dim))
b2 = np.zeros((1, output_dim))

# Hyperparameters
learning_rate = 1.0
epochs = 10000
eps = 1e-8  # To prevent division by zero in RMSE gradient

# 4. Training Loop
for epoch in range(1, epochs + 1):
    # --- Forward Propagation ---
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)
    
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)
    
    # --- RMSE Loss Computation ---
    mse = np.mean((A2 - Y) ** 2)
    rmse = np.sqrt(mse)
    
    # --- Backpropagation ---
    # dL / dA2
    dL_dA2 = (A2 - Y) / (X.shape[0] * (rmse + eps))
    
    # Output layer delta: dL / dZ2
    delta2 = dL_dA2 * sigmoid_derivative(A2)
    
    # Gradients for W2 and b2
    dW2 = np.dot(A1.T, delta2)
    db2 = np.sum(delta2, axis=0, keepdims=True)
    
    # Hidden layer delta: dL / dZ1
    delta1 = np.dot(delta2, W2.T) * sigmoid_derivative(A1)
    
    # Gradients for W1 and b1
    dW1 = np.dot(X.T, delta1)
    db1 = np.sum(delta1, axis=0, keepdims=True)
    
    # --- Gradient Descent Update ---
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    
    if epoch % 2000 == 0:
        print(f"Epoch {epoch:5d} | RMSE Loss: {rmse:.6f}")

# 5. Evaluation
print("\n--- Final Predictions ---")
Z1 = np.dot(X, W1) + b1
A1 = sigmoid(Z1)
Z2 = np.dot(A1, W2) + b2
predictions = sigmoid(Z2)

for i in range(len(X)):
    print(f"Input: {X[i].astype(int)} | Target: {int(Y[i][0])} | Predicted: {predictions[i][0]:.4f} (Round: {int(np.round(predictions[i][0]))})")