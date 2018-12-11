import scrapy
import xlwt,open_workbook
from xlrd import open_workbook

indeed_data_analyst = Workbook()
sheet1 = indeed_data_analyst.add_sheet('Sheet 1', cell_overwrite_ok=True)

next_follow=[]

class JobSpider(scrapy.Spider):
	name = "indeed"
	base_url = 'https://www.indeed.co.in/jobs?q=data+analyst&start='
 	start_urls = [
		
		]
	for i in range(0,99):
		url_follow=base_url+str((i*10))
		start_urls.append(url_follow)
	
	def parse(self, response):
		for row in response.css('h2.jobtitle'):
			follow_link = row.css('a::attr(href)').extract()
			for i  in follow_link:
				next_follow.append(i)			
		for i in range(0,len(next_follow)):
			sheet1.write(i, 0, next_follow[i])	

		indeed_data_analyst.save('indeed_url_follow.xls')

class FollowUp(scrapy.Spider):
	name="follow"
	base_url = 'https://www.indeed.co.in/'
	
	start_url=next_follow
	print start_url
	
	def parde(self,response):
		for row in response.css('div.jobsearch-JobInfoHeader-title'):
			print row
		
