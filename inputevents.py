import pandas as pd

# Load dataframes
inputevents_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/icu/inputevents.csv')
d_items_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/icu/d_items.csv', usecols=['itemid', 'label'])

# Perform join on 'itemid' to add 'label' to inputevents
inputevents_labeled_df = pd.merge(
    inputevents_df, 
    d_items_df, 
    on='itemid', 
    how='left'
)

# Save the resulting dataframe to a new CSV file
inputevents_labeled_df.to_csv('New/inputevents_LABELED.csv', index=False)

# Check resulting dataframe
print(inputevents_labeled_df.head())
