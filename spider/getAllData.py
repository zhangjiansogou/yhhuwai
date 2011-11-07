
import os

filed=open("./all.cfg", "r")
content =filed.readlines()
length=len(content)

loopURL=[]
cfg=[]
for i in range(0, length):
	name=content[i].split("=")[0]
	if i==0:
		cfg.append(content[i])
	else:
		if len(content[i]) < 2:
			for p in range(0, len(loopURL)):
				cfgfile=open("./crawlItems.cfg", "wb")
				for q in range(0, len(cfg)):
					cfgfile.write(cfg[q])
				cfgfile.write(loopURL[p])
				cfgfile.close()
				os.system("scrapy crawl huwai")
			cfg=[]
			loopURL=[]
		elif cmp(name, "start_urls") == 0:
			loopURL.append(content[i])
		else:
			cfg.append(content[i])
			if (i+1) == length:
				for j in range(0, len(loopURL)):
                                	cfgfile=open("./crawlItems.cfg", "wb")
                                	for k in range(0, len(cfg)):
                                        	cfgfile.write(cfg[k])
                                	cfgfile.write(loopURL[j])
                                	cfgfile.close()
					os.system("scrapy crawl huwai")
				cfg=[]
				loopURL=[]

#os.system("rm crawlItems.cfg")
	

