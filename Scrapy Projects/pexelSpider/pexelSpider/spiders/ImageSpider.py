from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor 
from pexelSpider.items import PexelspiderItem

class ImageSpider(CrawlSpider):
	name = "Pexel Spider"

	start_urls= ["https://www.pexels.com/collections/breakfast-time-cydtk1d/"]
	allowed_domains =["pexels.com"]

	rules = ( Rule(LinkExtractor(allow=(r'breakfast-time-cydtk1d.*')),callback='parse_item'),
		)

	def parse_item(self,response):
		
		links = response.xpath("//a[contains(@class,'js-photo-link')]/img")
		# print(links)
		for image in links[:2]:
			item = PexelspiderItem()

			img_link = image.xpath(".//@srcset").extract_first().split(",")
			item['image_urls'] = [img_link[0]]

			yield item