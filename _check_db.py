import sqlite3
db = sqlite3.connect('/home/kimbo/.hermes/kanban/boards/job-search/kanban.db')
cur = db.execute('SELECT name FROM sqlite_master WHERE type="table"')
tables = cur.fetchall()
print('Tables:', tables)
for t in tables:
    tname = t[0]
    cur2 = db.execute(f'SELECT * FROM {tname} LIMIT 10')
    cols = [d[0] for d in cur2.description]
    rows = cur2.fetchall()
    print(f'\n--- {tname} ({cols}) ---')
    for r in rows:
        print(r)
db.close()