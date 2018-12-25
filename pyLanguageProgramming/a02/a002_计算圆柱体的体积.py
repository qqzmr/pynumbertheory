# -*- coding:utf-8-*-

import math

if __name__ == "__main__":
    r = eval(input("圆柱的半径："))
    h = eval(input("圆柱的高："))
    area = math.pi * r * r
    volme = area * h
    print("圆柱的底面积是：", area)
    print("圆柱的体积是：", volme)

