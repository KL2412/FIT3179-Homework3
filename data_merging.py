# import pandas as pd

# data = pd.read_csv('Dataset\data1.csv')
# pop = pd.read_csv('Dataset\\total_population.csv')

# # Merge the datasets on 'country_code'
# combined_data = pd.merge(data, pop, on='country_code', how='left')

# # Drop duplicate rows, if any
# combined_data = combined_data.drop_duplicates()

# # Save the combined data for use in the Vega-Lite visualization
# combined_data.to_csv('data2.csv', index=False)

# import pandas as pd

# # Load the datasets
# population_df = pd.read_csv('Dataset\merged_countries_population.csv')
# medals_df = pd.read_csv('Dataset/medals_total.csv')

# # Merge the datasets on the 'country_code' column
# merged_df = pd.merge(population_df, medals_df, on='country_code', how='left')

# # Fill missing values with 0
# merged_df.fillna(0, inplace=True)

# print(merged_df.columns)

# # Print out the countries in medals_total.csv that have no match in total_population.csv
# no_match_df = merged_df[merged_df['Gold Medal'] == 0]
# print(no_match_df[['country_code', 'country', 'country_long_y']])

# # Save the merged dataset to a new CSV file
# merged_df.to_csv('Dataset/merged_medals_population.csv', index=False)

# print("Merge completed successfully.")