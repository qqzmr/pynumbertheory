# -*-coding:utf-8-*-

if __name__ == "__main__":
    num = 0
    sum = 0
    count1 = 0
    count2 = 0
    while True:
        num = eval(input("请输入整数："))
        if num == 0:
            break
        if num > 0:
            count1 += 1
        else:
            count2 += 1
        sum += num
    print("正整数的个数：", count1)
    print("负整数的个数：", count2)
    print("总和是：", sum)
    counttotal = count1 + count2
    if counttotal > 0:
        avg = 1.0 * sum / counttotal
        print("平均值是：", avg)
    else:
        print("平均值是：", 0)
