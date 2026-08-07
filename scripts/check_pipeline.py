import sqlite3, os

# NOTE: diagnostic-only utility. Queries the kanban DB for v4-era archetype
# keywords (Scrivener, Postilion, Tallow, ...) — not part of the current
# pipeline; kept for archaeology of old tasks.

db = os.path.expanduser('~/.hermes/kanban.db')
if os.path.exists(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    keywords = ['Scrivener', 'Postilion', 'Tallow', 'Gleaner', 'Carter', 
                'Sin-Eater', 'Purser', 'Remembrancer', 'Mudlark', 'Ombudsman',
                'sin-eater', 'purser', 'remembrancer', 'mudlark', 'ombudsman',
                'scrivener', 'postilion', 'tallow', 'gleaner', 'carter']
    like_clauses = ' OR '.join([f"title LIKE '%{k}%'" for k in keywords])
    cur.execute(f"SELECT id, title, status, assignee, created_at FROM tasks WHERE {like_clauses} ORDER BY created_at")
    rows = cur.fetchall()
    if rows:
        for r in rows:
            print(f'{r[0]:20s} | {r[1]:40s} | {r[2]:15s} | {r[3]:20s}')
    else:
        print('No matching tasks found')
    conn.close()
else:
    print('no kanban db found at', db)
