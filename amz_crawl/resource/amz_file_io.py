"""
关键词搜索

id,用户名字,keywords

filename : 1462451334_sam_keywords.json
format:
    {'keywords': ['key1', 'key2'], 'categories': ['woman', 'man']}

根据类目去爬虫
id,用户名字,keywords

filename : 1462451334_sam_crawl.json
format:
    {'category': "clothing/woman/underwear",
    "start_time":1462451334,
    "end_time":1462451339}



"""


import re
import time
import os
import pandas as pd
from urllib.parse import quote
import json



def urls_from_file_path(file_path):
    if 'keywords.json' in file_path:
        return get_keywords_urls_from_json(file_path)
    elif 'cate_crawl.json' in file_path:
        return get_bsr_new_crawl_urls_from_json(file_path)
    else:
        raise Exception("文件格式错误")


def get_keywords_urls_from_json(json_path):
    urls = []
    with open(json_path) as json_file:
        data = json.load(json_file)
        json_dict = data
        amazon_url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3D"

        keywords = json_dict['keywords']
        categories = json_dict['categories']

        for category in categories:
            for keyword in keywords:
                url = amazon_url + quote(category) + '&field-keywords=' + quote(keyword)
                urls.append(url)

    return urls
def get_bsr_new_crawl_urls_from_json(json_path):

    urls = []
    with open(json_path) as json_file:
        data = json.load(json_file)
        json_dict = data
        amazon_url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3D"

        keywords = json_dict['keywords']
        categories = json_dict['categories']

        for category in categories:
            for keyword in keywords:
                url = amazon_url + quote(category) + '&field-keywords=' + quote(keyword)
                urls.append(url)

    return urls


if __name__ == '__main__':
    urls = urls_from_file_path('1462451334_sam_keywords.json')
    print(urls)
