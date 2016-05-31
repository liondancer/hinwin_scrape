
import scrapy
import json
import os


class CraigslistSpider(scrapy.Spider):
    name = "craigslist"
    start_urls = [
        "https://geo.craigslist.org/iso/"
    ]

    def parse(self, response):



