# -*- coding: utf-8 -*-
# Website Cached at: 2016-07-24 14:12:11

import random
import json
import urlparse
import urllib

from scrapy.spiders import BaseSpider

from meishi.misc.log import *
from meishi.items import *


class MeishiCommentSpider(BaseSpider):
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
    max_limit = 272353

    def __init__(self):
        for i in range(1, self.max_limit):
            arguments = self.base_arguments
            arguments["id"] = i
            arguments["r"] = random.randint(0, 999999999999)
            self.start_urls.append(self.base_url + "?" + urllib.urlencode(arguments))

    def parse(self, response):
        items = []
        raw = response.text
        obj = json.loads(raw)
        item = MeishiComment()
        url = response.url
        result = urlparse.urlparse(url)
        params = urlparse.parse_qs(result.query, True)
        item['recipeId'] = int(params['id'][0])
        item['commentObj'] = obj['data']
        items.append(item)
        info('parsed ' + str(response))
        return items
