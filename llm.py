import pandas as pd
import openai  # or your Meditron client

# Load your intermediate CSV
df = pd.read_csv('path_to_your_intermediate_table.csv')

# Group by patient
patients = df.groupby('subject_id_admissions')

# LLM call function
def generate_summary(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or 'meditron', etc.
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']

# Updated prompt builder
def build_prompt(patient_df):
    # Use .iloc[0] to pick patient-level static values
    demographics = f"""- Gender: {patient_df['gender_admissions'].iloc[0]}
- Age: {patient_df['anchor_age_admissions'].iloc[0]}
- Anchor Year: {patient_df['anchor_year_admissions'].iloc[0]}
- Date of Death (if any): {patient_df['dod_admissions'].iloc[0]}"""

    admission_details = f"""- Admission ID: {patient_df['hadm_id'].iloc[0]}
- Admission Time: {patient_df['admittime_admissions'].iloc[0]}
- Discharge Time: {patient_df['dischtime_admissions'].iloc[0]}
- Admission Type: {patient_df['admission_type_admissions'].iloc[0]}
- Admission Location: {patient_df['admission_location_admissions'].iloc[0]}
- Discharge Location: {patient_df['discharge_location_admissions'].iloc[0]}
- Hospital Expired (1=Yes, 0=No): {patient_df['hospital_expire_flag_admissions'].iloc[0]}"""

    diagnoses = '; '.join(patient_df['long_title_diagnoses'].dropna().unique()) or "None listed"

    procedures = '; '.join(patient_df['long_title_procedures'].dropna().unique()) or "None listed"

    # Only keep labs that have a recorded value
    labs_df = patient_df.dropna(subset=['value_labs'])
    labs = '\n'.join([
        f"{row['charttime_labs']} - {row['itemid_labs']}: {row['value_labs']} {row['valueuom_labs']} (Ref: {row['ref_range_lower_labs']}–{row['ref_range_upper_labs']})"
        for _, row in labs_df.iterrows()
    ]) or "None listed"

    # Final prompt
    prompt = f"""
You are a clinical summarization assistant. Summarize the patient's hospital stay based on the structured data provided below. Maintain a formal, clinical tone. Avoid adding any fabricated information. If any section is missing, note it as \"Not available\".

Patient Demographics:
{demographics}

Admission Details:
{admission_details}

Diagnoses:
{diagnoses}

Procedures:
{procedures}

Lab Results:
{labs}

Please organize the output with clear section headings. Be precise and avoid redundant information.
"""
    return prompt

# Summarization loop
summaries = {}
for subject_id, patient_df in patients:
    prompt = build_prompt(patient_df)
    summary = generate_summary(prompt)
    summaries[subject_id] = summary

# Save summaries
pd.Series(summaries).to_csv('patient_summaries_current.csv')

