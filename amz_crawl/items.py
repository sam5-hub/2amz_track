# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.item import Item, Field

import re


# Helper

def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums


def return_value(value):
    return value


class AmazonOrdersItemLoader(ItemLoader):
    # 自定义itemloader
    # 把所有数组自动取第一位
    default_output_processor = TakeFirst()


# Item

class AmazonOrdersItem(Item):
    front_image_url = Field()
    front_image_path = Field()

    des = Field()
    belong = Field()  # 榜单类目
    category = Field()  # 分类
    sub_category = Field()  # 子分类

    rate_num = Field()
    reviews = Field()
    price = Field()
    question_num = Field()
    rank = Field()

    create_time = Field()


class SearchModel(Item):
    # 排名描述
    rank = Field()
    rank_des = Field()
    title = Field()
    des = Field()
    rate_num = Field()
    reviews = Field()
    question_num = Field()
    create_time = Field()
    page = Field()
    sponsored = Field()
    sponsored_rank = Field()

    # def setdes(self):
