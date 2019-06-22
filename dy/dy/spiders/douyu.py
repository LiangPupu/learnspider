# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DyItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    url = 'http://capi.douyucdn.cn/api/v1/getColumnRoom/8?client_sys=android&limit=20&offset='
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        items_list = json.loads(response.body)['data']
        if items_list:
            for i in items_list:
                item = DyItem()
                item['nickname'] = i['nickname']
                item['img_link'] = i['vertical_src']
                item['room_id'] = i['room_id']
                yield item
            self.offset += 20
            url = self.url + str(self.offset)
            print("--"*50)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

