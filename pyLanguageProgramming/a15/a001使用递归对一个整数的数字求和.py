# -*-coding:utf-8-*-


def sumDigits(n):
    if n == 0:
        return 0
    return n % 10 + sumDigits(n // 10)


if __name__ == "__main__":
    num = eval(input("请输入整数："))
    print(sumDigits(num))
