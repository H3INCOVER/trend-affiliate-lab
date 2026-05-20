from pathlib import Path
import csv
from patterns import generate_title

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_CSV = BASE_DIR / "data" / "ai_input.csv"
OUTPUT_CSV = BASE_DIR / "data" / "ai_generated_posts.csv"

def make_reason(seed_keyword, related_keyword):
    return f"「{related_keyword}」という検索が出ており、{seed_keyword}周辺で具体的な関心が見えます。"

def make_target(seed_keyword):
    if "NISA" in seed_keyword or "お金" in seed_keyword:
        return "お金の勉強をしている人・制度を確認したい人"
    if "行政書士" in seed_keyword or "宅建" in seed_keyword or "FP" in seed_keyword or "簿記" in seed_keyword:
        return "資格学習中の社会人・独学で勉強している人"
    if "CBT" in seed_keyword:
        return "CBT形式の試験を受ける予定の人"
    return "学び直しや情報収集をしている人"

def make_tags(seed_keyword):
    if "NISA" in seed_keyword or "お金" in seed_keyword:
        return "お金|学び直し|制度"
    if "行政書士" in seed_keyword:
        return "資格|行政書士|学習"
    if "CBT" in seed_keyword:
        return "資格|CBT|試験"
    return "学習|トレンド|観測"

def make_post(related_keyword):
    return f"最近『{related_keyword}』を調べる人が出てきてる。\n\nこういう検索ワードを見ると、今どこに不安や関心があるのか少し見える。"

with open(INPUT_CSV, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)

    writer.writerow([
        "seed_keyword",
        "related_keyword",
        "trend_score",
        "title",
        "reason",
        "target",
        "post",
        "tags"
    ])

    for row in rows:
        seed_keyword = row["seed_keyword"]
        related_keyword = row["related_keyword"]
        trend_score = row["trend_score"]

        title = generate_title(related_keyword)
        reason = make_reason(seed_keyword, related_keyword)
        target = make_target(seed_keyword)
        post = make_post(related_keyword)
        tags = make_tags(seed_keyword)

        writer.writerow([
            seed_keyword,
            related_keyword,
            trend_score,
            title,
            reason,
            target,
            post,
            tags
        ])

print(f"ai_generated_posts.csv を生成しました：{len(rows)}件")