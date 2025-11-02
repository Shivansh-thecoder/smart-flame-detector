import pandas as pd
import numpy as np

np.random.seed(42)

# ⚙️ Calibrated ranges (from your results)
SAFE_MIN, SAFE_MAX = 264, 304
FIRE_MIN, FIRE_MAX = 180, 234   # below 234 = fire

# Generate synthetic data
no_fire = np.random.normal((SAFE_MIN + SAFE_MAX)/2, 8, 300)
fire = np.random.normal((FIRE_MIN + FIRE_MAX)/2, 10, 300)

# Clip to realistic bounds
no_fire = np.clip(no_fire, SAFE_MIN, SAFE_MAX)
fire = np.clip(fire, FIRE_MIN, FIRE_MAX)

# Combine dataset
data = pd.DataFrame({
    "Flame_Value": np.concatenate([no_fire, fire]),
    "Label": [0]*len(no_fire) + [1]*len(fire)  # 0 = Safe, 1 = Fire
})

# Shuffle
data = data.sample(frac=1).reset_index(drop=True)

# Save
data.to_csv("flame_training_data.csv", index=False)
print("✅ Dataset saved as flame_training_data.csv")
print("Safe range:", SAFE_MIN, "-", SAFE_MAX)
print("Fire range:", FIRE_MIN, "-", FIRE_MAX)


