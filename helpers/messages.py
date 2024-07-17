import requests, os
from dotenv import load_dotenv

load_dotenv()


username = 'test51877'
page_id = '364595800072411'
url = 'https://graph.facebook.com/v20.0/'
page_access_token = os.getenv('INSTAGRAM_MARKER')

def get_instagram_id(instagram_user_id=''):
 conversation_url = url + page_id + '/conversations'
 param = dict()
 param['platform'] = 'instagram'
 param['access_token'] = page_access_token
 param['user_id'] = instagram_user_id
 response = requests.get(url=conversation_url, params=param)
 response = response.json()
 return response['data'][0]['id']

def get_messages_using_conversation_id(converstaion_id=''):
 message_url = url + converstaion_id
 message_param = dict()
 message_param['fields'] = 'messages'
 message_param['access_token'] = page_access_token
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
  message_get_param['fields'] = 'message,from'
  message_get_param['access_token'] = page_access_token
  message_get_response = requests.get(url =message_url_,params = message_get_param)
  message_get_response = message_get_response.json()
  try:
   sender = message_get_response['from']['username']
   message = message_get_response['message']

   response = {'role': 'user' if sender == username else 'assistant','content': message}
   message_.append(response)
  except:
   pass
 return message_

def get_messages(sender_id=''):
  return get_messages_using_conversation_id(get_instagram_id(sender_id))
