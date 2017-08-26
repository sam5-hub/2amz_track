# -*- coding: utf-8 -*-
__author__ = 'samwuu'

from scrapy.cmdline import execute
import sys
import os

BSR = 'https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_unv_auto_0_15718271_2'
HNR = 'https://www.amazon.com/gp/new-releases/ref=zg_bsnr_unv_0_7147440011_2'

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
cmd = 'scrapy crawl amz_spider'
execute(cmd.split())
