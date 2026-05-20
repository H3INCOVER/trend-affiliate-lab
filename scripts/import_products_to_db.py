from pathlib import Path
import sqlite3
import csv
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = BASE_DIR / "data" / "products.csv"
DB_PATH = BASE_DIR / "data" / "trend_lab.db"

today = datetime.now().date().isoformat()
now = datetime.now().isoformat()

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

added_count = 0
skip_count = 0

with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row["name"].strip()

        if not name:
            continue

        # 同じ日に同じ商品名がすでに入っていたらスキップ
        cur.execute("""
            SELECT COUNT(*)
            FROM trends
            WHERE name = ?
            AND date(collected_at) = ?
        """, (name, today))

        exists = cur.fetchone()[0]

        if exists:
            skip_count += 1
            continue

        cur.execute("""
            INSERT INTO trends (
                name,
                source,
                collected_at,
                status
            )
            VALUES (?, ?, ?, ?)
        """, (
            name,
            "csv_import",
            now,
            "hold"
        ))

        added_count += 1

conn.commit()
conn.close()

print(f"DB取り込み完了：追加 {added_count}件 / スキップ {skip_count}件")