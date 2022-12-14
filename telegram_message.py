import requests
import time

def send_to_telegram(message):
    apiToken = ''
    chatID = ''
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

x = int()
while True:
    send_to_telegram("")
    x += 1
    time.sleep(300)

print(x)
