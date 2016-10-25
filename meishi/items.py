# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

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


class MeishiComment(scrapy.Item):
    recipeId = scrapy.Field()
    commentObj = scrapy.Field()


class MeishiFavItem(scrapy.Item):
    userId = scrapy.Field()
    recipeId = scrapy.Field()
