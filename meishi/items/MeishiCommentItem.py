# -*- coding: utf-8 -*-

import scrapy


class MeishiCommentItem(scrapy.Item):
    recipeId = scrapy.Field()
    commentObj = scrapy.Field()
