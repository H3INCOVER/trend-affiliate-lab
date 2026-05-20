from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "trend_lab.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
SELECT id, name, status, collected_at
FROM trends
ORDER BY id DESC
""")

rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()