# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonOrdersItem(scrapy.Item):
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    des = scrapy.Field()
    rate_num = scrapy.Field()
    reviews = scrapy.Field()
    price = scrapy.Field()
    rank = scrapy.Field()  # 排名
    belong = scrapy.Field()  # 榜单类目
    category = scrapy.Field()  # 分类
    sub_category = scrapy.Field()  # 子分类
    question_num = scrapy.Field()
    create_time = scrapy.Field()


class SearchModel(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    des = scrapy.Field()
    rate_num = scrapy.Field()
    reviews = scrapy.Field()
    question_num = scrapy.Field()
    create_time = scrapy.Field()
    page = scrapy.Field()
    sponsored = scrapy.Field()
    sponsored_rank = scrapy.Field()
