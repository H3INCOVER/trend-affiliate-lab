from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "trend_lab.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

try:
    cur.execute("""
        ALTER TABLE trends
        ADD COLUMN tags TEXT
    """)

    print("tags カラムを追加しました")

except sqlite3.OperationalError as e:
    print("すでに追加済みの可能性:", e)

conn.commit()
conn.close()