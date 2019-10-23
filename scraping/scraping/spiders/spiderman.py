# -*- coding: utf-8 -*-
import psycopg2
import scrapy
from scraping.items import ScrapingItem
import re

class SpidermanSpider(scrapy.Spider):
    name = 'spiderman'
    #allowed_domains = ['blogspot.com']
    #start_urls = ['http://likcos.blogspot.com/']
    def __init__(self, domain='', *args, **kwargs):
        super(SpidermanSpider, self).__init__(*args, **kwargs)
        self.start_urls = [domain]
    # def parse(self, response):
    #     item= ScrapingItem()
    #     item['titulos']=response.css('a').xpath('@href').extract()
    #     item['titulos2']=response.css('a').xpath('@href').extract()
    #     return item

#scrapy crawl ejemplo1 -o salida5.csv 

    def parse(self, response):
        item = ScrapingItem()
        table_rows = response.css('a')
        dominio=self.start_urls[0]
        my_sufixes = "php","htm","html","pdf","doc","docx","jsp","aspx", "#"
        if not dominio.endswith(my_sufixes) and not dominio.endswith("/"):
            ndominio = dominio + "/"
        else:    
            k = dominio.rfind("/")
            ndominio = dominio[:k+1]


        for x in table_rows:
            if not str(x.css('a').xpath('@href').extract_first()).startswith('http'):
                print(self.start_urls[0] + str(x.css('a').xpath('@href').extract_first()))
                item['links'] = ndominio + str(x.css('a').xpath('@href').extract_first())
            else:
                item['links'] = str(x.css('a').xpath('@href').extract_first())
            yield item