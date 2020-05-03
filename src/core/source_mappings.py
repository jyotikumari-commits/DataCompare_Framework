from src.auth import sqlserver

sources = {
        1: 'SQL Server',
        2: 'Oracle',
        3: 'MongoDb',
        4: 'Postgre SQL',
        5: 'IBM db2',
        6: 'My SQL',
        7: 'CSV',
        8: 'Excel',
        9: 'Txt File'
    }

sourceMap = {
        'SQL Server': sqlserver,
        'Oracle': 'oracle'
    }