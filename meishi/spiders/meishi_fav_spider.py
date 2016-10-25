# -*- coding: utf-8 -*-
# Website Cached at: 2016-07-24 14:35:26

import urlparse

from scrapy.selector import Selector
from scrapy.spiders import BaseSpider

from meishi.misc.log import *
from meishi.items import *


class MeishiFavSpider(BaseSpider):
    name = "meishi_fav"
    allowed_domains = ["meishichina.com"]
    start_urls = []
    base_url = "http://home.meishichina.com/"
    max_limit = 272353

    def __init__(self):
        for i in range(1, self.max_limit):
            self.start_urls.append(self.base_url + "recipe-" + str(i) + ".html")

    def parse(self, response):
        items = []
        sel = Selector(response)
        item = MeishiFavItem()

        items.append(item)
        info('parsed ' + str(response))
        return items
