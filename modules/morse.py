def process():

    hz = {
        "shell": 3.505,
        "halls": 3.515,
        "slick": 3.522,
        "trick": 3.532,
        "boxes": 3.535,
        "leaks": 3.542,
        "strobe": 3.545,
        "bistro": 3.552,
        "flick": 3.555,
        "bombs": 3.565,
        "break": 3.572,
        "brick": 3.575,
        "steak": 3.582,
        "sting": 3.592,
        "vector": 3.595,
        "beats": 3.600
    }

    morse = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z"
    }

    s = [i for i in hz.keys()]

    print("==== 中断して結果を確認する場合は[!]と入力 ====")
    while len(s) > 1:
        print(s)
        input_morse = str(input('読み取った信号を入力 (トン: . / ツー: -) > '))
        if input_morse == '!':
            break
        else:
            target = morse.get(input_morse)
            if target:
                print(target)
                s = [i for i in s if target in i]
            else:
                print("Wrong Morse")

    print("---------------------------------------------------------------------")
    if s:

        for ss in s:
            print(f"result: {ss}, {hz.get(ss)}MHz")
        return True
    else:
        print("候補が見つかりませんでした。入力を確認してください。")
        return False
