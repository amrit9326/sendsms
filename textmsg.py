import requests
import json

URL = ''

# get request
apiKey=""
secretKey=""
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
	response =sendPostRequest(URL, apiKey,secretKey, 'stage', number, 'senderid',s)
	print (response.text)
