#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re, datetime
import urllib
import json
from bs4 import BeautifulSoup
from lib.urlopener import URLOpener
from base import BaseFeedBook
from config import SHARE_FUCK_GFW_SRV

def getBook():
    return tech

class tech(BaseFeedBook):
    title                 = u'Tech News'
    __author__            = 'freereaper'
    description           = u'每周科技新闻精选，知乎问答精选，Quora精选，豆瓣，博客，经济学人China和Tech部分，各种科普，果壳天文，深夜食堂，数学精选。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_freereaper.gif"
    coverfile             = "cv_freereaper.jpg"
    network_timeout       = 60
    oldest_article        = 1
    max_articles_per_feed = 9
    #留空则每天投递
    #deliver_days          = ['Friday']
    deliver_times = [6]
    feeds = [
        ('36kr', 'http://www.36kr.com/feed?1.0'),
        (u'左岸读书', 'http://www.zreading.cn/feed'),
        (u'好奇心日报', 'http://www.qdaily.com/feed'),
        (u'TechCrunch 中国', 'http://techcrunch.cn/feed/'),
        (u'爱范儿', 'http://www.ifanr.com/feed'),
        ('Top News - MIT Technology Review', 'http://www.technologyreview.com/topnews.rss'),
        ('Hacker News', 'https://news.ycombinator.com/rss'),
        (u'麻省理工科技评论', 'http://zhihurss.miantiao.me/section/id/14'),
        (u'大公司日报', 'http://zhihurss.miantiao.me/daily/id/5'),
        (u'小道消息', 'http://hutu.me/feed'),
        (u'极客公园', 'http://www.geekpark.net/rss'),
        (u'极客范', 'http://www.geekfan.net/feed/'),
        (u'人人都是产品经理', 'http://iamsujie.com/feed/'),
        (u'邹剑波Kant', 'http://kant.cc/feed'),
        (u'环球科学', 'http://blog.sina.com.cn/rss/sciam.xml'),
        (u'泛科学', 'http://pansci.tw/feed'),
        (u'果壳网', 'http://www.guokr.com/rss/'),
        (u'果壳网科学人', 'http://feed43.com/8781486786220071.xml'),
        (u'简书推荐', 'http://jianshu.milkythinking.com/feeds/recommendations/notes'),
        ('Quora', 'http://www.quora.com/rss', True),
        ('The Economist: China', 'http://www.economist.com/feeds/print-sections/77729/china.xml'),
        ('The Economist: Science and technology', 'http://www.economist.com/feeds/print-sections/80/science-and-technology.xml'),
        ('The Economist: Asia', 'http://www.economist.com/feeds/print-sections/73/asia.xml'),
        (u'知乎日报', 'http://zhihurss.miantiao.me/dailyrss'),
        (u'深夜食堂', 'http://zhihurss.miantiao.me/section/id/1'),
        (u'BBC', 'http://www.bbc.com/zhongwen/simp/index.xml'),
        (u'reddit', 'http://www.reddit.com/r/nosleep/top/.rss?sort=top&t=day'),
        ]

