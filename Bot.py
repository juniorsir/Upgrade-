from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to handle messages
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response['choices'][0]['message']['content']
        # Send reply to the user
        update.message.reply_text(bot_reply)
    except Exception as e:
        update.message.reply_text("An error occurred: " + str(e))

# Main function to start the bot
def main():
    # Set your Telegram bot token
    TELEGRAM_TOKEN = "7994516956:AAGDjQ_MlujhqmuFN458F5xqQ34S8PQbkbM"

    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
