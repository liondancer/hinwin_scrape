# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class HinwinItem(scrapy.Item):
#     link = scrapy.Field()
#     post_title = scrapy.Field()
#     datetime_posted = scrapy.Field()
#     location = scrapy.Field()


# Items are containers that will be loaded with scraped data
class CraigslistItem(scrapy.Item):
    link = scrapy.Field()
    post_title = scrapy.Field()
    updated = scrapy.Field()
    location = scrapy.Field()
    post = scrapy.Field()
    contact_info = scrapy.Field()
    email = scrapy.Field()
    posted = scrapy.Field()
    post_id = scrapy.Field()
