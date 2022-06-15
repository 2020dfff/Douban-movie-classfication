# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DoubanMovie(scrapy.Item):
    name = scrapy.Field()
    ranking = scrapy.Field()
    score = scrapy.Field()
    review_count = scrapy.Field()
    year = scrapy.Field()
    quote = scrapy.Field()
    detail_url = scrapy.Field()
    introduce = scrapy.Field()

class DoubanComment(scrapy.Item):
    movie = scrapy.Field()
    username = scrapy.Field()
    comment = scrapy.Field()
    score = scrapy.Field()
    time = scrapy.Field()
    vote = scrapy.Field()
