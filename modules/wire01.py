def process(s: int):
    w = str(input('ワイヤの色を上から順に入力 (赤: r, 青: b, 黄: y, 黒: k, 白: w) > '))
    val = -1

    if len(w) == 3:
        if not 'r' in w:
            val = 2
        elif w[-1] == "w":
            val = 3
        elif w.count("b") > 1:
            val = 3 - w[::-1].index("b")
        else:
            val = 3
    if len(w) == 4:
        if w.count("r") > 1 and s % 2:
            val = 4 - w[::-1].index("r")
        elif w[-1] == "y" and not "r" in w:
            val = 1
        elif w.count("b") == 1:
            val = 1
        elif w.count("y") > 1:
            val = 4
        else:
            val = 2
    if len(w) == 5:
        if w[-1] == "b" and s % 2:
            val = 4
        elif w.count("r") == 1 and w.count("y") > 1:
            val = 1
        elif not "k" in w:
            val = 2
        else:
            val = 1
    if len(w) == 6:
        if not "y" in w and s % 2:
            val = 3
        elif w.count("y") == 1 and w.count("w") > 1:
            val = 4
        elif not "r" in w:
            val = 6
        else:
            val = 4

    print("---------------------------------------------------------------------")
    print(f"please cut {val}")

    return True
