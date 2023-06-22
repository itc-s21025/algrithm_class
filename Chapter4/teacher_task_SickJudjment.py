# 　喜友名さんのコードを参考にかきました

LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, "38.5℃以上の発熱がある？"],
    [3, 4, "元気がある？"],
    [5, 6, "むねがひいひい？"],
    [None, None, "氷枕で病院"],
    [None, None, "様子をみる"],
    [None, None, "解熱剤で病院"],
    [None, None, "速攻で病院"],
]

result = 0


def sickjudjment(result=0):
    for i in range(2):
        s = input(f'{node[result][DATA]}(Y/n): ').lower()
        if s == 'y':
            result = node[result][RIGHT]
        elif s == 'n':
            result = node[result][LEFT]
        else:
            print("y or n で答えてください")
            return a()

    return node[result][DATA]


print(sickjudjment())
