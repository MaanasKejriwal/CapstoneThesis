import pandas as pd

# Load dataframes
labevents_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/hosp/labevents.csv')
d_labitems_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/hosp/d_labitems.csv', usecols=['itemid', 'label'])

# Perform join on 'itemid' to add 'label' to labevents
labevents_labeled_df = pd.merge(
    labevents_df, 
    d_labitems_df, 
    on='itemid', 
    how='left'
)

# Save the resulting dataframe to a new CSV file
labevents_labeled_df.to_csv('New/LABEVENTS_LABELED.csv', index=False)

# Check resulting dataframe
print(labevents_labeled_df.head())
