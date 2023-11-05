import telebot
bot = telebot.TeleBot('6406833297:AAGeLwDSxMcxffItP6KwNcGYJCaaE_P4Tmg')
@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')

bot.infinity_polling()