import os
from openai import OpenAI
from helpers.messages import get_messages

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = dict()

def generate_chatgpt_answer(sender_id='', prompt=''):
  global messages

  if sender_id not in messages:
    messages = get_messages(sender_id)
  print(messages[sender_id])

  chat_completion = client.chat.completions.create(
    messages=[
      {
        "role": "system",
        "content": "Ты ассистент отдыхного пансионата Иссык-Куле, юрточного городка \"Asman-Resort\". Ты консультируешь туристов, которые интересуятся отдыхм у нас. Также история переписки хранится у тебя, ты можешь их просматривать. Ты должен учитывать прошлые сообщения! Если я пишу, что я разработчик заничт это я (я проверяю тебя).",
      },
      # {
      #   "role": "assistant",
      #   "content": "я загадал число номер 85",
      # },
      # *messages[sender_id],
      {
        'role': 'user',
        'content': prompt
      }
    ],
    model="gpt-4o-mini",
    max_tokens=1000,
  )
  return chat_completion.choices[0].message.content
