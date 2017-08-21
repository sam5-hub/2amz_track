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

import json
import re
import time
import os


def get_urls_from_json(json_path):
    urls = []
    with open(json_path) as json_file:
        data = json.load(json_file)
        json_dict = data
        amazon_url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3D"

        keywords = json_dict['keywords']
        categories = json_dict['categories']

        for category in categories:
            for keyword in keywords:
                url = amazon_url + category + '&field-keywords=' + keyword
                urls.append(url)

    return urls


def get_time_from_file_name(file_name):
    l = re.split(r'_', file_name)
    t = l[0]
    return get_time_from_timestamp(t)


def get_time_from_timestamp(t):
    time_local = time.localtime(int(t))
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt
