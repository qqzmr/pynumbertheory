import  scrapy
#from  scrapy import cmdline
#pycharm执行风格
#cmdline.execute(["scrapy","crawl","ctospider","-o","51cto.xml"])



#进程启动爬虫，可以并发执行多个
from scrapy.crawler import CrawlerProcess  #进程启动爬虫
from scrapy.utils.project import get_project_settings #抓取配置
from  cyzonespider.spiders.chuangyezhe import ChuangyezheSpider
settings = get_project_settings()  #抓取配置
process = CrawlerProcess(settings=settings)#进程启动爬虫
process.crawl(ChuangyezheSpider)
#process.crawl(CtospiderSpider1)   可以并发执行多个
# process.crawl(CtospiderSpider2)
process.start()


