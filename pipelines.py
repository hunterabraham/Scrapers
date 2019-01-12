
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item


from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter

class AirtspidersPipeline(object):

  def __init__(self):
    self.files = {SIXCOMPDATA.csv}

  def from_crawler(cls, crawler):
    pipeline = cls()
    crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    return pipeline

  def spider_opened(self, spider):
    file = open('%s_items.csv' % spider.name, 'w+b')
    self.files[spider] = file
    self.exporter = CsvItemExporter(file)
    self.exporter.fields_to_export = [
    'Company Name',
    'Current Price',
    'Previous Close',
    'Day\'s Range',
    'Historical Volatility',
    'Market Cap',
    'Shares Outstanding',
    'EPS',
    'P/E Ratio',
    'Beta (Volatility)',
    'Percent Held by Institutions']
    self.exporter.start_exporting()

  def spider_closed(self, spider):
    self.exporter.finish_exporting()
    file = self.files.pop(spider)
    file.close()

  def process_item(self, item, spider):
    self.exporter.export_item(item)
    return item
from scrapy.exceptions import DropItem
