# -*-coding:utf-8-*-


def getPentagonalNumber(n):
    return n * (3 * n - 1) // 2


if __name__ == "__main__":
    print(getPentagonalNumber(3))
