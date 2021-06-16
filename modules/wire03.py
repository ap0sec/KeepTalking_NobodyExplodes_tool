def process():

    r = 0
    b = 0
    k = 0

    R = [
        'C',
        'B',
        'A',
        'AC',
        'B',
        'AC',
        'ABC',
        'AB',
        'B'
    ]

    B = [
        'B',
        'AC',
        'B',
        'A',
        'B',
        'BC',
        'C',
        'AC',
        'A'
    ]

    K = [
        'ABC',
        'AC',
        'B',
        'AC',
        'B',
        'BC',
        'AB',
        'C',
        'C',
    ]

    print('クリア時は [!] を入力')

    while True:
        print("---------------------------------------------------------------------")

        i = str(input('ワイヤの色 (赤: r, 青: b, 黒: k) > '))

        if i == '!':
            return True

        if i == 'r':
            print(R[r])
            r += 1
        if i == 'b':
            print(B[b])
            b += 1
        if i == 'k':
            print(K[k])
            k += 1
