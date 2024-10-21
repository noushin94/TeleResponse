
#checking for which column have null values and how many
def null_value_check(df):
    list_column = df.isnull().sum().to_list()  # List of null counts for each column
    null_column = {}

    # Iterate through the list of columns and check for non-zero null counts
    for column in range(len(list_column)):
        if list_column[column] != 0:
            # Assign the column name as the key and the null count as the value
            null_column[df.columns[column]] = list_column[column]

    # Print the columns with their respective null values
    print(f"These columns have null values: {null_column}")



#checking columns type
def columns_type(df):
    num_obj_column = 0
    num_int_column = 0 
    num_flt_column = 0 

    # Loop through each column in the dataframe
    for column in df.columns:
        if df[column].dtype == "object":
            num_obj_column += 1
        elif df[column].dtype == "int64":
            num_int_column += 1
        elif df[column].dtype == "float64":
            num_flt_column += 1

    print(f"This data has {num_obj_column} object columns and {num_int_column} integer columns and {num_flt_column} float columns")

    # Optionally return the counts if needed
    return num_obj_column, num_int_column, num_flt_column


