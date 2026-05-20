from pathlib import Path
import csv
import json
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = BASE_DIR / "data" / "ai_generated_posts.csv"
OUTPUT_JSON = BASE_DIR / "data" / "posts.json"

posts = []

with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for i, row in enumerate(reader, start=1):
        posts.append({
            "id": i,
            "name": row["title"],
            "source": "google_trends_ai",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "tags": row["tags"],
            "reason": row["reason"],
            "target": row["target"],
            "post": row["post"],
            "status": "未判定"
        })

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f"posts.json を生成しました：{len(posts)}件")