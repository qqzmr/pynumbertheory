# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CyzonespiderPipeline(object):

    def __init__(self):
        self.file = open("1.txt", "w")

    def __del__(self):
        self.file.close()

    def process_item(self, item, spider):
        if  spider.name=="chuangyezhe":
            print(item)
            self.file.write(str(item) + "\r\n")
            self.file.flush()
            return item