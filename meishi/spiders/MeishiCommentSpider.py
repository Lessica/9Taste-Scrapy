# -*- coding: utf-8 -*-
# Website Cached at: 2016-07-24 14:12:11

import random

from scrapy.spiders import Spider

from meishi.misc.log import *
from meishi.items.MeishiCommentItem import *


class MeishiCommentSpider(Spider):
    name = "meishi_comment"
    allowed_domains = ["meishichina.com"]
    start_urls = []
    base_url = "http://home.meishichina.com/ajax/comment.php"
    base_arguments = {
        "ac": "clist",
        "pageSize": 1000,
        "page": 1,
        "orderBy": "desc",
        "isEdit": 0,
        "isDel": 1,
        "isReply": 1,
        "id": 0,
        "idtype": "recipe",
        "r": 0
    }
    max_limit = 295804

    def __init__(self, *a, **kw):
        super(MeishiCommentSpider, self).__init__(*a, **kw)
        for i in range(1, self.max_limit):
            arguments = self.base_arguments
            arguments["id"] = i
            arguments["r"] = random.randint(0, 999999999999)
            self.start_urls.append(self.base_url + "?" + urllib.urlencode(arguments))

    def parse(self, response):
        items = []
        item = MeishiCommentItem(response)
        items.append(item)
        info('parsed ' + str(response))
        return items
