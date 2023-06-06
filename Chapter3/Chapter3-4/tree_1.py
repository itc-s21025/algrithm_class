LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, "Iカレ"],
    [3, 4, "プログラム"],
    [5, 6, "就活"],
    [None, None, "java"],
    [6, 7, "python"],
    [None, None, "コミュニケーション"],
    [None, None, "data試験"],
    [None, None, "実習Algorithm"]
]
MAX = len(node)

print("指定のノードを調べます")
print("何も入力せずにEnterを押すと終了します")

while True:
    s = input("number=")
    if s == "":
        break
    n = int(s)
    if 0 <= n and n < MAX:
        print("node{}の値は{}".format(n, node[n][DATA]))
        le = node[n][LEFT]
        if le != None:
            print("左の子は" + str(node[le][DATA]))
        else:
            print("左の子は存在しません")
        ri = node[n][RIGHT]
        if ri != None:
            print("右の子は" + str(node[ri][DATA]))
        else:
            print("右の子は存在しません")
    else:
        print("0から" + str(MAX-1)+"の範囲で入力してください")

