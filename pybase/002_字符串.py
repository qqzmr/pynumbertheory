import string

if __name__ == "__main__":
    print("----1.去掉空格及特殊字符")
    a1 = "   ,dfadfadfa, "
    b1 = a1.strip().lstrip().rstrip(',')
    print(type(b1), b1)
    print("----2.复制字符串")
    a2 = "   ,dfadfadfa, "
    b2 = a2
    print(type(b2), b2)
    print("----3.连接字符串")
    a3 = "   ,dfadfadfa, "
    b3 = a3 + str(123456789)
    print(type(b3), b3)
    print("----4.查找字符串")
    a4 = "dfadfadfa"
    b4 = a4.index("fa")
    print(type(b4), b4)
    b4 = a4.rindex("fa")
    print(type(b4), b4)
    print("----5.比较字符串")
    a5 = "dfadfadfa"
    a52 = "dfadfada"
    # >,<,>=,<=,==,!=
    b5 = a5 < a52  # cmp函数python3中被移除了
    print(type(b5), b5)
    print("----6.字符串长度（中文）")
    a6 = "哈dfadf"
    b6 = len(a6)
    print(type(b6), b6)
    print("----7.字符串大写")
    a7 = "哈dfadf"
    b7 = a7.upper()
    print(type(b7), b7)
    print("----8.字符串小写")
    a8 = "哈HHOdfasd"
    b8 = a8.lower()
    print(type(b8), b8)
    print("----9.字符串首字母大写")
    a9 = "dfasd wes dfasdfa"
    b9 = a9.capitalize()
    print(type(b9), b9)
    print("----10.字符串单词首字母大写")
    a10 = "hello world"
    b10 = string.capwords(a10)
    print(type(b10), b10)
    b10 = a10.title()
    print(type(b10), b10)
    print("----11.字符串大写变小写，小写变大写")
    a11 = "heLlo worlD"
    b11 = a11.swapcase()
    print(type(b11), b11)
    print("----12.字符串翻转")
    a12 = "heLlo worlD"
    b12 = a12[::-1]
    print(type(b12), b12)
    print("----13.字符串分割")
    a13 = "heLlo,worlD"
    b13 = a13.split(',')
    print(type(b13), b13)
    print("----14.字符串序列连接")
    a14 = ['hello', 'world']  # a14只能是字符串列表
    b14 = "-".join(a14)
    print(type(b14), b14)
    print("----15.字符串内查找")
    a15 = "today is a fine day"
    b15 = a15.find("is")
    print(type(b15), b15)
    print("----16.字符串替换")
    a16 = "today is a fine day"
    b16 = a16.replace("is", "not")
    print(type(b16), b16)
    print("----17.判断字符串组成")
    # isdigit ———— 检测字符串时候只由数字组成
    # isalnum ———— 检测字符串是否只由数字和字母组成
    # isalpha ———— 检测字符串是否只由字母组成
    # islower ———— 检测字符串是否只含有小写字母
    # isupper ———— 检测字符串是否只含有大写字母
    # isspace ———— 检测字符串是否只含有空格
    # istitle ———— 检测字符串是否是标题（每个单词首字母大写）
    a17 = "哈哈today is a fine day"
    b17 = a17.islower()
    print(type(b17), b17)
