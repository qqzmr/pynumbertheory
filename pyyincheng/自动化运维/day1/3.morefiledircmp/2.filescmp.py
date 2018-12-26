import filecmp
import os
#cmpfiles可以对比文件，不可以对比文件夹，第一个列表相等，第二个列表不等
print(filecmp.cmpfiles("./cyzonespider1","./cyzonespider2",
      os.listdir("./cyzonespider1")))
print(filecmp.cmpfiles("./cyzonespider1","./cyzonespider2",
                       ['1.txt', 'scrapy.cfg', 'starts.py']))

