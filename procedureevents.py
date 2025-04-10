import pandas as pd

# Load dataframes
procedureevents_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/icu/procedureevents.csv')
d_items_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/icu/d_items.csv', usecols=['itemid', 'label'])

# Perform join on 'itemid' to add 'label' to procedureevents
procedureevents_labeled_df = pd.merge(
    procedureevents_df, 
    d_items_df, 
    on='itemid', 
    how='left'
)

# Save the resulting dataframe to a new CSV file
procedureevents_labeled_df.to_csv('New/procedureevents_LABELED.csv', index=False)

# Check resulting dataframe
print(procedureevents_labeled_df.head())
