from pathlib import Path
import sqlite3
import csv
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = BASE_DIR / "data" / "ai_posts.csv"
DB_PATH = BASE_DIR / "data" / "trend_lab.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

inserted_count = 0

with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row["name"].strip()
        tags = row["tags"].strip()
        reason = row["reason"].strip()
        target = row["target"].strip()
        post = row["post"].strip()
        status = row["status"].strip()

        # 重複チェック
        cur.execute("""
            SELECT id FROM trends
            WHERE name = ?
        """, (name,))

        exists = cur.fetchone()

        if exists:
            continue

        cur.execute("""
            INSERT INTO trends (
                name,
                source,
                collected_at,
                tags,
                reason,
                target,
                post,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        """, (
            name,
            "google_trends_ai",
            datetime.now().strftime("%Y-%m-%d"),
            tags,
            reason,
            target,
            post,
            status
        ))

        inserted_count += 1

conn.commit()
conn.close()

print(f"AI投稿をDBへ追加しました：{inserted_count}件")