import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

POSTS_PATH = BASE_DIR / "data" / "posts.json"
OUTPUT_PATH = BASE_DIR / "data" / "grouped_posts.json"

# posts.json 読み込み
with open(POSTS_PATH, "r", encoding="utf-8") as f:
    posts = json.load(f)

groups = {}

# Claude系まとめ
CLAUDE_KEYWORDS = [
    "claude",
]

# ChatGPT系
CHATGPT_KEYWORDS = [
    "chatgpt",
]

# Cursor系
CURSOR_KEYWORDS = [
    "cursor",
]

for post in posts:
    name = post["name"].lower()

    group_name = None

    if any(k in name for k in CLAUDE_KEYWORDS):
        group_name = "Claude業務導入"

    elif any(k in name for k in CHATGPT_KEYWORDS):
        group_name = "ChatGPT活用"

    elif any(k in name for k in CURSOR_KEYWORDS):
        group_name = "AIコーディング"

    else:
        group_name = "その他"

    if group_name not in groups:
        groups[group_name] = []

    groups[group_name].append(post)

# grouped形式へ変換
output = []

for group_name, items in groups.items():

    keywords = [item["name"] for item in items[:6]]

    if group_name == "Claude業務導入":

        summary = """
Claude、
「個人利用」
より
“業務導入”
系検索かなり増えてる。
""".strip()

    elif group_name == "ChatGPT活用":

        summary = """
「AIに聞きながら進める」
前提、
かなり普通になってきた感じある。
""".strip()

    elif group_name == "AIコーディング":

        summary = """
「自分で全部書く」
より、
AIと一緒に作る空気、
かなり強くなってる。
""".strip()

    else:

        summary = "最近少しずつ検索が増えてる話題。"

    output.append({
        "topic": group_name,
        "summary": summary,
        "keywords": keywords,
        "count": len(items)
    })

# 保存
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"{len(output)} グループ生成しました。")