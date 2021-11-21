import os
import telebot
from telebot import types

API_KEY = '2136817468:AAHj-YsAuHMrFWnHdbgaZ2n3kyJ_Yar7iDI'

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['get_info', 'info', 'getinfo'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Yes', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='No', callback_data='no')
    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Do you want to get some info about you?', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_id = types.KeyboardButton('GetGoldPrice')
        item_username = types.KeyboardButton('MY NICKNAME')

        markup_reply.add(item_id, item_username)
        bot.send_message(call.message.chat.id,
            reply_markup = markup_reply
        )

    if call.data == 'no':
        pass


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'MY ID':
        bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
    if message.text == 'MY NICKNAME':
        bot.send_message(message.chat.id, f'Your nickname: {message.from_user.first_name}')

bot.polling()
