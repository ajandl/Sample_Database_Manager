import sqlite3
import os


class ConnectionManager:

    def __init__(self, db_path):
        self.db_path = db_path

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        print('Connection closed')


# db_path = os.path.join(os.getcwd(), 'DummyDB', 'DummyDb1.db')

# with ConnectionManager(db_path) as con:
#     cur = con.cursor()
#     table_sql = '''CREATE TABLE IF NOT EXISTS Table1 (
#                     ID INTEGER PRIMARY KEY,
#                     Title VARCHAR(50))'''
#     cur.execute(table_sql)
#     cur.execute('''INSERT INTO Table1 
#                     VALUES (?, ?)''', (None, 'Other Title...'))
#     cur.execute('''SELECT * FROM Table1''')
#     selection = cur.fetchall()
#     for i in selection:
#         print(i)
#     cur.execute('''DROP TABLE Table1''')
#     con.commit()