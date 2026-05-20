from pathlib import Path
import sqlite3
import csv

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "trend_lab.db"
OUTPUT_PATH = BASE_DIR / "data" / "raw_signals.csv"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
SELECT
    id,
    title,
    url,
    source,
    collected_at
FROM raw_signals
ORDER BY id DESC
""")

rows = cur.fetchall()

conn.close()

with open(OUTPUT_PATH, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)

    writer.writerow([
        "id",
        "title",
        "url",
        "source",
        "collected_at"
    ])

    writer.writerows(rows)

print(f"Exported: {OUTPUT_PATH}")