from telebot import TeleBot
from telebot import types
from dotenv import load_dotenv
import sqlite3
import random
import os

load_dotenv()
bot = TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=["start", "help"])
def beginning (message):
    bot.reply_to(message, f'<strong>Hello! I am Tricky Cat. I make riddles for children and adults. To get a riddle from me, just ask me about it in a message. You can write your request however you like - I am  a smart bot, and I will understand what you want.</strong>', parse_mode='html')

@bot.message_handler(content_types=["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact", "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo","group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id", "migrate_from_chat_id", "pinned_message"])
def dont_send(message):
    bot.reply_to(message, f'<strong>Meow! I can read only text!</strong>', parse_mode='html')


@bot.message_handler()
def riddle(message):
    r_number = random.choice(range(1, 25))
    stroka_dliy_sql = str('SELECT * FROM riddles WHERE id ='+' '+str(r_number))
    conn = sqlite3.connect('riddles_base_eng.sql')
    cur = conn.cursor()
    cur.execute(stroka_dliy_sql)
    otvet_iz_sql = cur.fetchall()
    soobshenie = list(otvet_iz_sql[0])
    soobshenie_s_zagadkoy = soobshenie[1]
    otvet_na_zagadku = soobshenie[2]
    cur.close()
    conn.close()
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Find out the correct answer and close the riddle', callback_data= otvet_na_zagadku))
    if 'riddl' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'want' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'more' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'one' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'get' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'give' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'talk' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'write' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'talk' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'yes' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'next' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'keep' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    elif 'propose' in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>{soobshenie_s_zagadkoy}</strong>', reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, answer, otvet_na_zagadku)
    else:
        bot.reply_to(message, f"<strong>Meow? I propose riddles, ask me...  </strong>", parse_mode='html')
def answer(message, otvet_na_zagadku):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Find out the correct answer and close the riddle', callback_data=otvet_na_zagadku))
    if otvet_na_zagadku in message.text.lower():
        bot.send_message(message.chat.id, f'<strong>Correct answer! Ask me to tell you the next riddle!</strong>', parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'<strong>Incorrect answer!</strong>', reply_markup = markup, parse_mode='html')
        bot.register_next_step_handler(message, answer,otvet_na_zagadku)


@bot.callback_query_handler(func=lambda callback: True)
def loos(callback):
    porazhenie = callback.data
    if callback.data:
        bot.send_message(callback.message.chat.id, f'<strong>Correct answer: {porazhenie}</strong>', parse_mode='html')
        bot.clear_step_handler_by_chat_id(callback.message.chat.id)


bot.infinity_polling(timeout=10, long_polling_timeout = 5)
