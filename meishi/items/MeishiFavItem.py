# -*- coding: utf-8 -*-

import scrapy


class MeishiFavItem(scrapy.Item):
    userId = scrapy.Field()
    recipeId = scrapy.Field()
