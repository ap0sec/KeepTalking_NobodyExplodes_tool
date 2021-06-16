def process():
    s = [
        "about",
        "after",
        "again",
        "below",
        "could",
        "every",
        "first",
        "found",
        "great",
        "house",
        "large",
        "learn",
        "never",
        "other",
        "place",
        "plant",
        "point",
        "right",
        "small",
        "sound",
        "spell",
        "still",
        "study",
        "their",
        "there",
        "these",
        "thing",
        "three",
        "water",
        "where",
        "which",
        "world",
        "would",
        "write",
    ]
    print("==== 中断する場合は[!]と入力 ====")
    for t in [1, 5, 3, 2, 4]:
        print(s)
        i = input(f'{t}文字目の候補を列挙 (小文字) > ')
        if i == '!':
            print("---------------------------------------------------------------------")
            print(s)
            return False
        s = [ss for ss in s if ss[t-1] in i]
        if len(s) < 2:
            if s:
                print("---------------------------------------------------------------------")
                print(f"result: {s[0]}")
                return True
            else:
                print("候補が見つかりませんでした。入力を確認してください。")
                return False
