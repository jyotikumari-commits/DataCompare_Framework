from src.connections import sqlserver as conn_class

global sql_conn


def close_connection():
    sql_conn.close_connection()


def open_connection():
    server = input("Enter the SQL server name:\n")
    database = input("Enter the database name:\n")

    sql_conn = conn_class.SqlServer(server, database)

    authentication = input("Connect using windows authentication(y/n):\n")

    if authentication == 'n':
        username = input("Enter the username:\n")
        password = input("Enter the password:\n")
        connection = sql_conn.non_windows_authentication(username, password)
    else:
        connection = sql_conn.windows_authentication()

    return connection
