MAX = 5
stack = [0]*MAX
sp = 0

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp = sp + 1
        print("データ", d, "を追加しました")
    else:

        print("これ以上データを入れられません")

def pop():
    global sp
    if sp > 0:
        sp = sp - 1
        return stack[sp]
    else:
        print("取り出すデータが存在しません")
        return None

def main():
    global sp
    for i in range(2):
        push(i)
    pop()
    for i in range(2, 5):
        push(i)
main()

