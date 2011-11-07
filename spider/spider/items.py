# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from mySpider import getList

class SpiderItem(Item):
    # define the fields for your item here like:
	innerItem={}
	namelist = getList()
	for item in namelist:
		innerItem[item] = Field()
