# -*- coding: utf-8 -*-
import scrapy

class DmozSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["douyu.org"]
    start_urls = [
        "https://www.douyu.com/directory",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
