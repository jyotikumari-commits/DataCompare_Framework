import datacompy
import pandas as pd


def compare(df1, df2, key):
    res = datacompy.Compare(
        df1, df2,
        join_columns = key,  # You can also specify a list of columns eg ['policyID','statecode']
        abs_tol = 0,  # Optional, defaults to 0
        rel_tol = 0,  # Optional, defaults to 0
        df1_name = 'Original',  # Optional, defaults to 'df1'
        df2_name = 'New')  # Optional, defaults to 'df2'

    return res.report()


def data(connection1, connection2, query, uniquekey):
    SQL_Query = pd.read_sql_query(query, connection1)
    dataframe1 = pd.DataFrame(SQL_Query)
    dataframe2 = pd.read_csv(connection2)
    result = compare(dataframe1, dataframe2, uniquekey)
    print(result)
    return
