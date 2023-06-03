import scrapy
from scrapy.crawler import CrawlerProcess


class FlixbusSpider(scrapy.Spider):
    name = "flixbus"
    allowed_domains = ["shop.global.flixbus.com"]
    # start_urls = ["https://global.flixbus.com"]
    
    def __init__(self, from_city_id=None, to_city_id=None, date=None, *args, **kwargs):
        super(FlixbusSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"https://shop.global.flixbus.com/search?departureCity={from_city_id}&arrivalCity={to_city_id}&rideDate={date}&adult=1"]

    def parse(self, response):
        print("--------------------------------$$$##########$$$$$$$$$$$$$######")
        print(response)
        print("--------------------------------$$$##########$$$$$$$$$$$$$######")
