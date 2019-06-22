# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class LeibaoPipeline(object):
    def __init__(self):
        self.f = open('leipin.csv', 'a', encoding='utf-8', newline='')
        self.filesname = ['name','gz', 'dd', 'xl', 'jy', 'cn', 'url' ]
        self.writer = csv.DictWriter(self.f, fieldnames=self.filesname)
        self.writer.writeheader()
    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item
    def close(self):
        self.f.close()
