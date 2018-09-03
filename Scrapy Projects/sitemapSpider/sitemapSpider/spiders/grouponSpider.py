import scrapy
from scrapy.spiders import SitemapSpider

class SpiderGroupOn(SitemapSpider):
	name = "GroupOn"
	sitemap_urls = ["https://www.groupon.com/sitemap.xml"]

	sitemap_rules = [('/deals/','parse_deal')]
	
	def parse_deal(self,response):
		print(response.url)

	# def parse(self,response):
	# 	print(response.url)