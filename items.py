# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AopspiderItem(scrapy.Item):
    REVLYA1 = scrapy.Field()
    REVLYA2 = scrapy.Field()
    REVLYA3 = scrapy.Field()
    REVLYA4 = scrapy.Field()
    EBITDALYA1 = scrapy.Field()
    EBITDALYA2 = scrapy.Field()
    EBITDALYA3 = scrapy.Field()
    EBITDALYA4 = scrapy.Field()
    SGALYA1 = scrapy.Field()
    SGALYA2 = scrapy.Field()
    SGALYA3 = scrapy.Field()
    SGALYA4 = scrapy.Field()
    REVLQA1 = scrapy.Field()
    REVLQA2 = scrapy.Field()
    REVLQA3 = scrapy.Field()
    REVLQA4 = scrapy.Field()
    CapExLYA1 = scrapy.Field()
    CapExLYA2 = scrapy.Field()
    CapExLYA3 = scrapy.Field()
    CapExLYA4 = scrapy.Field()
    PtoBV = scrapy.Field()
    EVtoEBITDA = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
