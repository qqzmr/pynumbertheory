# -*- coding: utf-8 -*-
import scrapy


class RongziSpider(scrapy.Spider):
    name = 'rongzi'
    allowed_domains = ['cyzone.cn']
    start_urls = ['http://cyzone.cn/']

    def parse(self, response):
        pass
