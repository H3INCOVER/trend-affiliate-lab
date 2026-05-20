from pathlib import Path
import sqlite3
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "trend_lab.db"
OUTPUT_PATH = BASE_DIR / "data" / "trend_candidates.json"

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("""
SELECT
    id,
    seed,
    query,
    score,
    source,
    collected_at,
    is_product_candidate,
    created_at
FROM trend_candidates
ORDER BY collected_at DESC, score DESC
""")

rows = cur.fetchall()
conn.close()

data = []

for row in rows:
    data.append({
        "id": row["id"],
        "seed": row["seed"],
        "query": row["query"],
        "score": row["score"],
        "source": row["source"],
        "collectedAt": row["collected_at"],
        "isProductCandidate": bool(row["is_product_candidate"]),
        "createdAt": row["created_at"],
    })

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Exported: {OUTPUT_PATH}")
print(f"{len(data)} candidates exported.")