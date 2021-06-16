def process(serial, battery, paralel):
    sample = '''
    ==== サンプル ====
    LED点灯・星付き・赤 : LSR
    星付き・赤青 : SRB
    LED点灯・白 : L
    LED星なし・赤白 : R
    LED星なし・白 : -
    '''

    print(sample)

    print('クリア時は [!] を入力')

    while True:
        print("---------------------------------------------------------------------")
        i = input('ワイヤの情報を入力 (サンプルを参照) > ')

        if i == '!':
            return True
        else:
            if 'L' in i and 'S' in i:
                if 'R' in i and 'B' in i:
                    print('切らない')
                elif 'B' in i:
                    P(paralel)
                else:
                    B(battery)
            elif 'L' in i:
                if 'R' in i and 'B' in i:
                    S(serial)
                elif 'R' in i:
                    B(battery)
                elif 'B' in i:
                    P(paralel)
                else:
                    print('切らない')
            elif 'S' in i:
                if 'R' in i and 'B' in i:
                    P(paralel)
                elif 'B' in i:
                    print('切らない')
                else:
                    print('切る')
            else:
                if not 'R' in i and not 'B' in i:
                    print('切る')
                else:
                    S(serial)


def S(serial):
    if serial % 2:
        print('切らない')
    else:
        print('切る')
    return


def B(battery):
    if battery > 1:
        print('切る')
    else:
        print('切らない')
    return


def P(paralel):
    if paralel:
        print('切る')
    else:
        print('切らない')
    return
