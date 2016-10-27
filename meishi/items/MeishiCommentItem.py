# -*- coding: utf-8 -*-

import scrapy
import json
import urlparse


class MeishiCommentItem(scrapy.Item):
    recipeId = scrapy.Field()
    commentObj = scrapy.Field()

    def __init__(self, response):
        super(MeishiCommentItem, self).__init__(self)

        raw = response.text
        obj = json.loads(raw)
        url = response.url
        result = urlparse.urlparse(url)
        params = urlparse.parse_qs(result.query, True)
        self['recipeId'] = int(params['id'][0])
        self['commentObj'] = obj['data']
