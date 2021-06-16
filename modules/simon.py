def process(serial_wc):

    c = int(input('現在のミス回数を入力 (int) > '))

    memory = []

    while True:
        i = str(input('新しく点灯したものを入力 (赤: r, 青: b, 黄: y, 緑: g, クリア時: c, 間違えた場合: w) > '))

        if i == 'c':
            return True
        elif i == 'w':
            c += 1
            memory = []
        elif not i in ['r', 'g', 'b', 'y']:
            print('Wrong Input')
            continue
        elif serial_wc:
            if c == 0:
                if i == 'r':
                    memory.append('b')
                elif i == 'b':
                    memory.append('r')
                elif i == 'y':
                    memory.append('g')
                else:
                    memory.append('y')
            elif c == 1:
                if i == 'r':
                    memory.append('y')
                elif i == 'b':
                    memory.append('g')
                elif i == 'y':
                    memory.append('r')
                else:
                    memory.append('b')
            elif c == 2:
                if i == 'r':
                    memory.append('g')
                elif i == 'b':
                    memory.append('r')
                elif i == 'y':
                    memory.append('b')
                else:
                    memory.append('y')
        else:
            if c == 0:
                if i == 'r':
                    memory.append('b')
                elif i == 'b':
                    memory.append('y')
                elif i == 'y':
                    memory.append('r')
                else:
                    memory.append('g')
            elif c == 1:
                if i == 'r':
                    memory.append('r')
                elif i == 'b':
                    memory.append('b')
                elif i == 'y':
                    memory.append('g')
                else:
                    memory.append('y')
            elif c == 2:
                if i == 'r':
                    memory.append('y')
                elif i == 'b':
                    memory.append('g')
                elif i == 'y':
                    memory.append('r')
                else:
                    memory.append('b')
        print("---------------------------------------------------------------------")
        print(memory)

    return True
