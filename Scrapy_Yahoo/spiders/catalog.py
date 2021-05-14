import scrapy


class CatalogSpider(scrapy.Spider):
    name = 'catalog'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['http://finance.yahoo.com/']

    def parse(self, response):
        pass
