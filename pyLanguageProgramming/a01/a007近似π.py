# -*-coding:utf-8-*-

if __name__ == "__main__":
    n = 9
    sum = 0
    flag = True
    for i in range(90000):
        if flag:
            sum += 1 / (2 * i + 1)
        else:
            sum -= 1 / (2 * i + 1)
        flag = not flag
    sum *= 4
    print(sum)



