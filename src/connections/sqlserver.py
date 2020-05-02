import pyodbc


class SqlServer:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.conn = ''

    def non_windows_authentication(self, username, password):
        username = username
        password = password

        try:

            self.conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                                       'Server=' + self.server +
                                       ';Database=' + self.database +
                                       ';username=' + username +
                                       ';password=' + password +
                                       ';Trusted_Connection=yes;')

            return self.conn

        except pyodbc.Error as err:
            print("Error while connecting to Server")
            print(err)

    def windows_authentication(self):
        try:
            self.conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                                       'Server=' + self.server +
                                       ';Database=' + self.database +
                                       ';Trusted_Connection=yes;')

            return self.conn

        except pyodbc.Error as err:
            print("Error while connecting to Server")
            print(err)

    def close_connection(self):
        self.conn.close()
