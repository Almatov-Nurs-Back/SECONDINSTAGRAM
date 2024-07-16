import requests, os
from dotenv import load_dotenv

load_dotenv()

def get_instgaram_conversation():
 url = 'https://graph.facebook.com/v13.0/'
 conversation_url = url + '364595800072411' + '/conversations'
 param = dict()
 param['platform'] = 'instagram'
 param['access_token'] = os.getenv('INSTAGRAM_MARKER')
 response = requests.get(url=conversation_url, params=param)
 response = response.json()
 return(response)

# print(get_instgaram_conversation())

def get_messages(converstaion_id=''):
 url = 'https://graph.facebook.com/v13.0/'
 message_url = url + converstaion_id
 message_param = dict()
 message_param['fields'] = 'messages'
 message_param['access_token'] = os.getenv('INSTAGRAM_MARKER')
 # this will give us all the message_id in the conversation but not the messages directly
 response = requests.get(url=message_url, params=message_param)
 response = response.json()
 # so will get the details of the messages using their message_id
 message_ = []
 # we will traverse through all the message_id and get the data and store it inside a list
 for i in response['messages']['data']:
  #print(i['id'])
 ################################ Get the message information #####################################
  message_url_ = url + i['id']
  message_get_param = dict()
  # this field defines the data you want from the endpoint
  message_get_param['fields'] = 'message,created_time,from,to'
  message_get_param['access_token'] = os.getenv('INSTAGRAM_MARKER')
  message_get_response = requests.get(url =message_url_,params = message_get_param)
  message_get_response = message_get_response.json()
  try:
   sender = message_get_response['from']['username']
   receiver  = message_get_response['to']['data'][0]['username']
   message = message_get_response['message']
   time = message_get_response['created_time']

   response = {'sender': sender,'receiver':receiver,'message':message,'time':time}
   message_.append(response)
  except:
   pass
 return message_

print(get_messages('aWdfZAG06MTpJR01lc3NhZA2VUaHJlYWQ6MTc4NDE0Njc1MjYzMjI1NzU6MzQwMjgyMzY2ODQxNzEwMzAxMjQ0MjU5NjYwMjExNDM5OTY1NjY4'))
