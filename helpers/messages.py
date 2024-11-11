import requests, os, asyncio
from dotenv import load_dotenv
import aiohttp

load_dotenv()

username = 'test51877'
page_id = '364595800072411'
url = 'https://graph.facebook.com/v20.0/'
page_access_token = os.getenv('INSTAGRAM_MARKER')

def get_instagram_id(instagram_user_id=''):
  conversation_url = url + page_id + '/conversations'
  param = {
    'platform': 'instagram',
    'access_token': page_access_token,
    'user_id': instagram_user_id
  }
  response = requests.get(url=conversation_url, params=param).json()

  # Проверяем, есть ли 'data' в ответе
  if 'data' in response and response['data']:
    return response['data'][0]['id']
  else:
    # Возвращаем None или выбрасываем ошибку, если нет данных
    print("No data found for the given instagram_user_id")
    return None

async def fetch_message(session, message_id):
    message_url = url + message_id
    params = {
      'fields': 'message,from',
      'access_token': page_access_token
    }
    async with session.get(message_url, params=params) as response:
        return await response.json()

async def get_messages_using_conversation_id(conversation_id):
  message_url = url + conversation_id
  params = {
    'fields': 'messages',
    'access_token': page_access_token
  }

  async with aiohttp.ClientSession() as session:
    async with session.get(message_url, params=params) as response:
      data = await response.json()
      message_ids = [msg['id'] for msg in data.get('messages', {}).get('data', [])]

      tasks = [fetch_message(session, message_id) for message_id in message_ids]
      messages_data = await asyncio.gather(*tasks)

  messages = []
  for message_data in messages_data:
    try:
      sender = message_data['from']['username']
      message = message_data['message']
      response = {
        'role': 'user' if sender == username else 'assistant',
        'content': message
      }
      messages.append(response)
    except KeyError:
      continue

  return messages

def get_messages(sender_id=''):
  conversation_id = get_instagram_id(sender_id)
  if conversation_id is None:
    return []  # или лог ошибки
  messages = asyncio.run(get_messages_using_conversation_id(conversation_id))
  return messages