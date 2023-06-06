import json
import pytest
from scrapy.http import TextResponse
from scrapy.utils.test import get_crawler
from flixbus_sample.spiders.flixbus import FlixbusSpider


@pytest.fixture
def flixbus_spider():
    # تنظیم مقادیر پارامترها برای استفاده در تست
    from_city_id = '1'
    to_city_id = '2'
    date = '2023-06-01'
    
    # ساخت شی Spider با پارامترهای فوق
    spider = FlixbusSpider(from_city_id=from_city_id, to_city_id=to_city_id, date=date)
    
    return spider


def test_flixbus_spider_parse_method(flixbus_spider):
    # تست تابع parse در FlixbusSpider
    
    # مثالی از پاسخ مورد انتظار
    response_data = {
        "cities": ["City 1", "City 2"],
        "brands": ["Brand 1", "Brand 2"],
        "operators": ["Operator 1", "Operator 2"],
        "stations": ["Station 1", "Station 2"],
        "trips": ["Trip 1", "Trip 2"],
    }
    url = f"https://global.api.flixbus.com/search/service/v4/search?from_city_id=1&to_city_id=2&departure_date=2023-06-01&products=%7B%22adult%22%3A1%7D&currency=EUR&locale=en&search_by=cities&include_after_midnight_rides=1"
    
    # تبدیل پاسخ مورد انتظار به فرمت JSON
    response_json = json.dumps(response_data)
    
    # ساخت یک نمونه از TextResponse با استفاده از پاسخ مورد انتظار
    response = TextResponse(url=url, body=response_json, encoding='utf-8')
    
    # فراخوانی تابع parse بر روی شی Spider با استفاده از پاسخ مورد انتظار
    parsed_data = list(flixbus_spider.parse(response))
    print("ressssssssssssss booood",response.status)
    print("paaaaaars dadaaaaas",parsed_data)
    print(response_data)
    # بررسی اینکه آیا پاسخ درست است
    assert len(parsed_data) == 2
    assert parsed_data[0] == response_data
