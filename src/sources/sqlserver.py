from src.connections import sqlserver as connclass


def sqlserver():
    global connection, path, sqlconn
    server = input("Enter the server name:\n")
    database = input("Enter the database name:\n")

    sqlconn = connclass.SqlServer(server, database)

    authentication = input("Connect using windows authentication(y/n):\n")

    if authentication == 'n':
        username = input("Enter the username:\n")
        password = input("Enter the password:\n")
        connection = sqlconn.non_windows_authentication(username, password)

    else:
        connection = sqlconn.windows_authentication()

