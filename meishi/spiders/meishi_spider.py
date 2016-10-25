# -*- coding: utf-8 -*-
# Website Cached at: 2016-10-25 09:09:46
# scrapy crawl meishi_spider

import urlparse

from scrapy.spiders import BaseSpider
from meishi.misc.log import *
from meishi.items.MeishiItem import *


class MeishiSpider(BaseSpider):
    name = "meishi"
    allowed_domains = ["meishichina.com"]
    start_urls = []
    base_url = "http://home.meishichina.com/"
    max_limit = MeishiItem.max_id()

    def __init__(self):
        for i in range(1, self.max_limit):
            self.start_urls.append(self.base_url + "recipe-" + str(i) + ".html")

    def parse(self, response):
        items = []
        item = MeishiItem(response)
        items.append(item)
        info('parsed ' + str(response))
        return items
