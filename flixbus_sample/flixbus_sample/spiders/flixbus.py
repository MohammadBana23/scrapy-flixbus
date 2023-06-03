import scrapy


class FlixbusSpider(scrapy.Spider):
    name = "flixbus"
    allowed_domains = ["global.flixbus.com"]
    start_urls = ["https://global.flixbus.com"]

    def parse(self, response):
        pass
