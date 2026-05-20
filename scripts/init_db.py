from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "trend_lab.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 既存テーブル削除
cursor.execute("DROP TABLE IF EXISTS raw_signals")

# 新テーブル作成
cursor.execute("""
CREATE TABLE IF NOT EXISTS raw_signals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    theme TEXT,
    seed_keyword TEXT,
    related_keyword TEXT,
    trend_score INTEGER,
    collected_date TEXT
)
""")

conn.commit()
conn.close()

print("DB初期化完了")