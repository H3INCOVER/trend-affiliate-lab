import subprocess
import sys

theme = sys.argv[1] if len(sys.argv) > 1 else "manabu"

commands = [
    ["python", "scripts/collect_trends.py", theme],
    ["python", "scripts/generate_posts.py"],
    ["python", "scripts/generate_ai_posts_draft.py"],
    ["python", "scripts/export_posts_from_csv.py"],
]

for command in commands:
    print("実行:", " ".join(command))
    subprocess.run(command, check=True)

print(f"{theme} の更新が完了しました。")