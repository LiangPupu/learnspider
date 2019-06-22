# -*- coding: utf-8 -*-
import scrapy
from ..items import MyspiderItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        item_list = response.xpath("//div[contains(@class, 'quote')]")
        # print(item_list)

        for i in item_list:
            text = i.xpath("./span[contains(@class, 'text')]/text()").get()
            author = i.xpath(".//small/text()").get()
            tags = i.xpath("./div[contains(@class, 'tags')]/a/text()").getall()
            item = MyspiderItem()
            item['text']=text
            item['author']=author
            item['tags']=tags
            yield item
        next_url = response.xpath('//li[contains(@class, "next")]//a/@href').get()

        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse)


