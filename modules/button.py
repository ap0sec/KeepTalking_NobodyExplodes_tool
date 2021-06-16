def process(battery, car, frk):
    color = str(input('ボタンの色 (赤: r, 青: b, 黄: y, 白: w) > '))
    text = int(input('テキスト (中止: 0, 起爆: 1, 長押し: 2, その他: 3) > '))

    val = ""

    if color == 'b' and text == 0:
        val = timing()
    elif battery > 1 and text == 1:
        val = '押してすぐ離す'
    elif color == 'w' and car:
        val = timing()
    elif battery > 2 and frk:
        val = '押してすぐ離す'
    elif color == 'y':
        val = timing()
    elif color == 'r' and text == 2:
        val = '押してすぐ離す'
    else:
        val = timing()

    print("---------------------------------------------------------------------")
    print(val)

    return True


def timing():
    indicator = str(input('インジケーターの色 (青: b, 黄: y, その他: x) > '))

    if indicator == 'b':
        return '長押し -> タイマー4'
    elif indicator == 'y':
        return '長押し -> タイマー5'
    else:
        return '長押し -> タイマー1'
