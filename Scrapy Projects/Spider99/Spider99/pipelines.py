# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class Spider99Pipeline(object):
#     def process_item(self, item, spider):
#         return item

from scrapy.exporters import CsvItemExporter
from scrapy.exceptions import DropItem
from pymongo import MongoClient


class CsvItemPipeline(object):

	def __init__(self):
		self.file = open("data.csv","wb")
		self.exporter = CsvItemExporter(self.file,lineterminator="\n")
		self.exporter.start_exporting()


	def close_spider(self,spider):
		self.exporter.finish_exporting()
		self.file.close()

	def process_item(self,item,spider):
		if item['possession'] == 'Ready To Move':
			self.exporter.export_item(item)
			return item	
		else:
			raise DropItem		


class MongoDBPipeline(object):

	def __init__(self):
		self.conn = MongoClient('localhost',27017)
		self.db = self.conn.db2
		self.collection = self.db.collection1 

	# def start_spider(self,spider):
	# 	# self.conn = MongoClient('localhost',27017)
	# 	# self.db = self.conn.sample
	# 	# self.collection = self.db.acres99	
	# 	pass

	def close_spider(self,spider):
		self.conn.close()

	def process_item(self,item,spider):
		self.collection.insert_one(dict(item)) 
		return item



