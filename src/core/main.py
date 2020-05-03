from src.core import compare
from src.core.source_mappings import *


def close_connection_type(connection):
    if source < 7:
        return sourceMap[sources[connection]].close_connection()
    else:
        return connection


# Opens connection if the selected source is a database
def open_connection_type(source_type):
    if source_type < 7:
        return sourceMap[sources[source_type]].open_connection()
    else:
        return source_type


if __name__ == '__main__':
    # prints list of available sources
    print("\nList of auth")
    for source in sources:
        print(source, '->', sources[source])

    source1 = int(input("\nSelect Source 1 - Enter the number associated with source\n"))
    source2 = int(input("Select Source 2 - Enter the number associated with source\n"))

    print("\nSelected source 1 is: " + sources[source1] + "\nSelected source 2 is: " + sources[source2] + "\n")

    # Opens the connection if the selected source is a database else takes the path
    connection1 = open_connection_type(source1)
    connection2 = open_connection_type(source2)

    # Passing control to Compare.py
    compare.fetch_data_type(connection1, connection2, source1, source2)

    # Closing the connection if the sources are databases
    close_connection_type(source1)
    close_connection_type(source2)

    print("Data comparison successful")
