Hinata46 = ["うしお", "かげやま", "かとう", "さいとう", "ささき", "ささき", "たかせ", "たかもと", "ひがしむら", "かねむら", "こさか", "かわた", "とみた", "にぶ", "はまぎし", "まつだ", "かみむら", "たかはし", "もりもと", "やまぐち"]

print(Hinata46, "元のデータ")

for i in range(0, 9):
    tmp = i
    for j in range(i+1, 10):
        if Hinata46[j] < Hinata46[tmp]:
            tmp = j
    Hinata46[i], Hinata46[tmp] = Hinata46[tmp], Hinata46[i]

print(Hinata46, "ソート後のデータ")
