# -*- coding: utf-8 -*-
import scrapy
from cyzonespider import items
import lxml.etree
class ChuangyezheSpider(scrapy.Spider):
    name = 'chuangyezhe'
    allowed_domains = ['cyzone.cn']
    #start_url=["http://www.cyzone.cn/vpeople/list-0-1/"]
    def start_requests(self):
        myurl="http://www.cyzone.cn/vpeople/list-0-"
        for i  in range(1,1019):
            yield scrapy.Request(myurl+str(i)+r"/",callback=self.parse)

    def parse(self, response):
        content = response.body
        mytree = lxml.etree.HTML(content)
        linelist = mytree.xpath("//tr[@class=\"ltp-plate\"]")

        for line in linelist:
            myitem = items.ChuangyezhespiderItem()
            if  len(line.xpath("./td[@class=\"people-name\"]/a/text()"))!=0:
                myitem["name"]=line.xpath("./td[@class=\"people-name\"]/a/text()")[0]
            else:
                myitem["name"] =""
            if  len(line.xpath(".//td[3]/a/text()"))!=0:
                myitem["company"] =line.xpath(".//td[3]/a/text()")[0]
            else:
                myitem["company"] =""
            if   len(line.xpath(".//td[4]/text()"))!=0:
                myitem["workname"] =line.xpath(".//td[4]/text()")[0]
            else:
                myitem["workname"] =""
            if len(line.xpath(".//td[5]/a/text()"))!=0:
                myitem["about"] =line.xpath(".//td[5]/a/text()")[0]
            else:
                myitem["about"] =""
            yield myitem




