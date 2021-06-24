
import telebot

class Telegram():
    def __init__(self):
        self.token = '1234567890:AAE_abCDEFghijKLmNOpqRsTuVWxyz'
        self.bot = telebot.TeleBot('1836210575:AAEOEdeTr8f5YxkM1yXE_Pv468sRqdtKRaU')
    
    @bot.message_handler(commands=['start'])
    def start_command(self, message):
        bot.send_message(message.chat.id, "Hello!")
    
    def run(self):
        self.bot.polling()


bot = telebot.TeleBot('1836210575:AAEOEdeTr8f5YxkM1yXE_Pv468sRqdtKRaU')

if __name__ == '__main__':
    @bot.message_handler(commands=['start'])
    def start_command(message):
        bot.send_message(message.chat.id, "Hello!")
    bot.polling()
