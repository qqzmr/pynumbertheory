#coding:utf-8
import difflib
string1="""
你酷，你喝水在水库2，
睡觉在古墓，嘴里流瀑布，
四肢像枕木，你当你是貂禅吕布，
其实你是南极土著
"""
string2="""
你酷，你喝水在水库1，
睡觉在古墓，嘴里流瀑布，
四肢像枕木，你当你是貂禅吕布，
其实你是南极土著
"""
text1_lines=string1.splitlines() #根据换行切割
text2_lines=string2.splitlines()
d=difflib.Differ()
diff=d.compare(text1_lines,text2_lines) #快速对比差异
#print(list(diff))
print("\n".join(list(diff)))

