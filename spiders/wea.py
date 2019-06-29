import scrapy
import re
import os
import json
from scrapy import  Request
from weather.items import WeatherItem

class WeatherSpider(scrapy.Spider):
    name = 'MySpider'
    allowed_domains = ["www.weather.com.cn/weather/101220101.shtml"]
    start_urls = ['http://www.weather.com.cn/weather/101220101.shtml']
    # proxy = get_proxy()
    # proxies = {
    # 'http': 'http://' + proxy,
    # 'https': 'https://' + proxy,
    # }

    def start_requests(self):
        with open('weather_code.json', 'r', encoding = 'utf-8') as f:
            self.weather_code = json.load(f)
        self.url = 'http://www.weather.com.cn/weather/{code}.shtml'
        for self.key in self.weather_code:
            request = Request(url = self.url.format(code = self.key), callback = self.parse)
            request.meta['code'] = self.key
            # print(self.weather_code[self.key])
            yield request

    def parse(self, response):
        items = []
        item = WeatherItem()
        item['City'] = self.weather_code[response.meta['code']]
        weather = response.xpath('//ul[@class="t clearfix"]')
        for i in list(range(7)):
            item['Date'] = weather.xpath('./li[' + str(i + 1) + ']/h1/text()').extract()[0]
            # item['HignTemperature'] = weather.xpath('./li[' + str(i + 1) + ']/p[@class="tem"]/span/text()').extract()[0]
            # item['HignTemperature'] = 1
            item['LowTemperature'] = weather.xpath('./li[' + str(i + 1) + ']/p[@class="tem"]/i/text()').extract()[0]
            item['Weather'] = weather.xpath('./li[' + str(i + 1) + ']/p[@class="wea"]/text()').extract()[0]
            item['WindDirection'] = weather.xpath('./li[' + str(i + 1) + ']/p[@class="win"]/em/span/@title').extract()[0]
            item['WindStrength'] = weather.xpath('./li[' + str(i + 1) + ']/p[@class="win"]/i/text()').extract()[0]
            items.append(item)
        return items



