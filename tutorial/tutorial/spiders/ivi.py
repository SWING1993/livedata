# -*- coding: utf-8 -*-
import scrapy

class IviItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()

class IviSpider(scrapy.Spider):
    name = "ivi"
    allowed_domains = ["ivi.bupt.edu.cn"]
    start_urls = [
        "http://ivi.bupt.edu.cn/",
    ]

    def parse(self, response):
        host = "http://ivi.bupt.edu.cn"
        for sel in response.xpath('//div[@class="2u -2u"]'):
            item = IviItem()
            item["title"] = sel.xpath('p/text()').extract()[0]
            item["href"] = host + sel.xpath('a[last()]/@href').extract()[0]
            yield item

        for sel in response.xpath('//div[@class="2u"]'):
            item = IviItem()
            item["title"] = sel.xpath('p/text()').extract()[0]
            item["href"] = host + sel.xpath('a[last()]/@href').extract()[0]
            yield item
