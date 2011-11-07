import pymongo

class Dboperator:
	def __init__(self):
		self.dbase = pymongo.Connection().items_database
#	def counter(self):
 #  		 ret = db.counters.findAndModify({query:{_id:"information"}, update:{$inc : {next:1}}, "new":true, upsert:true})
#		return ret.next

	def putDatatoBase(self, data):
		self.dbase.information.insert(data)
	def getDatafromBase(self, data):
		return self.dbase.information.find(data)		
	def getAllDatafromBase(self):
		try:
			rvalue = self.dbase.information.find()
		except:
			print "Exception happens when finding."

		return rvalue
	def removeDatafromBase(self, data):
		try:
			self.dbase.information.remove(data)
		except:
			print "Exception happens when removing."

