import requests, os
from flask import Flask, request
from dotenv import load_dotenv
from helpers.openai_ import generate_chatgpt_answer


load_dotenv()
app = Flask(__name__)

VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
INSTAGRAM_MARKER = os.getenv('INSTAGRAM_MARKER')

@app.route('/', methods=['GET'])
def verify():
  if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == VERIFY_TOKEN:
    return request.args.get('hub.challenge'), 200
  return 'Verification token mismatch', 403

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  if data['object'] == 'instagram':
    for entry in data['entry']:
      for message in entry['messaging']:
        if message.get('message'):
          text = message['message'].get('text')
          sender_id = message['sender']['id']
          generated_answer = generate_chatgpt_answer(sender_id=sender_id, question=text)
          print(generated_answer)
          send_message(sender_id, generated_answer)
  return 'OK', 200

# @app.route('/oauth', methods=['GET'])
# def authentication():
#   return render_template('templates/oauth.html')

def send_message(recipient_id, text):
  url = f"https://graph.facebook.com/v12.0/me/messages?access_token={INSTAGRAM_MARKER}"
  headers = {'Content-Type': 'application/json'}
  payload = {
    'recipient': {'id': recipient_id},
    'message': {'text': text}
  }
  requests.post(url, headers=headers, json=payload)

if __name__ == '__main__':
  app.run(debug=True)
