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
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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

}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

# 代理
# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = '/path/to/proxy/list.txt'

# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
# CUSTOM_PROXY = "http://host1:port"

DOWNLOADER_MIDDLEWARES = {

    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'amz_crawl.middlewares.RandomUserAgentMiddleware': 543,  # 自定义
    # 'amz_crawl.middlewares.RandomProxyMiddleware': 542
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    # 'scrapy_proxies.RandomProxy': 100,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    # 'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    #  scrapy_fake_useragent 框架
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# MYEXT_ENABLED = True
# EXTENSIONS = {
#     'scrapy.extensions.telnet.TelnetConsole': None,
#     'amz_crawl.extensions.SpiderOpenCloseLogging': 200,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'amz_crawl.pipelines.AmzCrawlPipeline': 1,
    'amz_crawl.pipelines.AmazonOrdersImagePipeline': 2,
    'amz_crawl.pipelines.AmzCrawlXLSXPipeline': 3,

}

# field名字，是数组
# IMAGES_URLS_FIELD = "front_image_url"
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



# linux pip install MySQL-python
DATABASE = {'drivername': 'mysql',
            'host': 'localhost',
            'port': '3306',
            'username': 'root',
            'password': '&ilk_CfUc9x/',
            'database': 'spider',
            'query': {'charset': 'utf8'}}
