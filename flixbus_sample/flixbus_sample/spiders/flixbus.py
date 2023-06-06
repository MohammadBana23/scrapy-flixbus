import scrapy
import json


class FlixbusSpider(scrapy.Spider):
    name = "flixbus"
    allowed_domains = ["shop.global.flixbus.com"]
    # start_urls = ["https://global.flixbus.com"]
    required_parameters = [
        'from_city_id',
        'to_city_id',
        'date',
    ]
    
    def __init__(self, from_city_id=None, to_city_id=None, date=None, *args, **kwargs):
        super(FlixbusSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"https://global.api.flixbus.com/search/service/v4/search?from_city_id={from_city_id}&to_city_id={to_city_id}&departure_date={date}&products=%7B%22adult%22%3A1%7D&currency=EUR&locale=en&search_by=cities&include_after_midnight_rides=1"]

    def parse(self, response):
        print("--------------------------------$$$##########$$$$$$$$$$$$$######")
        try:
            data = json.loads(response.text)
            cities = data["cities"]
            brands = data["brands"]
            operators = data["operators"]
            stations = data["stations"]
            trips = data["trips"]
            yield {
                "cities": cities,
                "brands": brands,
                "operators": operators,
                "stations" : stations,
                "trips": trips,
            }
        except Exception as e:
            print(f"Error: {e}")
        print("--------------------------------$$$##########$$$$$$$$$$$$$######")