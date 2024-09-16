import pandas as pd

coords = pd.read_csv('Homework 3\Dataset\\total_population.csv')
medals = pd.read_csv('Homework 3\Dataset\chloropleth_data.csv')

# Merge the datasets on 'country_code'
combined_data = pd.merge(medals, coords, on='country_code')

# Drop duplicate rows, if any
combined_data = combined_data.drop_duplicates()
print(combined_data)

# Save the combined data for use in the Vega-Lite visualization
combined_data.to_csv('data.csv', index=False)