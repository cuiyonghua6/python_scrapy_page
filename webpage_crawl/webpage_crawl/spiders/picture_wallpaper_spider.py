# coding=utf-8
import scrapy


class Spdier_pictures(scrapy.spiders.Spider):
    """爬取码农之家网站 分类下的python图书"""
    name = "book_xz577"  # 定义爬虫名，要和settings中的BOT_NAME属性对应的值一致

    # allowed_domains = []  # 搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页

    start_urls = ["https://www.xz577.com/e/python/"]  # 开始爬取的地址

    # 该函数名不能改变，因为Scrapy源码中默认callback函数的函数名就是parse
    def parse(self, response):
        sub_selector = response.xpath('//div[@class="f-fl m-leftbox"]')
        for sub in sub_selector:
            book_title = sub.xpath('./p/strong/a/text()').extract_first()
            book_publish = sub.xpath('./p/i[1]/text()').extract_first()
            book_author = sub.xpath('./p/i[2]/text()').extract_first()
            book_category = sub.xpath('./span/i[2]/text()').extract_first()
            book_update_time = sub.xpath('./span/i[3]/text()').extract_first()

            print(book_title, book_publish, book_author, book_category, book_update_time)

