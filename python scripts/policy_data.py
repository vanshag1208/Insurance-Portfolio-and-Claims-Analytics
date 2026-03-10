import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# -------------------------------
# Basic configuration
# -------------------------------

TOTAL_CUSTOMERS = 1_000_000
VEHICLE_VALUE = 100000

# tenure distribution (percentage)
tenure_distribution = {
    1: 0.20,
    2: 0.30,
    3: 0.40,
    4: 0.10
}

# -------------------------------
# Generate customer and vehicle IDs
# -------------------------------

customer_ids = np.arange(1, TOTAL_CUSTOMERS + 1)
vehicle_ids = customer_ids.copy()

# -------------------------------
# Generate purchase dates across 2024
# -------------------------------

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

total_days = (end_date - start_date).days + 1

# randomly distribute purchases across the year
random_days = np.random.randint(0, total_days, TOTAL_CUSTOMERS)
purchase_dates = [start_date + timedelta(days=int(x)) for x in random_days]

# -------------------------------
# Assign policy tenure based on distribution
# -------------------------------

tenure_values = list(tenure_distribution.keys())
tenure_probs = list(tenure_distribution.values())

policy_tenure = np.random.choice(
    tenure_values,
    size=TOTAL_CUSTOMERS,
    p=tenure_probs
)

# -------------------------------
# Calculate policy dates
# -------------------------------

policy_start_dates = [d + timedelta(days=365) for d in purchase_dates]

policy_end_dates = [
    start + timedelta(days=int(365 * tenure))
    for start, tenure in zip(policy_start_dates, policy_tenure)
]

# -------------------------------
# Premium calculation
# -------------------------------

premium = policy_tenure * 100

# -------------------------------
# Create dataframe
# -------------------------------

policy_data = pd.DataFrame({
    "Customer_ID": customer_ids,
    "Vehicle_ID": vehicle_ids,
    "Vehicle_Value": VEHICLE_VALUE,
    "Premium": premium,
    "Policy_Purchase_Date": purchase_dates,
    "Policy_Start_Date": policy_start_dates,
    "Policy_End_Date": policy_end_dates,
    "Policy_Tenure": policy_tenure
})

# -------------------------------
# Save dataset
# -------------------------------

policy_data.to_csv(r"C:\Users\vansh\Downloads\zopper assignment\excel\policy_sales_data.csv", index=False)

print("Policy dataset generated successfully!")
print(f"Total records: {len(policy_data)}")