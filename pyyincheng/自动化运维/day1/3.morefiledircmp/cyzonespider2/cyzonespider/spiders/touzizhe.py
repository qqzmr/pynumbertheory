# -*- coding: utf-8 -*-
import scrapy


class TouzizheSpider(scrapy.Spider):
    name = 'touzizhe'
    allowed_domains = ['cyzone.cn']
    start_urls = ['http://cyzone.cn/']

    def parse(self, response):
        pass
