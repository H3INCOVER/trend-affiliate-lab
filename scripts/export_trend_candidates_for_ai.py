import sqlite3
import csv
from pathlib import Path

# DBパス
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "trend_lab.db"

# 出力CSV
OUTPUT_PATH = BASE_DIR / "data" / "ai_input_trend_candidates.csv"

# DB接続
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# trend_candidates取得
cursor.execute("""
SELECT
    id,
    query,
    seed,
    score,
    source,
    collected_at,
    is_product_candidate
FROM trend_candidates
ORDER BY score DESC
""")

rows = cursor.fetchall()

# CSV出力
with open(OUTPUT_PATH, "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)

    # ヘッダー
    writer.writerow([
        "id",
        "query",
        "seed",
        "score",
        "source",
        "collected_at",
        "is_product_candidate"
    ])

    # データ
    writer.writerows(rows)

conn.close()

print(f"AI入力CSVを出力しました: {OUTPUT_PATH}")