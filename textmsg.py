import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
apiKey="1ZBYLLHWBUQ11QFMJUD4F3GPL4HZ1LLC"
secretKey="F6F30X3EV6WO9854"
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
number=input("Enter Number:")
while True:
	
	s=input("Enter Message :")
	response =sendPostRequest(URL, apiKey,secretKey, 'stage', number, '9125183799',s)
	print (response.text)
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
    