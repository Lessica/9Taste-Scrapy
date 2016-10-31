# -*- coding: utf-8 -*-
# Website Cached at: 2016-07-24 14:35:26


from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.http import Request

from meishi.misc.log import *
from meishi.items.MeishiFavItem import *


class MeishiFavSpider(Spider):
    name = "meishi_fav"
    allowed_domains = ["meishichina.com"]
    start_urls = []
    base_url = "http://home.meishichina.com/"
    max_limit = 1000000 # 9836579

    def __init__(self, *a, **kw):
        super(MeishiFavSpider, self).__init__(*a, **kw)
        for i in range(792234, self.max_limit):
            self.start_urls.append(self.base_url + "space-" + str(i) + "-do-favrecipe.html")

    def parse(self, response):
        sel = Selector(response)
        user_id = sel.css('a.attention').xpath('@user-id')
        if user_id:
            user_id = int(user_id.extract()[0])
        items = []
        j_list = sel.css('#J_list > ul > li')
        for j_detail in j_list:
            item = MeishiFavItem()
            item['userId'] = user_id
            recipe_id = j_detail.css('li').xpath('@data-id')
            if recipe_id:
                recipe_id = recipe_id.extract()[0]
            item['recipeId'] = recipe_id
            items.append(item)
        info('parsed ' + str(response))
        next_urls = sel.css('.ui-page-inner > a')
        if next_urls:
            next_url = next_urls[len(next_urls) - 1].xpath('@href')
            if next_url:
                next_url = next_url.extract()[0]
                yield Request(url=next_url, callback=self.parse)
        for e in items:
            yield e
