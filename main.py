import modules.wire01
import modules.button
import modules.simon
import modules.memory
import modules.morse
import modules.wire02
import modules.wire03
import modules.password


def main():

    menu = '''
    1:  ワイヤ
    2:  ボタン
    3:  麻雀
    4:  Windows
    5:  文字
    6:  記憶(数字)
    7:  モールス
    8:  複雑ワイヤ
    9:  記憶(ワイヤ)
    10: 迷路
    11: パスワード
    20: ダイヤル
    99: クリア(終了)
    '''

    battery = int(input('バッテリーは何本ありますか？ (int) > '))
    serial = int(input('シリアルナンバーの末尾は？ (int) > '))
    serial_wc = bool(int(input('シリアルナンバーに母音は含まれますか？ (True: 1/False: 0) > ')))
    paralel = bool(int(input('パラレルポートはありますか？ (True: 1/False: 0) > ')))
    car = bool(int(input('点灯したCARはありますか？ (True: 1/False: 0) > ')))
    frk = bool(int(input('点灯したFRKはありますか？ (True: 1/False: 0) > ')))

    while True:
        print(menu)

        i = int(input('> '))

        if i == 1:
            modules.wire01.process(serial)
        elif i == 2:
            modules.button.process(battery, car, frk)
        elif i == 3:
            print("PDF見て！！")
        elif i == 4:
            modules.simon.process(serial_wc)
        elif i == 5:
            print("TBD")
        elif i == 6:
            modules.memory.process()
        elif i == 7:
            modules.morse.process()
        elif i == 8:
            modules.wire02.process(serial, battery, paralel)
        elif i == 9:
            modules.wire03.process()
        elif i == 10:
            print("TBD")
        elif i == 11:
            modules.password.process()
        elif i == 20:
            print("TBD")
        elif i == 99:
            print("Bye!")
            return True
        else:
            print("Wrong function")

        print()
        print("=====================================================================")


if __name__ == "__main__":
    main()
