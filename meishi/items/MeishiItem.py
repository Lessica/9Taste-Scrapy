# -*- coding: utf-8 -*-

import scrapy


class MeishiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    recipeId = scrapy.Field()
    createdAt = scrapy.Field()
    authorId = scrapy.Field()
    authorName = scrapy.Field()
    recipeName = scrapy.Field()
    recipeFirstImageUrl = scrapy.Field()
    recipeMaterials = scrapy.Field()
    recipeIngredients = scrapy.Field()
    recipeTags = scrapy.Field()
    recipeDoTypes = scrapy.Field()
    recipeDescription = scrapy.Field()
    recipeTip = scrapy.Field()
