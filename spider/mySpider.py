def getList():
	name = MySpider("crawlItems.cfg")
	return name.getNameList() 
 
def getAll():
	allP = MySpider("crawlItems.cfg")
	return allP.getSettingsList()

def getDomain():
	allP = MySpider("crawlItems.cfg")
	return allP.getDomains()

def getStartURL():
	url = MySpider("crawlItems.cfg")
	return url.getStartUrls()

def getFilter():
	ff = MySpider("crawlItems.cfg")
	return ff.getFilter()

class MySpider:
        def __init__(self, path):
		self.path = path
		self.list = {}
		self.name = []
		self.url = []
		self.domains=""
		self.start_urls=""
		self.filter=""
		self.openCrawlItems()
        
        def addToList(self, name, url):
            self.list[name] = url
            self.name.append(name)
            self.url.append(url)
	
	def getFilter(self):
		return self.filter

	def getDomains(self):
		return self.domains

	def getStartUrls(self):
		return self.start_urls

        def getSettingsList(self):
            return self.list
        
        def getNameList(self):
            return self.name
        
        def getUrlList(self):
            return self.url
        
        def openCrawlItems(self):
            self.file = file(self.path)
            while True:
                line = self.file.readline()                 
                if len(line) == 0 or len(line) == 1:
			break
		else:
			first=line.split('"')[0].split("=")[0]
			second=line.split('"')[1]
			if cmp(first, "allowd_domains") == 0:
				self.domains=second
			elif cmp(first, "start_urls") == 0:
				self.start_urls=second
			elif cmp(first, "filter") == 0:
				self.filter=second
			else:
				self.addToList(first, second)
            self.closeCrawlItems()

        def closeCrawlItems(self):
            self.file.close()       
            

