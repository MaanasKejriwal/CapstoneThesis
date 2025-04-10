import pandas as pd

# Load DIAGNOSES_ICD.csv
diagnoses_icd_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/hosp/diagnoses_icd.csv', usecols=['subject_id', 'hadm_id', 'icd_code', 'icd_version'])

# Define sepsis-related ICD codes
sepsis_icd9 = ['78552', '0380', '0381', '0383', '0384', '0388', '0389', '99592']
sepsis_icd10 = ['A419']

# Filter for sepsis cases
sepsis_patients_df = diagnoses_icd_df[
    ((diagnoses_icd_df['icd_code'].isin(sepsis_icd9)) & (diagnoses_icd_df['icd_version'] == 9)) |
    ((diagnoses_icd_df['icd_code'].isin(sepsis_icd10)) & (diagnoses_icd_df['icd_version'] == 10))
]

# Extract unique subject_ids and hadm_ids
sepsis_subject_ids = sepsis_patients_df['subject_id'].unique().tolist()
sepsis_hadm_ids = sepsis_patients_df['hadm_id'].unique().tolist()

# Save the lists if needed
pd.Series(sepsis_subject_ids).to_csv('New/sepsis_subject_ids.csv', index=False)
pd.Series(sepsis_hadm_ids).to_csv('New/sepsis_hadm_ids.csv', index=False)

# Print results
print(f"Number of unique sepsis patients: {len(sepsis_subject_ids)}")
print(f"Number of unique sepsis hospital admissions: {len(sepsis_hadm_ids)}")
