def split_function():
    import pandas as pd

    # create variable with file
    excel_file = 'excel_main.xlsx'

    # create df with file
    df=pd.read_excel(excel_file)

    # sort rows in ascending order respect 'COMPANY' column
    df_sorted = df.sort_values('COMPANY')

    # editing column to convert to upper case elements from 'COMPANY' column, converting to string and then with upper()
    df_sorted['COMPANY'] = df_sorted['COMPANY'].str.upper()

    #   creation of two new columns  /     select column 'NAME' / conver to string /then splt words / True creates columns in df. False creates a list
    df_sorted[['FIRST NAME', 'LAST NAME']] = df_sorted['NAME'].str.split(',', expand=True)
    # these two columns are added to final
    #we want to insert these columns in specific position

    # get the position where we want to put the new columns, identifying the column that we will displace
    c_position = df_sorted.columns.get_loc('TYPE')

    # inserting the columns
    #     specific index of column / name of column / values to insert, we add pop, to eliminate column added previusly and to return a serie 
    df_sorted.insert(c_position, 'FIRST NAME', df_sorted.pop('FIRST NAME'))
    df_sorted.insert(c_position+1, 'LAST NAME', df_sorted.pop('LAST NAME'))

    # create a new file with the changes
    df_sorted.to_excel('file_after_split.xlsx', index=False)
    #print(df_sorted)


if __name__ == "__main__":
    split_function()