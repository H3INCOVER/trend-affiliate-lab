from pathlib import Path
import sqlite3
import feedparser
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "trend_lab.db"

RSS_FEEDS = [
    {
        "name": "ITmedia AI+",
        "url": "https://rss.itmedia.co.jp/rss/2.0/aiplus.xml"
    },
    {
        "name": "GIGAZINE",
        "url": "https://gigazine.net/news/rss_2.0/"
    }
]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

count = 0

for feed in RSS_FEEDS:
    parsed = feedparser.parse(feed["url"])

    for entry in parsed.entries:
        title = entry.title
        url = entry.link

        collected_at = datetime.now().strftime("%Y-%m-%d")

        try:
            cur.execute("""
                INSERT INTO raw_signals (
                    title,
                    url,
                    source,
                    collected_at
                )
                VALUES (?, ?, ?, ?)
            """, (
                title,
                url,
                feed["name"],
                collected_at
            ))

            count += 1

        except sqlite3.IntegrityError:
            # URL重複は無視
            pass

conn.commit()
conn.close()

print(f"{count} signals collected.")