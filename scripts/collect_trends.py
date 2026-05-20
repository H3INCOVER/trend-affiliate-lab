from pathlib import Path
import sqlite3
from datetime import datetime
import sys
from pytrends.request import TrendReq

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "trend_lab.db"

# テーマ指定
theme = sys.argv[1] if len(sys.argv) > 1 else "manabu"

# seedファイル
SEED_FILE = BASE_DIR / "data" / "seeds" / f"{theme}.txt"

# Google Trends 接続
pytrends = TrendReq(hl="ja-JP", tz=540)

# seed読み込み
with open(SEED_FILE, "r", encoding="utf-8") as f:
    keywords = [line.strip() for line in f if line.strip()]

# DB接続
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 今日の日付
today = datetime.now().strftime("%Y-%m-%d")

# 今日すでに取得済みか確認
cursor.execute(
    """
    SELECT COUNT(*)
    FROM raw_signals
    WHERE theme = ?
    AND collected_date = ?
    """,
    (theme, today)
)

count = cursor.fetchone()[0]

if count > 0:
    print(f"{theme} は今日はすでに {count} 件取得済みです。")
    conn.close()
    exit()

# Trends取得
all_rows = []

for keyword in keywords:
    print(f"取得中: {keyword}")

    try:
        pytrends.build_payload(
            [keyword],
            cat=0,
            timeframe="now 7-d",
            geo="JP",
            gprop=""
        )

        related_queries = pytrends.related_queries()

        if keyword not in related_queries:
            continue

        rising = related_queries[keyword]["rising"]

        if rising is None:
            continue

        for _, row in rising.iterrows():
            query = row["query"]
            value = row["value"]

            all_rows.append(
                (
                    theme,
                    keyword,
                    query,
                    value,
                    today
                )
            )

    except Exception as e:
        print(f"エラー: {keyword} -> {e}")

# DB保存
cursor.executemany(
    """
    INSERT INTO raw_signals
    (
        theme,
        seed_keyword,
        related_keyword,
        trend_score,
        collected_date
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    all_rows
)

conn.commit()

print(f"{theme} : {len(all_rows)} 件保存しました。")

conn.close()