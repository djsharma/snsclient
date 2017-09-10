# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from broker import BrokerThread
import subprocess

def handle_subscribe( request ):
	print "in subscribe"
	try:
		body = json.loads(request.body)
		resp = requests.get(body["SubscribeURL"]) 
	except Exception as e:
		raise Exception( "Error in Subscription" + str(e))

def handle_msg( request):
	try:
		body = json.loads(request.body)
		print body
		broker1 = BrokerThread(1, "broker-1")
		broker1.start()
		return
	except Exception as e:
		raise Exception( "Error in handle_msg" + str(e))

def handle_unsubscribe( request):
	try:
			body = json.loads(request.body)
			print body

	except Exception as e:
		raise Exception( "Error in handle_unsubscribe" + str(e))


function = {
			 'SubscriptionConfirmation': handle_subscribe,
			 'Notification': handle_msg,
			 'UnsubscribeConfirmation': handle_unsubscribe,		
}

# Create your views here.
def handle_notification( request ):
	print request.method
	if request.method =='POST':
		try:
			header = request.META
			print request.META
			msg_type = request.META['HTTP_X_AMZ_SNS_MESSAGE_TYPE']
			function[msg_type](request)
			return HttpResponse(status=200)
		except Exception as e:
			print "Request not processed", str(e)
			return HttpResponse(status=500)
	else:
		print "GET not served"
		return HttpResponse(status=500)
