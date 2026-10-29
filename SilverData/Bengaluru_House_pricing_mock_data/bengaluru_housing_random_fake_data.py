import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)
n_samples = 55000  # Generating 55,000 rows (exceeds your 50k requirement)

# 1. Zone: 1=East, 2=South, 3=North, 4=West/Suburbs
zones = np.random.choice([1, 2, 3, 4], size=n_samples, p=[0.30, 0.25, 0.25, 0.20])

# 2. Property Type: 1=Apartment, 2=Villa/Independent House, 3=Plot
prop_types = np.random.choice([1, 2, 3], size=n_samples, p=[0.70, 0.15, 0.15])

# 3. Size (sq ft): Gamma distribution skewed toward realistic residential sizes
sizes = np.random.gamma(shape=3.5, scale=350, size=n_samples).astype(int) + 450
sizes = np.clip(sizes, 450, 6500)

# 4. BHK: 0 for plots, 1-5 for apartments/villas based on size
bhk = np.where(prop_types == 3, 0, np.clip((sizes // 550), 1, 5))

# 5. Tech Hub Proximity (km): Exponential distribution favoring closer distances
tech_dist = np.random.exponential(scale=4.5, size=n_samples)
tech_dist = np.clip(tech_dist, 0.2, 25.0)

# 6. Construction Status: 1=Ready, 2=Under Construction, 3=New Launch
const_status = np.random.choice([1, 2, 3], size=n_samples, p=[0.58, 0.32, 0.10])

# 7. Amenities Score: 1 to 10
amenities = np.random.randint(1, 11, size=n_samples)

# 8. Metro Distance (km): Proximity to Purple/Blue/Green lines
metro_dist = np.random.exponential(scale=2.8, size=n_samples)
metro_dist = np.clip(metro_dist, 0.1, 15.0)

# 9. Water Scarcity Risk Index: 1 (Low) to 5 (High)
water_scarcity = np.random.choice([1, 2, 3, 4, 5], size=n_samples, p=[0.20, 0.30, 0.30, 0.15, 0.05])

# 10. Groundwater Status: 1=Adequate, 2=Depleted/Tanker Dependent
groundwater = np.random.choice([1, 2], size=n_samples, p=[0.52, 0.48])

# 11. Pollution Status Index: 1 (Clean) to 5 (High Pollution)
pollution = np.random.choice([1, 2, 3, 4, 5], size=n_samples, p=[0.10, 0.30, 0.40, 0.15, 0.05])

# 12. Commercial Viability Index: 1 to 10
commercial = np.random.randint(1, 11, size=n_samples)

# 13. Nearby Hospitals Count: Poisson distribution
hospitals = np.random.poisson(lam=3.2, size=n_samples)
hospitals = np.clip(hospitals, 0, 10)

# Calculate realistic price per sq ft based on feature weights & Bengaluru micro-market economics
base_price = 6200
zone_mult = np.select([zones == 2, zones == 3, zones == 1, zones == 4], [1.38, 1.26, 1.22, 1.0])
prop_mult = np.select([prop_types == 2, prop_types == 1, prop_types == 3], [1.32, 1.0, 1.12])
tech_factor = 1.0 / (0.15 + tech_dist * 0.06)
metro_factor = 1.0 / (0.12 + metro_dist * 0.09)

price_per_sqft = (
    base_price * zone_mult * prop_mult 
    + (tech_factor * 1400) 
    + (metro_factor * 1100) 
    + (amenities * 180) 
    + (commercial * 120)
    - (water_scarcity * 150)
    + np.random.normal(0, 1200, n_samples)
)
price_per_sqft = np.clip(price_per_sqft, 3500, 26000)

# Map price per sq ft to target labels:
# 1: Budget (< ₹8,000)
# 2: Mid-Range (₹8,000 – ₹12,000)
# 3: Premium (₹12,000 – ₹15,000)
# 4: Luxury (> ₹15,000)
labels = np.select(
    [
        price_per_sqft < 8000,
        (price_per_sqft >= 8000) & (price_per_sqft <= 12000),
        (price_per_sqft > 12000) & (price_per_sqft <= 15000),
        price_per_sqft > 15000
    ],
    [1, 2, 3, 4]
)

# Export to LIBSVM format
file_name = "bengaluru_housing.libsvm"
with open(file_name, "w") as f:
    for i in range(n_samples):
        line = (
            f"{labels[i]} "
            f"1:{zones[i]} "
            f"2:{prop_types[i]} "
            f"3:{sizes[i]} "
            f"4:{bhk[i]} "
            f"5:{tech_dist[i]:.2f} "
            f"6:{const_status[i]} "
            f"7:{amenities[i]} "
            f"8:{metro_dist[i]:.2f} "
            f"9:{water_scarcity[i]} "
            f"10:{groundwater[i]} "
            f"11:{pollution[i]} "
            f"12:{commercial[i]} "
            f"13:{hospitals[i]}\n"
        )
        f.write(line)

print(f"Successfully generated {n_samples} rows and saved to '{file_name}'.")