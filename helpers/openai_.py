import os
from openai import OpenAI
from helpers.messages import get_messages

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = dict()

def generate_chatgpt_answer(sender_id='', prompt=''):
  if sender_id not in messages:
    messages[sender_id] = get_messages(sender_id)

  chat_completion = client.chat.completions.create(
    messages=[
      {
        "role": "system",
        "content": "Ты ассистент отдыхного пансионата Иссык-Куле, юрточного городка \"Asman-Resort\". Ты консультируешь туристов, которые интересуятся отдыхм у нас.",
      },
      *messages[sender_id],
      {
        'role': 'user',
        'content': prompt
      }
    ],
    model="gpt-4o-mini",
    max_tokens=1000,
  )
  return chat_completion.choices[0].message.content
