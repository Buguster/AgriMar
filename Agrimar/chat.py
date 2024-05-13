import requests
from openai import OpenAI
chatbot = OpenAI()

chat = [{"role": "system", "content": "You are an agriculture expert who answer farmer's questions such as crops types and the weather and all the types of questions that can improve their cultivation based on the region"}]


def CustomChatBot(user_input):
    chat.append({"role": "user", "content": user_input})
    response = chatbot.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat
    )
    ChatGPT_reply = response.choices[0].message.content
    chat.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


def get_weather(lat, lon):
    api_key = "c8c90c9dd99dd912654a8b115e2928bf"
    url = f'https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        return None
