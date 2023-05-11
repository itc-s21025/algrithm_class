def fun1(n):
    two = 2 ** n
    three = 3 ** n

    result = three - two
    return result
n = int(input())
print(fun1(n))