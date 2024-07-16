import requests, os
from dotenv import load_dotenv

load_dotenv()

def get_conversations(access_token, instagram_business_account_id):
  url = f"https://graph.facebook.com/v12.0/{instagram_business_account_id}/conversations"
  params = {
    'access_token': access_token
  }
  response = requests.get(url, params=params)
  return response.json()

def get_messages(access_token, conversation_id):
  url = f"https://graph.facebook.com/v12.0/{conversation_id}/messages"
  params = {
    'access_token': access_token
  }
  response = requests.get(url, params=params)
  return response.json()

access_token = os.getenv('INSTAGRAM_MARKER')
instagram_business_account_id = "364595800072411"

conversations = get_conversations(access_token, instagram_business_account_id)
print(conversations)

# for conversation in conversations['data']:
#   conversation_id = conversation['id']
#   messages = get_messages(access_token, conversation_id)
#   print(f"Messages for conversation {conversation_id}:", messages)
