import telebot
from telebot import types

def main_key():
    key = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    btn1 = types.KeyboardButton(text="🏠")
    btn2 = types.KeyboardButton(text="🔎")
    btn3 = types.KeyboardButton(text="⁉️")
    btn4 = types.KeyboardButton(text="➕")
    btn5 = types.KeyboardButton(text="👤")
    key.add(btn1,btn2,btn3,btn4,btn5)
    return key