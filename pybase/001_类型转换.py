# -*-coding:utf-8-*-

if __name__ == "__main__":
    print("----1.字符串转化成整型")
    a1 = "80"
    b1 = int(a1, 10)
    print(type(b1), b1)
    print("----2.字符串转换成浮点型")
    a2 = "80"
    b2 = float(a1)
    print(type(b2), b2)
    print("----3.字符串转换成复数")
    a3 = "80+2j"
    b3 = complex(a3)
    print(type(b3), b3)
    print("----4.数字转换成字符串")
    a4 = 127
    b4 = str(a4)
    print(type(b4), b4)
    print("----5. 返回一个对象的String格式")
    a5 = 127
    b5 = repr(a5)
    print(type(b5), b5)
    print("----6. 执行一个字符串表达式，返回计算的结果")
    b6 = eval("12+(23*2)")
    print(type(b6), b6)
    print("----7. 返回元组")
    b7 = tuple([1, 2, 3, 4])
    print(type(b7), b7)
    print("----8. 返回列表")
    b8 = list((1, 2, 3, 4))
    print(type(b8), b8)
    print("----9. 返回集合")
    b9 = set((1, 2, 3, 4))
    print(type(b9), b9)
    print("----10. 返回不可变集合")
    b10 = frozenset((1, 2, 3, 4))
    print(type(b10), b10)
    print("----11. 返回值是当前整数对应的ascii字符")
    b11 = chr(123)
    print(type(b11), b11)
    print("----12.  返回对应的 ASCII 数值，或者 Unicode 数值")
    b12 = ord('张')
    print(type(b12), b12)
    print("----13.  把一个整数转换为十六进制字符串")
    b13 = hex(12345)
    print(type(b13), b13)
    print("----14.  把一个整数转换为八进制字符串")
    b14 = oct(12345)
    print(type(b14), b14)
