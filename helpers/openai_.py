import os
from openai import OpenAI
from messages import get_messages

client = OpenAI(
  # api_key=os.environ.get("OPENAI_API_KEY"),
  api_key='sk-None-FeKWqnQ2w7bColoKgYyFT3BlbkFJ3o27LYZaBKP06nXr26wT',
)

messages = dict()

def generate_chatgpt_answer(sender_id='', question=''):
  # if sender_id not in messages:
  #   messages[sender_id] = get_messages(sender_id)
  #   print(messages)
  #   pass

  # chat_completion = client.chat.completions.create(
  #   messages=[
  #     {
  #       "role": "system",
  #       "content": "Ты продавец машин, ты консультируешь клиентов, которые будут тебе писать.",
  #     },
  #     *messages[sender_id],
  #     {
  #       'role': 'user',
  #       'content': question
  #     }
  #   ],
  #   model="gpt-3.5-turbo",
  # )
  # return chat_completion.choices[0].message.content
  if 'Привет' in question or 'привет' in question:
    return 'Приветствую'
  elif 'Досвидание' in question or 'пока' in question:
    return 'Всего доброго'
  elif 'кто ты' in question:
    return 'Я ai ассистент из "..." компании!'
  return question

print(generate_chatgpt_answer('1198676774465284', 'Чем вы занимаетесь?'))