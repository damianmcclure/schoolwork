import sqlite3
import hashlib

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

#cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

cur.execute('DELETE FROM Ages;')
cur.execute('INSERT INTO Ages (name, age) VALUES (\'Samarjit\', 30);')
cur.execute('INSERT INTO Ages (name, age) VALUES (\'Sohaib\', 18);')
cur.execute('INSERT INTO Ages (name, age) VALUES (\'Seatle\', 32);')
cur.execute('INSERT INTO Ages (name, age) VALUES (\'Jaymi\', 38);')

cur.execute('SELECT name || age AS X FROM Ages ORDER BY X;')
for row in cur:
    print(hashlib.sha1(row[0].encode()).hexdigest())

conn.close()
