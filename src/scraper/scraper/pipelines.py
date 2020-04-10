# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from houseChecker.settings.dev import MONGO_SETTINGS
from scrapy.exceptions import DropItem


class ScraperPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            MONGO_SETTINGS['MONGODB_SERVER'],
            MONGO_SETTINGS['MONGODB_PORT']
        )
        db = connection[MONGO_SETTINGS['MONGODB_DB']]
        self.collection = db[MONGO_SETTINGS['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
        return item
