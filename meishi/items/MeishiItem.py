# -*- coding: utf-8 -*-
# Website Cached at: 2016-10-25 09:09:46

import scrapy
from scrapy.selector import Selector


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

        created_at = sel.css('.rtime').xpath('text()')
        if created_at:
            created_at = created_at.extract()[0].replace(u"发表于", "")
        self['createdAt'] = created_at

        first_image_url = sel.css('.J_photo > img').xpath('@src')
        if first_image_url:
            first_image_url = first_image_url.extract()[0]
        self['recipeFirstImageUrl'] = first_image_url

        recipe_materials = sel.css('div.recipeCategory_sub_R')
        if recipe_materials:
            recipe_materials = recipe_materials[0].css('ul > li')
        self['recipeMaterials'] = []
        for recipe_material in recipe_materials:
            recipe_material_name = recipe_material.css('li > span.category_s1').xpath('text()')
            if recipe_material_name:
                recipe_material_name = recipe_material_name.extract()[0].strip()
            if len(recipe_material_name) == 0:
                recipe_material_name = recipe_material.css('li > span.category_s1 > a').xpath('text()')
                if recipe_material_name:
                    recipe_material_name = recipe_material_name.extract()[0].strip()
            self['recipeMaterials'].append(recipe_material_name)
        
        recipe_ingredients = sel.css('div.recipeCategory_sub_R')
        if recipe_ingredients:
            recipe_ingredients = recipe_ingredients[1].css('ul > li')
        self['recipeIngredients'] = []
        for recipe_ingredient in recipe_ingredients:
            recipe_ingredient_name = recipe_ingredient.css('li > span.category_s1').xpath('text()')
            if recipe_ingredient_name:
                recipe_ingredient_name = recipe_ingredient_name.extract()[0].strip()
            if len(recipe_ingredient_name) == 0:
                recipe_ingredient_name = recipe_ingredient.css('li > span.category_s1 > a').xpath('text()')
                if recipe_ingredient_name:
                    recipe_ingredient_name = recipe_ingredient_name.extract()[0].strip()
            self['recipeIngredients'].append(recipe_ingredient_name)

        recipe_tags = sel.css('div.recipeCategory_sub_R')
        if recipe_tags:
            recipe_tags = recipe_tags[0].css('category_s1')
        self['recipeTags'] = []
        self['recipeDoTypes'] = []
        for recipe_tag in recipe_tags:
            recipe_href = recipe_tag.css('a')
            if recipe_href:
                if 'type-do' in recipe_href.xpath('@href').extract()[0]:
                    recipe_tag_name = recipe_href.xpath('@title').extract()[0]
                    self['recipeDoTypes'].append(recipe_tag_name)
                else:
                    recipe_tag_name = recipe_href.xpath('@title').extract()[0]
                    self['recipeTags'].append(recipe_tag_name)
            else:
                recipe_tag_name = recipe_tag.css('b').xpath('text()').extract()[0]
                self['recipeTags'].append(recipe_tag_name)

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

    @staticmethod
    def max_id():
        return 272353
    
