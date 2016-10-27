# -*- coding: utf-8 -*-
# Cached at: 2016-10-27 15:43

import scrapy


class MeishiFavItem(scrapy.Item):
    userId = scrapy.Field()
    recipeId = scrapy.Field()
