import pandas as pd

# Example input lists
patient_ids = [0,10009049,10007928,10020786,10004235,10018081,10020944,10037861,10015860,10031757,10035631,10019003,10003400,10037975,10002428,10002428] # Replace with actual IDs
patients_cols = ['subject_id', 'gender', 'anchor_age', 'anchor_year', 'dod']
admissions_cols = ['subject_id', 'hadm_id', 'admittime', 'dischtime', 'admission_type', 'admission_location', 'discharge_location', 'hospital_expire_flag']

# Assuming you've loaded these tables already
patients_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/hosp/patients.csv', usecols=patients_cols)
admissions_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/hosp/admissions.csv', usecols=admissions_cols)

# Filter by patient_ids
patients_filtered = patients_df[patients_df['subject_id'].isin(patient_ids)]
admissions_filtered = admissions_df[admissions_df['subject_id'].isin(patient_ids)]

# Perform inner join
patient_admissions_df = pd.merge(patients_filtered, admissions_filtered, on='subject_id', how='inner')

# Check resulting dataframe
print(patient_admissions_df.head())
# Save to CSV
patient_admissions_df.to_csv('New/PATIENTS_ADMISSIONS.csv', index=False)
