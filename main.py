import telebot
import openai

bot_key = '6646836348:AAEeKFdyHa9r4zWYyM91TB_SYWx99cKqb3Q'
openai.api_key = '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'

bot = telebot.TeleBot(bot_key)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, я твой GPT бот. Готов тебе помочь!')

@bot.message_handler(content_types=['text'])
def main(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message.text,
        max_tokens=150,
        temperature=0.7,
        stop=None,
    )
    if response and response.choices:
        reply = response.choices[0].text.strip()
    else:
        reply = 'Ой что-то не так'
    bot.send_message(message.chat.id, reply)

bot.polling(none_stop=True)