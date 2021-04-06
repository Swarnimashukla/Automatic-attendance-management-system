import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
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

def sms(name,mobileno,subjectname):
  response = sendPostRequest(URL, '18Q54I39P0TBAK53Z5G4M26XU5DL1KMU', '7R2M2FZP75LXZ380', 'stage', '+91'+mobileno, 'suyash.gautam97@gmail.com', 'Your ward '+ name +' was present in '+subjectname+' lecture' )
  print(response.text)
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want


