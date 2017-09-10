# -*- coding: utf-8 -*-
# @Author: dhananjaysharma
# @Date:   2017-09-08 15:27:28
# @Last Modified by:   dhananjaysharma
# @Last Modified time: 2017-09-08 17:54:59
import threading

class BrokerThread(threading.Thread):
	
	def __init__(self,threadId,threadName):
		threading.Thread.__init__(self)
		self.threadId=threadId
		self.threadName=threadName

	def run(self):
		print "data"
		pass