#!/usr/bin/python
import threading
import time
import subprocess

class BrokerThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
      print "Starting " + time.ctime(time.time())
      subprocess.call(['sh','/Users/dhananjaysharma/Workspace/webcache/snsclient/client/basic.sh'])      
      print "Exiting " + time.ctime(time.time())

# broker1 = BrokerThread(1, "broker-1")
# broker1.start()
# print "out of loop"

