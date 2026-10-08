from telegram.ext import Updater,CommandHandler
from telegram import KeyboardButton

def start_func(update,context):
    pass

def main():
    update = Updater(token="adsfkajsdlfasdjf")
    dispatcher = update.dispatcher

    dispatcher.add_handler(CommandHandler("start",start_func))

    update.idle()
    update.start_polling()


if __name__ == "__main__":
    main()