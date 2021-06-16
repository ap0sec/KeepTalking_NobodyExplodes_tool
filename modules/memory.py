def process():

    step = 1
    memory = []
    while step < 6:

        d = int(input('ディスプレイの数字 (最初からやる場合は[0])> '))

        if d == 0:
            step = 1
            memory = []
            continue

        if step == 1:
            if d == 3:
                print('3番目')
                p = 3
            elif d == 4:
                print('4番目')
                p = 4
            else:
                print('2番目')
                p = 2
            l = int(input('押したボタンのラベル > '))
            memory.append([p, l])
        elif step == 2:
            if d == 1:
                print('4のラベル')
                l = 4
                p = int(input('押したボタンの位置 > '))
            if d == 3:
                print('1番目')
                p = 1
                l = int(input('押したボタンのラベル > '))
            else:
                print(f'{memory[0][0]}番目')
                p = memory[0][0]
                l = int(input('押したボタンのラベル > '))
            memory.append([p, l])
        elif step == 3:
            if d == 1:
                print(f'{memory[1][1]}のラベル')
                l = memory[1][1]
                p = int(input('押したボタンの位置 > '))
            elif d == 2:
                print(f'{memory[0][1]}のラベル')
                l = memory[0][1]
                p = int(input('押したボタンの位置 > '))
            elif d == 3:
                print('3番目')
                p = 3
                l = int(input('押したボタンのラベル > '))
            else:
                print('4のラベル')
                l = 4
                p = int(input('押したボタンの位置 > '))
            memory.append([p, l])
        elif step == 4:
            if d == 1:
                print(f'{memory[0][0]}番目')
                p = memory[0][0]
            elif d == 2:
                print('1番目')
                p = 1
            else:
                print(f'{memory[1][0]}番目')
                p = memory[1][0]

            l = int(input('押したボタンのラベル > '))
            memory.append([p, l])
        elif step == 5:
            if d == 1:
                print(f'{memory[0][1]}のラベル')
            elif d == 2:
                print(f'{memory[1][1]}のラベル')
            elif d == 3:
                print(f'{memory[3][1]}のラベル')
            else:
                print(f'{memory[2][1]}のラベル')
        step += 1
    return
