MAX = 6
que = [0]*MAX
head = 0
tail = 0
count = 0
def enqueue(d):
    global tail
    global count
    time = 15
    nt = (tail+1)%MAX

    if nt == head:
        print("これ以上データを入れられません")
    else:
        que[tail] = d
        tail = nt
        count += 1
        a = time * count
        print("データ", d, "を追加しました。待ち時間", a, "です")



def dequeue():
    global head
    global count
    if head == tail:
        print("取り出すデータが存在しません")
        return None
    else:
        d = que[head]
        head = (head+1)%MAX
        count -= 1

        return d
def main():
    for i in range(3):
        enqueue(i)

    for i in range(2):
        d = dequeue()

        print("取り出したデータ", d)

    for i in range(1):
        enqueue(i)

main()

