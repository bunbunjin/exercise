
def main():
    input1 = input().split() #range
    input2 = input().split() #個数
    input3 = input().split() #割る数
    num = []
    ras = list(range(int(min(input1)), int(max(input1))))
    for i in ras:
        for x in input3:
            am = i % int(x)
            if am == 0:
                num.append(am)
            else:
                pass
    print(len(ras))
    print(len(num))
    return len(ras) - len(num)


main()