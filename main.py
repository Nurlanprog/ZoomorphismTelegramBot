from telegram import *
from telegram.ext import *

rusCulture = "Русская культура"
japanCulture = "Japan"

negativeJapan={"カメ (черепаха)" : "пьяница", "白いマウス (белая мышь)" : "верный слуга", "ツバメ (ласточка)" : "возлюбленный",
        "コウモリ (летучая мышь)" : "Эгоист ",  " トビ (коршун)": "мелкий воришка", "ねこ (кошечка)": "о женщине ласкового характера",
          "鴨 (дикая утка" : "простак", "蟻 (муравей)" : "трудоголик", "バッタ (кузнечик)": " человек, который стремится получить выгоду за короткое время",
          "秋刀魚 (рыба сайра)": "болтун", "鷹 (сокол)": "мудрый", "烏 (ворона)": "не организованный", "黒猫 (черная кошка)": "мстительный воин",
          "狐 (лиса)": " красивая", "蝶 (бабочка)": "женственность", "鯉 (сазан)" : "усердный", "タ ヌ キ (Енотовидная собака )": "игривый, жизнерадостный",
         "象 (слон)": " интеллектуальный, великий", "クレイン (журавль)": "удачливый", "ライオン (лев)": "властный, сильный", "フクロウ (сова)": "Доброжелательный",
          "トーク (снежная обезьяна)": "мудрый", "鹿 (олень)": "посланник Бога", "トンボ (стрекоза)": "мужественный", "孔雀 (павлин)": "добрый, заботливый",
          " フェニックス (феникс)": "спококойный, гармоничный", "うさぎ (кролик)": "преданный, целеустремленный", "鯛 (морской лещ)": "добрый, позитивный",
        "鴛鴦 (утка-мандаринка)": "гармоничный, красивый", "牛 (корова)": "умный"}


def start(bot, update):
  bot.message.reply_text(main_menu_message(),
                         reply_markup=main_menu_keyboard())

def main_menu(bot, update):
  bot.callback_query.message.edit_text(main_menu_message(),
                          reply_markup=main_menu_keyboard())

def first_menu(bot, update):
  bot.callback_query.message.edit_text(first_menu_message(),
                          reply_markup=first_menu_keyboard())

def second_menu(bot, update):
  bot.callback_query.message.edit_text(second_menu_message(),
                          reply_markup=second_menu_keyboard())

def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

def error(update, context):
    print(f'Update {update} caused error {context.error}')

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Menu 1', callback_data='m1')],
              [InlineKeyboardButton('Menu 2', callback_data='m2')],
              [InlineKeyboardButton('Menu 3', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Choose the option in main menu:'

def first_menu_message():
  return 'rusCulture:'

def second_menu_message():
  return 'japanCulture:'

############################# Handlers #########################################
updater = Updater('token="5015104346:AAHvwHGrGnNiiowkI-7OQbjkCoOY0FEiHy4', use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_1'))
updater.dispatcher.add_error_handler(error)

updater.start_polling()
