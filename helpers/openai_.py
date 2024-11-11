import os
from openai import OpenAI
from helpers.messages import get_messages

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = dict()

def generate_chatgpt_answer(sender_id='', prompt=''):
  # # ----- Code with ChatGPT -----
  # if sender_id not in messages:
  #   messages[sender_id] = get_messages(sender_id)
  #   print(messages)
  #   pass
  # print(sender_id)
  # # -----------------------------

  chat_completion = client.chat.completions.create(
    messages=[
      {
        "role": "system",
        "content": "Ты ассистент отдыхного пансионата Иссык-Куле, юрточного городка \"Asman-Resort\". Ты консультируешь туристов, которые интересуятся отдыхм у нас.",
      },
      # # ----- Code with ChatGPT -----
      # *messages[sender_id],
      # # -----------------------------
      {
        'role': 'user',
        'content': prompt
      }
    ],
    model="gpt-3.5-turbo-0125",
    max_tokens=1000,
  )
  return chat_completion.choices[0].message.content

  # # ----- Code for testing -----
  # if 'Привет' in prompt or 'привет' in prompt:
  #   return 'Приветствую'
  # elif 'Досвидание' in prompt or 'пока' in prompt:
  #   return 'Всего доброго'
  # elif 'кто ты' in prompt or 'Чем вы занимаетесь' in prompt or 'чем вы занимаетесь' in prompt:
  #   return 'Я ai ассистент из "..." компании!'

  # return prompt
  # # ----------------------------

print(generate_chatgpt_answer(sender_id='1198676774465284', prompt='Чем вы занимаетесь?'))
