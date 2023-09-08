import sqlite3

connection = sqlite3.connect("itstep_DB.sl3",5)
cur = connection.cursor()
#cur.execute("DROP TABLE first_table;")
cur.execute("INSERT INTO first_table (name, temperature) VALUES ('Kremenchyg','22');")
#cur.execute("CREATE TABLE first_table (name TEXT, temperature TEXT);")
#cur.execute("DELETE FROM first_table WHERE rowid=1;")
#cur.execute("SELECT rowid, name FROM first_table WHERE rowid = 3;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()