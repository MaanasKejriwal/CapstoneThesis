import pandas as pd

# Load dataframes
chartevents_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/icu/chartevents.csv')
d_items_df = pd.read_csv('/Users/maanas/Desktop/Ashoka/ASP/Sem 8/Capstone Thesis/mimic-iv-clinical-database-demo-2.2/icu/d_items.csv', usecols=['itemid', 'label'])

# Perform join on 'itemid' to add 'label' to chartevents
chartevents_labeled_df = pd.merge(
    chartevents_df, 
    d_items_df, 
    on='itemid', 
    how='left'
)

# Save the resulting dataframe to a new CSV file
chartevents_labeled_df.to_csv('New/CHARTEVENTS_LABELED.csv', index=False)

# Check resulting dataframe
print(chartevents_labeled_df.head())

