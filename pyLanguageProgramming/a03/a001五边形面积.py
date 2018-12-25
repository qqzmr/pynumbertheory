# -*-coding:utf-8-*-

import math

if __name__ == "__main__":
    r = 5.5  # 中心到五边的距离
    area = 5 * r * r * math.sin(360/5) / 2.0  # 5absinC/2
    print("面积是:", area)

