# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FortuneCompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    rank = scrapy.Field()
    location = scrapy.Field()
    stock = scrapy.Field()
    logo = scrapy.Field()
    industry = scrapy.Field()
