# -*-coding:utf-8-*-

if __name__ == "__main__":
    print("a\ta^2\ta^3")
    a = 1
    while True:
        print(a, end="")
        print("\t", end="")
        print(a ** 2, end="")
        print("\t", end="")
        print(a ** 3)
        a += 1
        if a >= 5:
            break
