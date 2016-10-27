# -*- coding: utf-8 -*-
# Website Cached at: 2016-10-27 15:45:23
# scrapy crawl meishi_spider

import urlparse

from scrapy.spiders import Spider
from meishi.misc.log import *
from meishi.items.MeishiItem import *


class MeishiSpider(Spider):
    name = "meishi"
    allowed_domains = ["meishichina.com"]
    start_urls = []
    base_url = "http://home.meishichina.com/"
    max_limit = 295804

    def __init__(self, *a, **kw):
        super(MeishiSpider, self).__init__(*a, **kw)
        for i in range(1, self.max_limit):
            self.start_urls.append(self.base_url + "recipe-" + str(i) + ".html")

    def parse(self, response):
        items = []
        item = MeishiItem(response)
        items.append(item)
        info('parsed ' + str(response))
        return items
