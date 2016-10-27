# -*- coding: utf-8 -*-
# Website Cached at: 2016-07-24 14:35:26

import urlparse

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from meishi.misc.log import *
from meishi.items.MeishiFavItem import *


class MeishiFavSpider(CrawlSpider):
    name = "meishi_fav"
    allowed_domains = ["meishichina.com"]
    start_urls = []
    base_url = "http://home.meishichina.com/"
    rules = (
        Rule(link_extractor = LinkExtractor(
            allow=(r'space-\d+-do-favrecipe-page-\d+\.html'),
            unique=True
        ), callback='parse', follow=True),
    )
    max_limit = 5

    def __init__(self, *a, **kw):
        super(MeishiFavSpider, self).__init__(*a, **kw)
        for i in range(1, self.max_limit):
            self.start_urls.append(self.base_url + "space-" + str(i) + "-do-favrecipe.html")

    def parse(self, response):
        sel = Selector(response)
        item = MeishiFavItem()
        info('parsed ' + str(response))
        yield item
