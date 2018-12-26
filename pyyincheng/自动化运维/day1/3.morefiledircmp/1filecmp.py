# -*-coding:utf-8-*-
import filecmp
#对比文件相等或者不等，相等True.不等Flase
print(filecmp.cmp("./cyzonespider1/1.txt","./cyzonespider2/1.txt"))
print(filecmp.cmp("./cyzonespider1/1.txt","./cyzonespider2/starts.py"))



