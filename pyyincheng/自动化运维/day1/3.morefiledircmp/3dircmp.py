#coding:utf-8
import filecmp

dirdiff=filecmp.dircmp("./cyzonespider1","./cyzonespider2")
print(dirdiff.report())#对比的日志.当前目录
print("-----------------")
#print(dirdiff.report_full_closure())#所有目录
print("-----------------")
#print(dirdiff.report_partial_closure())#当前目录与第一级别目录
print(dirdiff.left_list)#对比的左边目录
print(dirdiff.right_list)#对比的右边目录
print(dirdiff.common)#相同的文件或者目录
print(dirdiff.left_only)#左边独有
print(dirdiff.right_only)#右边独有
print(dirdiff.common_files)#共有的文件相同
print(dirdiff.common_dirs)#共有的相同文件夹
print(dirdiff.common_funny)#两边都存在，但是无法对比，权限
print(dirdiff.same_files)#相同文件
print(dirdiff.diff_files)#不同文件
print(dirdiff.funny_files)#都存在但无法对比的文件
