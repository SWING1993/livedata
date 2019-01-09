# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class Douyu(scrapy.Item):
    title = scrapy.Field()
    img = scrapy.Field()
    url = scrapy.Field()
    directory = scrapy.Field()

    name = scrapy.Field()
    num = scrapy.Field()
    c2url = scrapy.Field()
    tid = scrapy.Field()
    rid = scrapy.Field()
    sid = scrapy.Field()
    bid = scrapy.Field()

class DouyuDirectorySpider(scrapy.Spider):
    name = "douyu.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    allowed_domains = ["www.douyu.com"]
    start_urls = [
        "https://www.douyu.com/directory",
    ]

    def parse(self, response):
        host = "https://www.douyu.com"

        # 爬取分类
        for sel in response.xpath('//li[@class="unit "]'):
            item = Douyu()
            item['img']= sel.xpath('a/img/@data-original').extract()[0]
            item['title'] = sel.xpath('a/p/text()').extract()[0]
            item['url'] = host + sel.xpath('a/@href').extract()[0]
            yield Request(item['url'])

        # 爬取分类下的房间信息
        for sel in response.xpath('//a[@class="play-list-link"]'):
            item = Douyu()
            item['url'] = host + sel.xpath('@href').extract()[0]
            item['title'] = sel.xpath('@title').extract()[0]
            item['c2url'] = sel.xpath('@data-c2url').extract()[0]
            item['tid'] = sel.xpath('@data-tid').extract()[0]
            item['rid'] = sel.xpath('@data-rid').extract()[0]
            item['sid'] = sel.xpath('@data-sid').extract()[0]
            item['bid'] = sel.xpath('@data-bid').extract()[0]
            item['img'] = sel.xpath('span/img/@data-original').extract()[0]
            item['name'] = sel.xpath('div/p/span[@class="dy-name ellipsis fl"]/text()').extract()[0]
            item['num'] = sel.xpath('div/p/span[@class="dy-num fr"]/text()').extract()[0]
            # print("房间item:", item)
            yield item


 # 保存item到json
 # scrapy crawl douyu.com -o douyu.json

 # 将 response 存到本地
 # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)




