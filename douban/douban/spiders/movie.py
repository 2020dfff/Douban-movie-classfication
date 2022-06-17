import scrapy
from douban.items import DoubanMovie

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = DoubanMovie()
        for node in response.xpath('//ol[@class="grid_view"]/li'):
            item['ranking'] = node.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['name'] = node.xpath('.//span[@class="title"][1]/text()').extract()[0]
            item['score'] = node.xpath('.//div[@class="star"]/span[2]/text()').extract()[0]
            item['review_count'] = node.xpath('.//div[@class="star"]/span[4]/text()').extract()[0]
            item['quote'] = node.xpath('.//p[@class="quote"]/span/text()').extract_first()
            item['detail_url'] = node.xpath('.//div[@class="pic"]/a/@href').extract()[0]
            item['introduce'] = ''.join(node.xpath('.//div[@class="bd"]/p/text()').extract()[0]).strip() + '\n' + ''.join(node.xpath('.//div[@class="bd"]/p[1]/text()').extract()[1]).strip()

            yield item
            print(item)

        next_page = response.xpath('//span[@class="next"]/a/@href')
        if next_page:
            url = 'https://movie.douban.com/top250' + next_page[0].extract()
            yield scrapy.Request(url, callback=self.parse)
