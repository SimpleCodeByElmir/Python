from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
from time import sleep

def get_subscribers_count(update: Update, context: CallbackContext) -> None:
    channel_id = ['example1', 'example2', 'example3',
                  'example4', 'example5']  # list of chats

    for i in range(0, len(channel_id)):
        if i == 3:  # fall asleep after getting info about x chats 
            context.bot.send_message(update.message.chat_id, f'Sleeping... wait few seconds')
            sleep(5)  # seconds of sleeping
        try:
            # Get the chat ID of the channel
            chat_id = context.bot.get_chat(channel_id[i]).id

            # Get the number of subscribers
            subscribers_count = context.bot.get_chat_members_count(chat_id)

            context.bot.send_message(update.message.chat_id, f'Current number of subscribers: {subscribers_count}')

        except Exception as e:
            print(f'Error: {e}')
            context.bot.send_message(update.message.chat_id, 'Failed to get subscriber count.')

def main():
    updater = Updater('PUT_YOUR_BOT_TOKEN_HERE', use_context=True)  # TOKEN
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('getsubscribers', get_subscribers_count))

    # Add a button to the main menu
    main_menu_keyboard = [[KeyboardButton('/getsubscribers')]]
    reply_markup = ReplyKeyboardMarkup(main_menu_keyboard, resize_keyboard=True)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
