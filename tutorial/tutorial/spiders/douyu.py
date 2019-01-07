# -*- coding: utf-8 -*-
import scrapy

class DouyuDirectory(scrapy.Item):
    title = scrapy.Field()
    img = scrapy.Field()
    href = scrapy.Field()

class DouyuDirectorySpider(scrapy.Spider):
    name = "douyu_directory"
    allowed_domains = ["www.douyu.com"]
    start_urls = [
        "https://www.douyu.com/directory",
    ]

    def parse(self, response):
        for sel in response.xpath('//li[@class="unit "]'):
            item = DouyuDirectory()
            img = sel.xpath('a/img/@data-original').extract()[0]
            item['img'] = img
            title = sel.xpath('a/p/text()').extract()[0]
            item['title'] = title
            href = sel.xpath('a/@href').extract()[0]
            item['href'] = href
            print(href)
            yield item









