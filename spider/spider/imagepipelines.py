# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import dboperator

class ImagesPipelines(ImagesPipeline):
	def get_media_requests(self, item, info):
		#for image_url in item['image_urls']:
		yield Request(item['image_urls'])

	def item_completed(self, results, item, info):
		db= dboperator.DB()
		
		image_paths = [x['path'] for ok, x in results if ok]	
		if not image_paths:
			raise DropItem("Item contains no images")
		item['image_paths'] = image_paths

		db.update({"imageurl":{"originurl":item['image_urls'],"localurl":image_paths[0]}}, {"imageurl":{"originurl":item['image_urls'],"localurl":""}})

		return item
