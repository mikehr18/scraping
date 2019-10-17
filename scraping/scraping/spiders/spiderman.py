# -*- coding: utf-8 -*-
import psycopg2
import scrapy
from scraping.items import ScrapingItem

class SpidermanSpider(scrapy.Spider):
    name = 'spiderman'
    allowed_domains = ['blogspot.com']
    start_urls = ['http://likcos.blogspot.com/']

    # def parse(self, response):
    #     item= ScrapingItem()
    #     item['titulos']=response.css('a').xpath('@href').extract()
    #     item['titulos2']=response.css('a').xpath('@href').extract()
    #     return item

#scrapy crawl ejemplo1 -o salida5.csv 

    def parse(self, response):
        item = ScrapingItem()
        table_rows = response.css('a')
        for x in table_rows:
            item['links'] = x.css('a').xpath('@href').extract_first()
            yield item