# -*- coding: utf-8 -*-

# Scrapy settings for amz_crawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os
import socket

BOT_NAME = 'amz_crawl'

SPIDER_MODULES = ['amz_crawl.spiders']
NEWSPIDER_MODULE = 'amz_crawl.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'amz_crwal.middlewares.AmazonOrdersSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     'amazon_orders.middlewares.ProxyMiddleware': 100,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'amz_crawl.pipelines.AmazonOrdersPipeline': 1,
    'amz_crawl.pipelines.AmazonOrdersImagePipeline': 2,
    'amz_crawl.pipelines.AmzCrawlXLSXPipeline': 3,

}

# field名字，是数组
IMAGES_URLS_FIELD = "front_image_url"
project_dir = os.path.abspath(os.path.curdir)

# 放到指定位置 /home/images/....

if socket.gethostname() == 'iZwz9gxohhsdr3oj02junuZ':
    IMAGES_STORE = '/home/AMZ-ALL-BSR-HNR/Images'
else:
    IMAGES_STORE = os.path.join(project_dir, 'resource')

if socket.gethostname() == 'iZwz9gxohhsdr3oj02junuZ':
    RESOURCE_STORE = '/home/AMZ-ALL-BSR-HNR'
else:
    RESOURCE_STORE = os.path.join(project_dir, 'AMZ-ALL-BSR-HNR')

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DB_SERVER = 'MySQLdb'
DB_CONNECT = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '&ilk_CfUc9x/',
    'port': 3306,
    'db': 'ams',
    'charset': 'utf8',
    'use_unicode': True
}
