import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm

# 1. Load the exported weights
weights = np.load("weights.npy")

# 2. Reshape into 28x28 grid
weights_grid = weights.reshape(28, 28)

# 3. Find the value representing the background/neutral level
# In MNIST, corner pixels (e.g. [0, 0]) are always background (0 for both digits)
neutral_val = weights_grid[0, 0]

# 4. Set up the colormap centered at the neutral background value
# vmin=0 (Blue), vcenter=neutral_val (White), vmax=1 (Red)
norm = TwoSlopeNorm(vmin=0.0, vcenter=neutral_val, vmax=1.0)

fig, ax = plt.subplots(figsize=(7, 7))
im = ax.imshow(weights_grid, cmap="bwr", norm=norm)

# 5. Add colorbar with custom annotations
cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_ticks([0.0, neutral_val, 1.0])
cbar.set_ticklabels(["0.0 (Digit 0 / Blue)", "Neutral (White)", "1.0 (Digit 1 / Red)"])

# 6. Styling
ax.set_title("28x28 Linear Model Weights (0 vs 1)", fontsize=14, pad=12)
ax.set_xlabel("Pixel Column")
ax.set_ylabel("Pixel Row")

plt.tight_layout()
plt.savefig('weight_grid.png')