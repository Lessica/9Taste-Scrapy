# -*- coding: utf-8 -*-
# Website Cached at: 2016-10-25 09:09:46

import scrapy
from scrapy.selector import Selector


class MeishiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    recipeId = scrapy.Field()
    authorId = scrapy.Field()
    authorName = scrapy.Field()
    recipeName = scrapy.Field()
    recipeFirstImageUrl = scrapy.Field()
    recipeMaterials = scrapy.Field()
    recipeTags = scrapy.Field()
    recipeDescription = scrapy.Field()
    recipeTip = scrapy.Field()

    def __init__(self, response):
        super(MeishiItem, self).__init__(self)

        sel = Selector(response)

        recipe_id = sel.css('#recipe_id').xpath('@value')
        if recipe_id:
            recipe_id = recipe_id.extract()[0]
        else:
            recipe_id = 0
        self['recipeId'] = int(recipe_id)

        recipe_title = sel.css('#recipe_title').xpath('@value')
        if recipe_title:
            recipe_title = recipe_title.extract()[0]
        self['recipeName'] = recipe_title

        author_id = sel.css('#recipe_uid').xpath('@value')
        if author_id:
            author_id = author_id.extract()[0]
        else:
            author_id = 0
        self['authorId'] = int(author_id)

        author_name = sel.css('#recipe_username').xpath('text()')
        if author_name:
            author_name = author_name.extract()[0]
        self['authorName'] = author_name

        first_image_url = sel.css('.J_photo > img').xpath('@src')
        if first_image_url:
            first_image_url = first_image_url.extract()[0]
        self['recipeFirstImageUrl'] = first_image_url

        recipe_materials = []
        materials = sel.css('div.recipeCategory_sub_R')[0].css('ul > li')
        for material in materials:
            material_t = material.css('li > span.category_s1 > a > b')
            if len(material_t) == 0:
                material = material.css('li > span.category_s1 > b').xpath('text()')
            else:
                material = material_t.xpath('text()')
            if material:
                material = material.extract()[0]
                recipe_materials.append(material)
        self['recipeMaterials'] = recipe_materials

        recipe_tags = []
        tags = sel.css('div.recipeCategory_sub_R')[1].css('ul > li')
        for tag in tags:
            tag_t = tag.css('li > span.category_s1 > a')
            if len(tag_t) == 0:
                tag = tag.css('li > span.category_s1 > b').xpath('text()')
            else:
                tag = tag_t.xpath('text()')
            if tag:
                tag = tag.extract()[0]
                recipe_tags.append(tag)
        self['recipeTags'] = recipe_tags

        description = sel.css('#block_txt > div').xpath('text()')
        if description:
            description = description.extract()[0].strip()
            if len(description) != 0:
                self['recipeDescription'] = description

        tip = sel.css('div.recipeTip').xpath('text()')
        if tip:
            tip = tip.extract()[0].strip()
            if len(tip) != 0:
                self['recipeTip'] = tip
