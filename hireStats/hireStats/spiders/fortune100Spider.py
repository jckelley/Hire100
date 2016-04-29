import scrapy
from bs4 import BeautifulSoup
from hireStats.items import FortuneCompanyItem
import re

class fortune100Spider(scrapy.Spider):
	name = "fortune100"
	allowed_domains = ["fortune.com"]
	start_urls = [
		"http://fortune.com/fortune500/"
	]


	def parse(self, response):
		filename = response.url.split("/")[-2] + '.html'
		soup = BeautifulSoup(response.body, "lxml")
		prettyText = soup.prettify()
		with open(filename, "wb") as f:
			f.write(response.body)
		
		companiesListElements = soup.find_all("li", class_="company-list-item")
		for company in companiesListElements:
			companyItem = FortuneCompanyItem()
			companyItem["rank"] = company.find("span", class_="ranking").get_text().replace(".","")
			print company.find("span", class_="ranking").get_text().replace(".","")
			#print company.find("img", class_="company-list-thumbnail").get_text()
			print company.find("span", class_="company-name").get_text()
			mktData =  company.find("span", class_="company-list-mkt-data").get_text()
			ticker = re.findall("[a-zA-Z]+", mktData)
			print ticker
			print company.find("li", class_="company-location").get_text()
			print company.find("li", class_="company-industry").get_text()



