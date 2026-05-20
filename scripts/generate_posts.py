from pathlib import Path
import sqlite3
import json
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "trend_lab.db"

OUTPUT_JSON = BASE_DIR / "data" / "draft_posts.json"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
SELECT
    theme,
    seed_keyword,
    related_keyword,
    trend_score
FROM raw_signals
ORDER BY trend_score DESC
LIMIT 30
""")

rows = cursor.fetchall()


def build_title(keyword, seed_keyword):
    keyword_lower = keyword.lower()

    if "pricing" in keyword_lower or "price" in keyword_lower:
        return f"{keyword}に、導入前確認の検索傾向が見られる"

    if "small business" in keyword_lower or "business" in keyword_lower:
        return f"{keyword}に、小規模業務導入を確認する検索傾向が見られる"

    if "testing" in keyword_lower or "test" in keyword_lower:
        return f"{keyword}に、実装精度を確認する検索傾向が見られる"

    if "next.js" in keyword_lower or "react" in keyword_lower:
        return f"{keyword}に、開発環境の変化を確認する検索傾向が見られる"

    if "code" in keyword_lower or "agent" in keyword_lower or "sdk" in keyword_lower:
        return f"{keyword}に、AI開発支援を確認する検索傾向が見られる"

    return f"{keyword}に、関連情報を確認する検索傾向が見られる"


def build_comment(keyword):
    keyword_lower = keyword.lower()

    # pricing系
    if "pricing" in keyword_lower or "price" in keyword_lower:
        return f"""最近、
「{keyword}」
系の検索が増えている。

単純な興味というより、

「実際いくらかかる？」
「継続利用できる？」
「業務へ入れると現実的？」

みたいな、
導入前確認の空気が強くなってきている感じある。

特に最近は、

AIを試す
↓
業務へ入れる
↓
費用確認

まで進む流れが、
かなり自然になってきている。

もし今から見るなら、

・無料枠
・従量課金
・チーム利用
・API料金

この辺から整理すると、
かなり掴みやすいと思う。
"""

    # small business系
    if "small business" in keyword_lower or "business" in keyword_lower:
        return f"""最近、
「{keyword}」
系の検索が増えている。

最初は、
AIを少し触ってみる、
くらいだったものが、

少しずつ、

「実際の仕事へ入る？」
「小さい会社でも使える？」
「どこから導入する？」

みたいな、
現実的な確認フェーズへ
移ってきている感じある。

特に、
大企業向けというより、

小規模運営や個人事業レベルで、
実際どう使うかを
調べる動きが増えているのかも。

もし今から触るなら、

・議事録
・問い合わせ返信
・メール整理

くらいから見ると、
かなりイメージ掴みやすいと思う。
"""

    # 開発・実装系
    if "testing" in keyword_lower or "test" in keyword_lower:
        return f"""最近、
「{keyword}」
系の検索が増えている。

単純に作るだけではなく、

「ちゃんと動く？」
「壊れない？」
「保守できる？」

みたいな、
実装精度を意識する空気が
少し強くなってきている感じある。

特に最近は、

AIで作る
↓
あとで困る
↓
テスト必要

という流れを経験した人も
増えてきているのかも。

もし今から見るなら、

・コンポーネント単位
・表示確認
・エラー検知

あたりから触ると、
かなり理解しやすいと思う。
"""

    # Next.js / React系
    if "next.js" in keyword_lower or "react" in keyword_lower:
        return f"""最近、
「{keyword}」
系の検索が増えている。

単なる学習というより、

「今どの作り方が普通？」
「新しい構成どう変わった？」
「実務ではどう使う？」

みたいな確認が、
かなり増えてきている感じある。

特に最近は、

AIで作れる
↓
でも構成理解は必要

という空気も強くなってきている。

もし今から触るなら、

・App Router
・components
・state
・server/client

この辺から見ると、
全体像かなり掴みやすいと思う。
"""

    # AI開発支援系
    if "code" in keyword_lower or "agent" in keyword_lower or "sdk" in keyword_lower:
        return f"""最近、
「{keyword}」
系の検索が増えている。

単なるAIチャットではなく、

「AIにどこまで任せられる？」
「開発へ組み込める？」
「自動化できる？」

みたいな方向へ、
関心が移ってきている感じある。

特に最近は、

コード生成
↓
修正補助
↓
エージェント化

まで視野へ入れる人も
増えてきているのかも。

もし今から見るなら、

・コード補助
・ファイル編集
・タスク分解

くらいから触ると、
かなりイメージ掴みやすいと思う。
"""

    # デフォルト
    return f"""最近、
「{keyword}」
系の検索が増えている。

単なる話題確認というより、

「実際どう使う？」
「今どこまで来てる？」
「何が変わった？」

みたいな、
確認目的の検索が
増えてきている感じある。

特に最近は、

AI
開発
自動化

あたりを、
実際の作業へ入れる流れが
かなり強くなってきている。

もし今から触るなら、

・小さい用途
・部分導入
・試験運用

くらいから始めると、
かなり理解しやすいと思う。
"""


posts = []

for row in rows:
    theme, seed_keyword, related_keyword, trend_score = row

    keyword = related_keyword

    title = build_title(keyword, seed_keyword)

    tags = [
        seed_keyword,
        "Google Trends",
        "観測"
    ]

    comment = build_comment(keyword)

    posts.append({
        "title": title,
        "tags": tags,
        "comment": comment,
        "keyword": keyword,
        "trend_score": trend_score,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    })

conn.close()

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f"posts.json生成完了: {OUTPUT_JSON}")