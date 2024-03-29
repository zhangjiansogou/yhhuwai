from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from spider.items import SpiderItem
from mySpider import getAll, getDomain, getStartURL, getFilter
import json
import os
import uuid
import dboperator

class SpiderSpider(BaseSpider):
	name = "huwai"
	domain = getDomain()
	url = getStartURL()
	allowed_domains = [domain]
	start_urls=[url]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		ff = getFilter()
		sites = hxs.select(ff)
		filters = getAll()
		preurl= getDomain()

		imageitems=[]

		for site in sites:
			item = SpiderItem()
			add = True
			oneItem={}
			db= dboperator.DB()
			for name in item.innerItem:
				exdata  = site.select(filters[name]).extract()
				if len(exdata) == 0:
					add = False
					break
				else:
					if cmp("link", name) == 0 and exdata[0].find("http://") == -1:
						oneItem[name] = "http://"+preurl+exdata[0]
					elif cmp("imageurl", name) == 0 and exdata[0].find("http://") == -1:
						oneItem[name] = {"originurl":"http://"+preurl+exdata[0], "localurl":""}
						item["image_urls"] = oneItem[name]["originurl"]
					elif cmp("place", name) == 0:
						if exdata[0].find("<") != -1:
							place = exdata[0].split(">")	
							place.remove(place[0])
							place.remove(place[0])
							place2=""
							while 1 < len(place):
								place2 += place[0].split("<")[0]
								place.remove(place[0])
							oneItem[name] = place2[5:]
						else:
							oneItem[name] = exdata[0][5:]
					elif cmp("time", name) ==0:
						if exdata[0].find("<") !=-1:
							timestr = exdata[0].split(">")	
							timestr.remove(timestr[0])
							timestr.remove(timestr[0])
							timestr2=""
							while 1 < len(timestr):
								timestr2 += timestr[0].split("<")[0]
								timestr.remove(timestr[0])
							oneItem[name] = timestr2[5:]
						else:
							oneItem[name] = exdata[0][5:]
					elif cmp("hotnumber", name) == 0 and exdata[0].find("<") != -1:	
						hotstr = exdata[0].split(">")	
						hotstr.remove(hotstr[0])
						hotstr.remove(hotstr[0])
						hotstr2=""
						while 1 < len(hotstr):
							hotstr2 += hotstr[0].split("<")[0]
							hotstr.remove(hotstr[0])
						oneItem[name] = hotstr2
					else:
						oneItem[name] = exdata[0]
						

			if add:
				db.save(oneItem)
				imageitems.append(item)
		return imageitems

