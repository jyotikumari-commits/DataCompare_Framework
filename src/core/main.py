from src.core import compare
from src.sources import sqlserver as sqlparam


def function(argument1, argument2):
    files = []
    switcher = {
        1: "sqlparam.sqlserver()",
        2: "one",
        3: "two",
    }

    files.append(switcher[argument1])
    files.append(switcher[argument2])

    return files

if __name__ == '__main__':
    sources = {1: 'SQL Server',
               2: 'Oracle',
               3: 'MongoDb',
               4: 'CSV'}



    print("\nList of sources")
    for source in sources:
        print(source, '->', sources[source])

    source1 = int(input("\nSelect Source 1 - Enter the number associated with source\n"))
    source2 = int(input("Select Source 2 - Enter the number associated with source\n"))

    print("\nSelected source 1 is: " + sources[source1] + "\nSelected source 2 is: " + sources[source2] + "\n")

    ## Sql Server
    if sources[source1] == 'SQL Server':
        sqlparam.sqlserver()

    # sqlquery = input("Enter the SQL Query: \n")
    # uniquekey = input("Enter the unique key/business key: \n")
    #
    # if sources[source2] == 'CSV':
    #     path = input("Enter the file path: \n")
    #
    # result = compare.data(connection, path, sqlquery, uniquekey)
    #
    # if result:
    #     sqlconn.close_connection()




