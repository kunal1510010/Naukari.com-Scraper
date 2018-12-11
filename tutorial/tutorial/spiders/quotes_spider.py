import scrapy
import xlwt
from xlwt import Workbook

python_data_analyst = Workbook()
sheet1 = python_data_analyst.add_sheet('Sheet 1', cell_overwrite_ok=True)
list_desig=[]
list_org=[]
list_exp=[]
list_loc=[]
list_skill=[]
list_salary=[]


class JobSpider(scrapy.Spider):
	name = "openings"
	base_url = 'https://www.naukri.com/data-engineer-python-jobs-'
 	start_urls = [
		
		]
	for i in range(0,91):
		url_follow=base_url+str(i)
		start_urls.append(url_follow)
        print(start_urls)
	
	def parse(self, response):
		for row in response.css('div.row'):
			desig=row.css('li.desig::text').extract()
			org=row.css('span.org::text').extract()
			exp=row.css('span.exp::text').extract()
			loc=row.css('span.loc span::text').extract()
			skill=row.css('span.skill::text').extract()
			salary=row.css('span.salary::text').extract()


			for i in desig:
				list_desig.append(i)
			for i in org:
				list_org.append(i)
			for i in exp:
				list_exp.append(i)
			for i in loc:
				list_loc.append(i)
			for i in skill:
				list_skill.append(i)
			for i in salary:
				list_salary.append(i)

		sheet1.write(0, 0, 'Designation')
		sheet1.write(0, 1, 'Organization')
		sheet1.write(0, 2, 'Experience')		
		sheet1.write(0, 3, 'Location')
		sheet1.write(0, 4, 'Skills')
		sheet1.write(0, 5, 'Salary')
		
		for i in range(1,len(list_skill)):
			sheet1.write(i, 0, list_desig[i])
			sheet1.write(i, 1, list_org[i])
			sheet1.write(i, 2, list_exp[i])
			sheet1.write(i, 3, list_loc[i])
			sheet1.write(i, 4, list_skill[i])
			sheet1.write(i, 5, list_salary[i])	

		python_data_analyst.save('data_engineer_python.xls')
		
