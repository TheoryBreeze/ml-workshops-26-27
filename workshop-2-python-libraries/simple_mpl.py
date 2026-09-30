import matplotlib.pyplot as plt
import numpy as np

# Simple dummy data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 5, 3, 8, 7])

# 1. Create a 2x3 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 6))

# --- ROW 0 ---
# Plot (Row 0, Col 0): Simple Line Plot
axes[0, 0].plot(x, y)
axes[0, 0].set_title("Line Plot")

# Plot (Row 0, Col 1): Scatter Plot
axes[0, 1].scatter(x, y)
axes[0, 1].set_title("Scatter Plot")

# Plot (Row 0, Col 2): Bar Chart
axes[0, 2].bar(x, y)
axes[0, 2].set_title("Bar Chart")

# --- ROW 1 ---
# Plot (Row 1, Col 0): Line with y squared
axes[1, 0].plot(x, y**2)
axes[1, 0].set_title("y Squared")

# Plot (Row 1, Col 1): Horizontal Bar Chart
axes[1, 1].barh(x, y)
axes[1, 1].set_title("Horizontal Bar")

# Plot (Row 1, Col 2): Step Plot
axes[1, 2].step(x, y)
axes[1, 2].set_title("Step Plot")

# 2. Adjust spacing so titles and labels do not overlap
plt.tight_layout()

# 3. Display
plt.savefig("simple_mpl_example.png")