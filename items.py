# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    City = scrapy.Field()
    Date = scrapy.Field()
    # HignTemperature = scrapy.Field()
    LowTemperature = scrapy.Field()
    Weather = scrapy.Field()
    WindDirection = scrapy.Field()
    WindStrength = scrapy.Field()



