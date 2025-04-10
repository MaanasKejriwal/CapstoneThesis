import pandas as pd

# Define your files and which columns to use
tables_info = [
    ('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/New/PATIENTS_ADMISSIONS.csv', ['subject_id','gender','anchor_age','anchor_year','dod','hadm_id','admittime','dischtime','admission_type','admission_location','discharge_location','hospital_expire_flag'], 'admissions'),
    ('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/New/DIAGNOSES_ICD_LABELED.csv', ['hadm_id','icd_code','icd_version','long_title'], 'diagnoses'),
    ('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/New/LABEVENTS_LABELED.csv', ['labevent_id','hadm_id','specimen_id','itemid','order_provider_id','charttime','storetime','value','valuenum','valueuom','ref_range_lower','ref_range_upper','flag'], 'labs'),
    ('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/New/PROCEDURES_ICD_LABELED.csv', ['hadm_id','icd_code','icd_version','long_title'], 'procedures'),
    ('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/New/CHARTEVENTS_LABELED.csv', ['hadm_id','stay_id','caregiver_id','charttime','storetime','itemid','value','valuenum','valueuom','warning','label'], 'chartevents'),
    ('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/New/inputevents_LABELED.csv', ['hadm_id','stay_id','caregiver_id','starttime','endtime','storetime','itemid','amount','amountuom','rate','rateuom','orderid','linkorderid','ordercategoryname','secondaryordercategoryname','ordercomponenttypedescription','ordercategorydescription','patientweight','totalamount','totalamountuom','isopenbag','continueinnextdept','statusdescription','originalamount','originalrate','label'], 'inputevents'),
    ('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/New/procedureevents_LABELED.csv', ['hadm_id','stay_id','caregiver_id','starttime','endtime','storetime','itemid','value','valueuom','location','locationcategory','orderid','linkorderid','ordercategoryname','ordercategorydescription','patientweight','isopenbag','continueinnextdept','statusdescription','ORIGINALAMOUNT','ORIGINALRATE','label'], 'procedureevents')
]

# Helper function: load and rename columns
def load_and_rename(file_path, cols, suffix):
    df = pd.read_csv(file_path, usecols=cols)
    rename_map = {col: f"{col}_{suffix}" for col in df.columns if col != 'hadm_id'}
    return df.rename(columns=rename_map)

# Start with the first table
file_path, cols, suffix = tables_info[0]
merged = load_and_rename(file_path, cols, suffix)

# Progressively merge one table at a time
for file_path, cols, suffix in tables_info[1:]:
    print(f"Merging with {file_path}...")
    next_table = load_and_rename(file_path, cols, suffix)
    merged = pd.merge(merged, next_table, on='hadm_id', how='outer')
    
    # Save after every merge (optional but safe)
    merged.to_csv('intermediate_merged.csv', index=False)
    print(f"Saved intermediate after merging {file_path}")

# Save the final version
merged.to_csv('final_merged_table.csv', index=False)
print("\n🎉 Final merged table created successfully: final_merged_table.csv")
