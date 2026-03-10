import pandas as pd
import numpy as np

np.random.seed(42)

# ---------------------------
# load policy dataset
# ---------------------------

policy_data = pd.read_csv(r"C:\Users\vansh\Downloads\zopper assignment\excel\policy_sales_data.csv")

# ---------------------------
# 2025 CLAIMS
# ---------------------------

eligible_days = [7,14,21,28]

eligible_2025 = policy_data[
    policy_data["Policy_Purchase_Date"].str[8:10].astype(int).isin(eligible_days)
]

claims_2025 = eligible_2025.sample(frac=0.30)

claims_2025_df = pd.DataFrame({
    "Claim_ID": range(1, len(claims_2025) + 1),
    "Customer_ID": claims_2025["Customer_ID"],
    "Vehicle_ID": claims_2025["Vehicle_ID"],
    "Claim_Amount": 10000,
    "Claim_Date": claims_2025["Policy_Start_Date"],
    "Claim_Type": 1
})

# ---------------------------
# 2026 CLAIMS
# ---------------------------

eligible_2026 = policy_data[
    policy_data["Policy_Tenure"] == 4
]

claims_2026 = eligible_2026.sample(frac=0.10)

date_range = pd.date_range("2026-01-01","2026-02-28")

random_dates = np.random.choice(date_range, len(claims_2026))

claims_2026_df = pd.DataFrame({
    "Claim_ID": range(
        len(claims_2025_df) + 1,
        len(claims_2025_df) + len(claims_2026) + 1
    ),
    "Customer_ID": claims_2026["Customer_ID"],
    "Vehicle_ID": claims_2026["Vehicle_ID"],
    "Claim_Amount": 10000,
    "Claim_Date": random_dates,
    "Claim_Type": 2
})

# ---------------------------
# combine claims
# ---------------------------

claims_data = pd.concat([claims_2025_df, claims_2026_df])

# ---------------------------
# save file
# ---------------------------

claims_data.to_csv(r"C:\Users\vansh\Downloads\zopper assignment\excel\claims_data.csv", index=False)

print("Claims dataset generated!")
print("Total claims:", len(claims_data))