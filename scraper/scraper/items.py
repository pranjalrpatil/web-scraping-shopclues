# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

import pathlib


class ScraperItem(scrapy.Item):
    titles = scrapy.Field(serializer = str)
    prices = scrapy.Field(serializer = str)
    images=scrapy.Field(serializer = str)