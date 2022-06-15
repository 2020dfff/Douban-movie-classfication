import scrapy
import json
from douban.items import DoubanComment

class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/subject/1292052/comments?start=0&limit=600&status=P&sort=time']


    def start_requests(self):
       f = open("./movie.json") 
       movies = json.load(f)
       for movie in movies:
           url = movie['detail_url'] + "comments?start=0&limit=600&status=P&sort=time"
           yield scrapy.Request(url=url, callback=self.parse)
            url = movie['detail_url'] + "comments?start=0&limit=600&status=P&sort=new_score"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = DoubanComment()
        title = response.css('#content h1::text').get()
        for node in response.xpath('//div[@id="comments"]/div'):
            item['movie'] = title
            item['username'] = node.css('.comment-info a::text').get()
            item['comment'] = node.css('span.short::text').get()
            item['score'] = node.css('.comment-info .rating').xpath('@title').get()
            item['time'] = node.css('.comment-time').xpath('@title').get()
            item['vote'] = node.css('.vote-count::text').get()
            yield item
