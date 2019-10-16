# -*- coding: utf-8 -*-
import scrapy
from scraping.items import ScrapingItem

class SpidermanSpider(scrapy.Spider):
    name = 'spiderman'
    allowed_domains = ['http://sagitario.itmorelia.edu.mx/~rogelio']
    start_urls = ['http://http://sagitario.itmorelia.edu.mx/~rogelio/']

    def parse(self, response):
        item= ScrapingItem()
        item['titulos']=response.css('a').xpath('@href').extract()
        item['titulos2']=response.css('a').xpath('@href').extract()
        return item
