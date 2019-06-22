# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy
from .settings import IMAGES_STORE
import os

class DyPipeline(object):
    def process_item(self, item, spider):
        return item


class DyImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['img_link']
        yield scrapy.Request(url=image_link)

    def item_completed(self, results, item, info):
        # print(results)
        img_path = [x['path'] for y, x in results if y][0]
        old_path = IMAGES_STORE + img_path
        new_path = IMAGES_STORE + 'full/'+item['nickname'] + '.jpg'
        os.rename(old_path, new_path)
        return item
