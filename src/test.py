import datacompy
import pandas as pd
import pyodbc


conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                'Server=ITT-AKSHAY;'
                                'Database=AdventureWorks2017;'
                                'Trusted_Connection=yes;')

query = 'SELECT [BusinessEntityID],[PasswordHash],[PasswordSalt],[rowguid],[ModifiedDate] FROM [Person].[Password]'
path = 'C:\\Users\\akshay.telkar\\PycharmProjects\\DataComparison\\test.csv'

SQL_Query = pd.read_sql_query(query, conn)

df = pd.DataFrame(SQL_Query)


df1 = pd.read_csv(path)
# df2 = pd.read_csv('C:\\Users\\akshay.telkar\\PycharmProjects\\DataComparison\\test - Copy.csv')

compare = datacompy.Compare(
    df,df1,
    join_columns='BusinessEntityID',  #You can also specify a list of columns eg ['policyID','statecode']
    abs_tol=0, #Optional, defaults to 0
    rel_tol=0, #Optional, defaults to 0
    df1_name='Original', #Optional, defaults to 'df1'
    df2_name='New' #Optional, defaults to 'df2'
)
print(compare.report())