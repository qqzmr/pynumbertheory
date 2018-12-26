#coding:utf-8
import difflib
string1="""
text1_lines=string1.splitlines() #1
text2_lines=string2.splitlines()
d=difflib.HtmlDiff()
print(d.make_file(text1_lines,text2_lines))
file=open("diff.html","w")
file.write(d.make_file(text1_lines,text2_lines))
file.close()
"""
string2="""
text1_lines=string1.splitlines() #2
text2_lines=string2.splitlines()
d=difflib.HtmlDiff()
print(d.make_file(text1_lines,text2_lines))
file=open("diff.html","w")
file.write(d.make_file(text1_lines,text2_lines))
file.close()
"""
text1_lines=string1.splitlines() #根据换行切割
text2_lines=string2.splitlines()
d=difflib.HtmlDiff()
#print(d.make_file(text1_lines,text2_lines))
file=open("diff.html","w")
file.write(d.make_file(text1_lines,text2_lines))
file.close()

filetable=open("difft.html","w")
print(d.make_table(text2_lines,text1_lines))
filetable.write(d.make_table(text2_lines,text1_lines))
filetable.close()