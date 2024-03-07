def merge_function():
    import pandas as pd


    # Read  files
    df_after_split = pd.read_excel('file_after_split.xlsx')
    df_location = pd.read_excel('Locacion.xlsx')

    # sort values
    df_after_split = df_after_split.sort_values('STATE')
    df_location = df_location.sort_values('STATE')

    # Merge on STATE
    merged_df = pd.merge(df_location,df_after_split, on='STATE', how='left')

    # change name
    merged_df = merged_df.rename(columns={'CITY':'CIUDAD'})

    # Get location
    location = merged_df.columns.get_loc('CAPITAL')

    # Relocation of two columns 'CAPITAL', 'CIUDAD'
    merged_df.insert(location, 'FIRST NAME', merged_df.pop('FIRST NAME'))
    merged_df.insert(location+1, 'LAST NAME', merged_df.pop('LAST NAME'))


    sorted_merged_df = merged_df.sort_values('COMPANY')

    merged_df.to_excel('merged.xlsx', index=False)
    

if __name__ == "__main__":
    merge_function()
