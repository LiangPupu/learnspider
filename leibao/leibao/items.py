# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LeibaoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    gz = scrapy.Field()
    dd = scrapy.Field()
    xl = scrapy.Field()
    jy = scrapy.Field()
    cn = scrapy.Field()
    url = scrapy.Field()
