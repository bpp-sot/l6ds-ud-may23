import scrapy


class HackerNewsSpider(scrapy.Spider):
    name = "hacker_news_spider"
    start_urls = ["https://news.ycombinator.com/news"]

    def parse(self, response):
        for link in response.css('span.titleline > a'):
            yield {'title': link.css('::text').get(), 'link': link.css('::attr(href)').get()}

# scrapy runspider hacker_news_spider.py -o hacker_news.json
