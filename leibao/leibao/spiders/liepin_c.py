# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LeibaoItem


class LiepinCSpider(CrawlSpider):
    name = 'liepin_c'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?key=python']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[contains(@class, 'pagerbar')]/a[last()-1]"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
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
            item = LeibaoItem(name=name, gz=gz, dd=dd, xl=xl, jy=jy, url=url, cn=cn)
            yield item