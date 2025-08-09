import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

# Load datasets
df1 = pd.read_csv(r"C:\Users\sahar\Downloads\UIMS.csv")
df2 = pd.read_csv(r"C:\Users\sahar\Downloads\QUES.csv")

# Extract the 'size2' column
y = df1['size2']
x = df2['size2']

# Convert to numpy arrays
xnew = x.to_numpy()
ynew = y.to_numpy()

# Perform Mann-Whitney U test
stat, p_value = mannwhitneyu(ynew, xnew)

# Print results
print(f'Statistics={stat:.2f}, p={p_value:.2f}')

# Level of significance
alpha = 0.05

# Conclusion
if p_value < alpha:
    print("Reject Null Hypothesis (Significant difference between size2 metric of UIMS and Ques)")
else:
    print("Fail to Reject Null Hypothesis (No significant difference between size2 metric of UIMS and Ques)")


# Find common numerical columns
common_columns = df1.columns.intersection(df2.columns)

# Perform Mann-Whitney U test for each common column
results = []

for col in common_columns:
    stat, p_value = mannwhitneyu(df1[col], df2[col])
    results.append({'Metric': col, 'U-statistic': stat, 'p-value': p_value})

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Display results
print(results_df)

# Interpretation
alpha = 0.05
print("\nInterpretation:")
for _, row in results_df.iterrows():
    if row['p-value'] < alpha:
        print(f"{row['Metric']}: Significant difference (Reject Null Hypothesis)")
    else:
        print(f"{row['Metric']}: No significant difference (Fail to Reject Null Hypothesis)")