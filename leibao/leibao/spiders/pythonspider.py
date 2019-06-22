# -*- coding: utf-8 -*-
import scrapy
from ..items import LeibaoItem

class PythonspiderSpider(scrapy.Spider):
    name = 'pythonspider'
    allowed_domains = ['www.liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?key=python']

    def parse(self, response):
        items_list = response.xpath("//ul[contains(@class, 'sojob-list')]/li")

        for i in items_list:
            name = i.xpath(".//h3/@title").get()
            dec = i.xpath(".//p[contains(@class, 'condition')]/@title").get()
            dec = dec.split("_")
            gz = dec[0]
            dd = dec[1]
            xl = dec[2]
            jy = dec[3]
            url = i.xpath(".//h3/a/@href").get()
            if not url.startswith('https'):
                url = response.urljoin(url)
            cn = i.xpath(".//div[contains(@class, 'company-info')]/p/a/text()").get()
            item = LeibaoItem(name=name,gz=gz,dd=dd, xl=xl, jy=jy, url=url,cn=cn)
            yield item

        next_url = response.xpath("//div[contains(@class, 'pagerbar')]/a[last()-1]/@href").get()
        if not next_url:
            print('*'*1000)
        if len(next_url) > 20:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)

