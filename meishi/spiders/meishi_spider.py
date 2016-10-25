# -*- coding: utf-8 -*-
# Website Cached at: 2016-10-25 09:09:46
# scrapy crawl meishi_spider

import urlparse

from scrapy.selector import Selector
from scrapy.spiders import BaseSpider

from meishi.misc.log import *
from meishi.items import *


class MeishiSpider(BaseSpider):
    name = "meishi"
    allowed_domains = ["meishichina.com"]
    start_urls = []
    base_url = "http://home.meishichina.com/"
    max_limit = 272353

    def __init__(self):
        for i in range(1, self.max_limit):
            self.start_urls.append(self.base_url + "recipe-" + str(i) + ".html")

    def parse(self, response):
        items = []
        sel = Selector(response)
        item = MeishiItem()

        recipe_id = sel.css('#recipe_id').xpath('@value')
        if recipe_id:
            recipe_id = recipe_id.extract()[0]
        else:
            recipe_id = 0
        item['recipeId'] = int(recipe_id)

        recipe_title = sel.css('#recipe_title').xpath('@value')
        if recipe_title:
            recipe_title = recipe_title.extract()[0]
        item['recipeName'] = recipe_title

        author_id = sel.css('#recipe_uid').xpath('@value')
        if author_id:
            author_id = author_id.extract()[0]
        else:
            author_id = 0
        item['authorId'] = int(author_id)

        author_name = sel.css('#recipe_username').xpath('text()')
        if author_name:
            author_name = author_name.extract()[0]
        item['authorName'] = author_name

        created_at = sel.css('.rtime').xpath('text()')
        if created_at:
            created_at = created_at.extract()[0].replace(u"发表于", "")
        item['createdAt'] = created_at

        first_image_url = sel.css('.J_photo > img').xpath('@src')
        if first_image_url:
            first_image_url = first_image_url.extract()[0]
        item['recipeFirstImageUrl'] = first_image_url

        recipe_materials = sel.css('div.recipeCategory_sub_R')
        if recipe_materials:
            recipe_materials = recipe_materials[0].css('ul > li')
        item['recipeMaterials'] = []
        for recipe_material in recipe_materials:
            recipe_material_name = recipe_material.css('li > span.category_s1').xpath('text()')
            if recipe_material_name:
                recipe_material_name = recipe_material_name.extract()[0].strip()
            if len(recipe_material_name) == 0:
                recipe_material_name = recipe_material.css('li > span.category_s1 > a').xpath('text()')
                if recipe_material_name:
                    recipe_material_name = recipe_material_name.extract()[0].strip()
            item['recipeMaterials'].append(recipe_material_name)

        recipe_ingredients = sel.css('div.recipeCategory_sub_R')
        if recipe_ingredients:
            recipe_ingredients = recipe_ingredients[1].css('ul > li')
        item['recipeIngredients'] = []
        for recipe_ingredient in recipe_ingredients:
            recipe_ingredient_name = recipe_ingredient.css('li > span.category_s1').xpath('text()')
            if recipe_ingredient_name:
                recipe_ingredient_name = recipe_ingredient_name.extract()[0].strip()
            if len(recipe_ingredient_name) == 0:
                recipe_ingredient_name = recipe_ingredient.css('li > span.category_s1 > a').xpath('text()')
                if recipe_ingredient_name:
                    recipe_ingredient_name = recipe_ingredient_name.extract()[0].strip()
            item['recipeIngredients'].append(recipe_ingredient_name)

        recipe_tags = sel.css('div.recipeCategory_sub_R')
        if recipe_tags:
            recipe_tags = recipe_tags[0].css('category_s1')
        item['recipeTags'] = []
        item['recipeDoTypes'] = []
        for recipe_tag in recipe_tags:
            recipe_href = recipe_tag.css('a')
            if recipe_href:
                if 'type-do' in recipe_href.xpath('@href').extract()[0]:
                    recipe_tag_name = recipe_href.xpath('@title').extract()[0]
                    item['recipeDoTypes'].append(recipe_tag_name)
                else:
                    recipe_tag_name = recipe_href.xpath('@title').extract()[0]
                    item['recipeTags'].append(recipe_tag_name)
            else:
                recipe_tag_name = recipe_tag.css('b').xpath('text()').extract()[0]
                item['recipeTags'].append(recipe_tag_name)

        description = sel.css('#block_txt > div').xpath('text()')
        if description:
            description = description.extract()[0].strip()
            if len(description) != 0:
                item['recipeDescription'] = description

        tip = sel.css('div.recipeTip').xpath('text()')
        if tip:
            tip = tip.extract()[0].strip()
            if len(tip) != 0:
                item['recipeTip'] = tip

        items.append(item)
        info('parsed ' + str(response))
        return items
