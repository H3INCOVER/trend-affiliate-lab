from pathlib import Path
import shutil
import subprocess
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

DRAFT_JSON = BASE_DIR / "data" / "draft_posts.json"
PUBLISHED_JSON = BASE_DIR / "data" / "published_posts.json"


def run(command):
    result = subprocess.run(
        command,
        cwd=BASE_DIR,
        shell=True,
        text=True,
        capture_output=True,
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        raise RuntimeError(f"コマンド失敗: {command}")


if not DRAFT_JSON.exists():
    raise FileNotFoundError(f"draft_posts.json が見つかりません: {DRAFT_JSON}")

shutil.copyfile(DRAFT_JSON, PUBLISHED_JSON)

print(f"公開用JSONへコピー完了: {PUBLISHED_JSON}")

run("git add data/published_posts.json data/draft_posts.json")

commit_message = f"Update posts {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

run(f'git commit -m "{commit_message}"')

run("git push")

print("GitHub push 完了。Vercel が自動反映します。")