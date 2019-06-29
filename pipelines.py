# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import  requests
import codecs
import json
import  csv

BASE_DIR = 'E:/weather/weather/weather'
# class WeatherPipeline(object):
#     def __init__(self):
#         self.file = open('weather.json', 'w', encoding = 'utf-8')
#
#     def close_spider(self, spider):
#         self.file.close()
#
#     def process_item(self, item, spider):
#         lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
#         self.file.write(lines)
#         return item


class W2txt(object):
    def process_item(self, item, spider):
        filename = BASE_DIR + '/data/weather.txt'
        with open(filename, 'a+') as f:
            f.write(item['Date'] + '\n')
            f.write(item['City'] + '\n')
            # f.write(item['HignTemperature'] + '\n')
            f.write(item['LowTemperature'] + '\n')
            f.write(item['Weather'] + '\n')
            f.write(item['WindDirection'] + '\n')
            f.write(item['WindStrength'] + '\n\n')
        return item

class W2json(object):
    def process_item(self, item, spider):
        filename = BASE_DIR + '/data/weather.json'
        with codecs.open(filename, 'a+') as f:
            line = json.dumps(dict(item), ensure_ascii=False)
            f.write(line)
        return item


class W2csv(object):
    def process_item(self, item, spider):
        print(item)  #debugging print
        filename = BASE_DIR + '/data/weather.csv'
        with open(filename, 'a+', newline = '') as f:
            csv_write = csv.writer(f, dialect="excel")
            csv_write.writerow([item['City'], item['Date'],  item['LowTemperature'], item['Weather'],
                                  item['WindDirection'], item['WindStrength']])
        return item

