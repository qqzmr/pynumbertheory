# -*-coding:utf-8-*-

import math

if __name__ == "__main__":
    a = eval(input("请输入a："))
    b = eval(input("请输入b："))
    c = eval(input("请输入c："))
    if a == 0:
        if b == 0:
            print("x = ", (-c * 1.0 / b))
        else:
            if c == 0:
                print("x为任意值")
            else:
                print("无解")
    else:
        discriminant = b * b - 4 * a * c
        if discriminant >= 0:
            discriminant = math.sqrt(discriminant)
            print("x1 = ", ((-b + discriminant) / (2 * a)))
            print("x2 = ", ((-b - discriminant) / (2 * a)))
        else:
            print("无实数解")


