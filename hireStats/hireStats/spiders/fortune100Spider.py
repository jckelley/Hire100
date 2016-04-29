import scrapy

class fortune100Spider(scrapy.Spider):
	name = "fortune100"
	allowed_domains = ["fortune.com"]
	start_urls = [
		"http://fortune.com/fortune500/"
	]


	def parse(self, response):
		filename = response.url.split("/")[-2] + '.html'
		with open(filename, "wb") as f:
			f.write(response.body)