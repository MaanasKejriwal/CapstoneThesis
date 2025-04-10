import pandas as pd

# Example input lists
hadm_ids = [0,22995465,20338077,23488445,24181354,21027282,29974575,24540843,24698912,20790339,20854119,25085565,28477280,29276678,27525946,29279905,23559586,27617929,28662225] # Replace with actual admission IDs
procedures_cols = ['subject_id', 'hadm_id', 'icd_code', 'icd_version']
d_icd_cols = ['icd_code', 'icd_version', 'long_title']

# Load dataframes
icd_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/hosp/procedures_icd.csv', usecols=procedures_cols)
d_icd_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/hosp/d_icd_procedures.csv', usecols=d_icd_cols)

# Filter by hospital admission IDs
icd_filtered = icd_df[icd_df['hadm_id'].isin(hadm_ids)]

# Define sepsis-related ICD codes
sepsis_icd9 = ['78552', '0380', '0381', '0383', '0384', '0388', '0389', '99592']
sepsis_icd10 = ['A419']

# Further filter for sepsis cases
sepsis_patients_df = icd_filtered[
    ((icd_filtered['icd_code'].isin(sepsis_icd9)) & (icd_filtered['icd_version'] == 9)) |
    ((icd_filtered['icd_code'].isin(sepsis_icd10)) & (icd_filtered['icd_version'] == 10))
]

# Perform join on icd_code and icd_version to add 'long_title'
procedures_detailed_df = pd.merge(
    sepsis_patients_df, 
    d_icd_df, 
    on=['icd_code', 'icd_version'], 
    how='left'
)

# Check resulting dataframe
print(procedures_detailed_df.head())

# Save to CSV
procedures_detailed_df.to_csv('New/PROCEDURES_ICD_LABELED.csv', index=False)

# Print results
print(f"Number of sepsis procedures records: {len(procedures_detailed_df)}")