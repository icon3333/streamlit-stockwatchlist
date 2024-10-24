import pandas as pd

def group_data(df, grouping_column):
    grouped_data = {}

    if pd.api.types.is_numeric_dtype(df[grouping_column]):
        # Numerical column, create quintiles
        df = df.copy()
        df['quintile'] = pd.qcut(df[grouping_column], 5, labels=False, duplicates='drop')
        for quintile in df['quintile'].unique():
            group_df = df[df['quintile'] == quintile]
            group_name = f"{grouping_column} Quintile {quintile + 1}"
            grouped_data[group_name] = group_df.drop(columns=['quintile'])
    else:
        # Categorical column
        for category in df[grouping_column].dropna().unique():
            group_df = df[df[grouping_column] == category]
            group_name = f"{grouping_column}: {category}"
            grouped_data[group_name] = group_df

    return grouped_data
