# Scrapy settings for spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'spider'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = ['spider.imagepipelines.ImagesPipelines']
IMAGES_STORE = '/home/shawn/workstation/yhhuwai/pitchdata/static/'
IMAGES_EXPIRES = 1
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
#ITEM_PIPELINES = [
#    'spider.pipelines.SpiderPipeline'
#]


