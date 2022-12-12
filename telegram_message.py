import requests
import time

def send_to_telegram(message):
    apiToken = '5554722719:AAENZZTxOITqaXzeyBDp3OIyAxaGI6N-VRo'
    chatID = '1270782866'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

x = int()
while True:
    send_to_telegram("иди на хуй")
    x += 1
    time.sleep(300)

print(x)
