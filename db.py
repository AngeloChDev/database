import sqlite3

conn = sqlite3.connect('dbase.sql')
conn.execute('''
             CREATE TABLE IF NOT EXISTS DATA(
                 ID INT PRIMARY KEY NOT NULL,
                 QUARTIERE TEXT NOT NULL,
                 METRI INT NOT NULL,
                 PREZZO INT NOT NULL
                )
            ''')
conn.close()