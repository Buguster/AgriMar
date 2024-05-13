from openai import OpenAI 
chatbot = OpenAI()

chat = [{"role": "system", "content": "You are an agriculture expert who answer farmer's questions such as crops types and the weather and all the types of questions that can improve their cultivation based on the region"}]

def CustomChatBot(user_input):
    chat.append({"role": "user" , "content": user_input})
    response = chatbot.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat
    )
    ChatGPT_reply = response.choices[0].message.content
    chat.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply