# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter

class AopspiderPipeline(object):

  def __init__(self):
    self.files = {AOPDATA.csv}

  def process_item(self, item, spider):
    self.exporter.export_item(item)
    return item
from scrapy.exceptions import DropItem
