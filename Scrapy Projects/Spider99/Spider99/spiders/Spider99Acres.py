import scrapy
from Spider99.items import Spider99Item

class Spider99Acres(scrapy.Spider):
	name = "Spider 99 acres"

	start_urls = ['https://www.99acres.com/property-in-bangalore-ffid']

	host_name = "https://www.99acres.com"
	page_count = 0
	def parse(self,response):
		Spider99Acres.page_count+=1

		print(response.url)
		cards = response.xpath("//div[contains(@class,'srpNw_Tpl')]")
		
		for card in cards[:5]:
			item = Spider99Item()

			title1 = card.xpath(".//th[@class='_srpttl']/a/span/text()").extract_first()
			title2 = card.xpath(".//th[@class='_srpttl']/a/span/b/text()").extract_first()
			property_title = title1 + title2

			builder_name = card.xpath(".//a[@class='sName']/b/text()").extract_first()
			

			price = card.xpath(".//span[contains(@class,'srpNw_price ')]/text()").extract_first()
			possession_raw = card.xpath(".//td[contains(@class,'_auto_possesionLabel')]/text()").extract_first()
			possession = possession_raw.replace("\n","").strip(" ")
			# print(possession)

			item['title'] = property_title
			item['builder_name'] = builder_name
			item['price'] = price
			item['possession'] = possession

			yield item

		next_page_abs = response.xpath("//a[@class='pgselActive']/@href").extract_first()
		# print(next_page_abs)
		
		next_page = Spider99Acres.host_name+next_page_abs
		# print(next_page)

		if Spider99Acres.page_count <=5 :
			yield response.follow(url=next_page,callback=self.parse)
		