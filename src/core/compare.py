import datacompy
import pandas as pd
from src.core.source_mappings import *


# Compares the data
def compare(df1, df2, key):
    res = datacompy.Compare(
        df1, df2,
        join_columns=key,  # You can also specify a list of columns eg ['policyID','statecode']
        abs_tol=0,  # Optional, defaults to 0
        rel_tol=0,  # Optional, defaults to 0
        df1_name='Original',  # Optional, defaults to 'df1'
        df2_name='New')  # Optional, defaults to 'df2'

    return res.report()


# Checks if the selected source needs a query or a path
def fetch_connection_type(source):
    if source < 7:
        query = input("Enter the query for " + sources[source] + ":\n")
        return ['q', query]
    else:
        path = input("Enter the path for " + sources[source] + ":\n")
        return ['p', path]


# Fetches the data from connection provided and creates a data frame
def fetch_data(connection_type, connection):
    if connection_type[0] == 'q':
        sql_query = pd.read_sql_query(connection_type[1], connection)
        return pd.DataFrame(sql_query)
    else:
        if connection == 7: # For CSV
            return pd.read_csv(connection_type[1])
        elif connection == 8:   # For excel
            pass
        else:
            pass    # For txt


# Check for the type of source selected
def fetch_data_type(connection1, connection2, source1, source2):
    ct1 = fetch_connection_type(source1)
    ct2 = fetch_connection_type(source2)

    primary_key = input("Enter the primary key: \n")

    data1 = fetch_data(ct1, connection1)
    data2 = fetch_data(ct2, connection2)

    result = compare(data1, data2, primary_key)
    print(result)
    return
