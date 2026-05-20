from pathlib import Path
import sqlite3
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "trend_lab.db"
JSON_PATH = BASE_DIR / "data" / "posts.json"

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("""
SELECT
    id,
    name,
    source,
    collected_at,
    tags,
    reason,
    target,
    post,
    status
FROM trends
ORDER BY id DESC
""")

rows = cur.fetchall()

posts = []

for row in rows:
    posts.append({
        "id": row["id"],
        "name": row["name"],
        "source": row["source"],
        "date": row["collected_at"][:10],
        "tags": row["tags"] or "",
        "reason": row["reason"] or "",
        "target": row["target"] or "",
        "post": row["post"] or "",
        "status": row["status"] or "hold",
    })

conn.close()

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("DB から posts.json を生成しました")