import os
import openai
from helpers.messages import get_messages

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not set in environment variables.")

client = openai

messages = dict()

def generate_chatgpt_answer(sender_id='', prompt=''):
  if sender_id not in messages:
    messages[sender_id] = get_messages(sender_id)

  print(messages[sender_id])

  chat_completion = client.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
      {
        "role": "system",
        "content": "Ты ассистент отдыхного пансионата Иссык-Куле, юрточного городка \"Asman-Resort\". Ты консультируешь туристов, которые интересуятся отдыхом у нас.",
      },
      *messages[sender_id],
      {
        'role': 'user',
        'content': prompt
      }
    ],
    max_tokens=1000,
  )
  return chat_completion.choices[0].message.content
