LEFT = 0
RIGHT = 1
count = 0
DATA = 2
x = []
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

def function1(node):
    global count, x
    if count == 8:
        return print(x)
    x.append(node[count][2])
    count += 1
    function1(node)

function1(node)






