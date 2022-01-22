from telegram import *
from telegram.ext import *
import requests
from bs4 import BeautifulSoup

updater = Updater(token="5015104346:AAHvwHGrGnNiiowkI-7OQbjkCoOY0FEiHy4")
dispatcher = updater.dispatcher

rusCulture = "Русская культура"
otherCultures = "Казахская и английская культура"

#responces
response = requests.get('https://Nurlanprog.github.io/').text
#soup
soup = BeautifulSoup(response, 'html.parser')

def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(otherCultures)], [KeyboardButton(rusCulture)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать на справочник зооморфизмов!",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def messageHandler(update: Update, context: CallbackContext):
    if rusCulture in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=soup.find("div", attrs={"class": "russian"}).text)
    if otherCultures in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=soup.find("div", attrs={"class": "others"}).text)



dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()