import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully\n")

#conn.execute('DROP TABLE main.students')
conn.execute('CREATE TABLE dita (ID INTEGER PRIMARY KEY, title TEXT, form_name TEXT, short_desc TEXT, category1 TEXT, category2 TEXT, text1 TEXT, text1n TEXT, text2 TEXT, text2n TEXT, text3 TEXT, text3n TEXT, text4 TEXT, text4n TEXT, text5 TEXT, text5n TEXT, file1 TEXT, file1n TEXT, file2 TEXT, file2n TEXT, content TEXT, created_at TEXT, updated_at TEXT)')
print ("Table created successfully\n")
conn.close()
