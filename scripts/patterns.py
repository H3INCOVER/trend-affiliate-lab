import random

OPENERS = [
    "最近、",
    "なんか",
    "じわじわ",
    "気づけば",
    "ここ最近、",
    "前より",
    "以前より",
    "今年入って",
    "意外と",
    "ここに来て",
    "ちょっと面白いのが",
    "“まず調べる”前提になってきた？",
    "前はここまでじゃなかったけど、",
    "検索の空気変わってきた？",
]

CHANGES = [
    "検索増えてる？",
    "見る機会増えた",
    "気にする人増えてるっぽい",
    "普通になってきた感じある",
    "調べる人かなり増えた印象",
    "以前より存在感ある",
    "じわじわ広がってる？",
    "ちゃんと定着してきた？",
    "最近かなり見る",
    "知らないと逆に不安になる段階かも",
    "“とりあえず確認”されてる感ある",
]

ENDINGS = [
    "なんか時代感じる。",
    "ちょっと面白い。",
    "ここ数年で空気変わった気がする。",
    "前はここまでじゃなかった。",
    "“知ってる前提”になってきた？",
    "わりとリアル。",
    "これ地味に大きい変化かも。",
    "気づけば普通になってる。",
    "なんとなく今っぽい。",
    "時代の流れ感じる。",
]

QUESTION_PATTERNS = [
    "“{keyword}”検索、増えてる？",
    "{keyword}、気にする人増えてるっぽい",
    "{keyword}、最近かなり見る",
    "{keyword}、“確認しておきたい”人増えてる？",
    "{keyword}、知らないと不安になる段階かも",
]

STATEMENT_PATTERNS = [
    "{keyword}が、じわじわ普通になってきた感じある",
    "{keyword}、“知ってる前提”になってきた？",
    "{keyword}、前より存在感ある",
    "{keyword}、最近ちゃんと定着してきた印象",
]

def generate_title(keyword):
    pattern_type = random.choice(["question", "statement"])

    if pattern_type == "question":
        pattern = random.choice(QUESTION_PATTERNS)
    else:
        pattern = random.choice(STATEMENT_PATTERNS)

    opener = random.choice(OPENERS)
    ending = random.choice(ENDINGS)

    title = f"{opener}{pattern.format(keyword=keyword)}。{ending}"

    return title