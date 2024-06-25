import scrapy


class LemanapronewparsSpider(scrapy.Spider):
    name = "lemanapronewpers"
    allowed_domains = ["https://lemanapro.ru/"]
    start_urls = ["https://lemanapro.ru/catalogue/osveshchenie/"]

    def parse(self, response):
        pass
