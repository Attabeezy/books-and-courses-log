import pandas as pd

# Data represented as a list of dictionaries with all values as 1s and 0s.
# Key Mapping:
# C: Cough, F: Fever, B: Difficulty breathing, T: Tiredness
# D: Diagnosis (1 = Sick, 0 = Healthy)
data = [
    {'C': 0, 'F': 1, 'B': 1, 'T': 1, 'D': 1}, # Patient 1: Sick
    {'C': 1, 'F': 1, 'B': 0, 'T': 1, 'D': 1}, # Patient 2: Sick
    {'C': 1, 'F': 0, 'B': 1, 'T': 1, 'D': 1}, # Patient 3: Sick
    {'C': 1, 'F': 1, 'B': 1, 'T': 0, 'D': 1}, # Patient 4: Sick
    {'C': 1, 'F': 0, 'B': 0, 'T': 1, 'D': 0}, # Patient 5: Healthy
    {'C': 0, 'F': 1, 'B': 1, 'T': 0, 'D': 0}, # Patient 6: Healthy
    {'C': 0, 'F': 1, 'B': 0, 'T': 0, 'D': 0}, # Patient 7: Healthy
    {'C': 0, 'F': 0, 'B': 0, 'T': 1, 'D': 0}, # Patient 8: Healthy
]

# Create the DataFrame directly from the list of dictionaries
df = pd.DataFrame(data)

# Optional: Rename columns to full names for clarity while keeping the 1/0 data
df.rename(columns={
    'C': 'Cough',
    'F': 'Fever',
    'B': 'Difficulty breathing',
    'T': 'Tiredness',
    'D': 'Diagnosis'
}, inplace=True)

# Display the resulting DataFrame
print(df)