#https://github.com/python-telegram-bot/python-telegram-bot/blob/master/tests/test_chat.py - example
# TODO: 
# - my handler
# - edit msg
# - delete msg
# - logger
# - save example current button
import telebot
import ast
import time
from telebot import types

class Telegram():
    def __init__(self):
        self.version = "0.1"
        self.token = '1836210575:AAEOEdeTr8f5YxkM1yXE_Pv468sRqdtKRaU'
        self.bot = telebot.TeleBot(self.token)

        #max length of key = 9 symbols
        self.stringList = {"file": "Скачать файл", "last_msg": "Последнее сообщение ", "state" : "Состояние терминала"}
        self.crossIcon = u"\u2713"
        self.checkIcon = "✔"    # u"\u2713" GREEN CHECK u"\u2713"
        self.heartIcon = "❤"
        

        @self.bot.message_handler(commands=['start'])
        def start_command(message):
            self.bot.send_message(message.chat.id, "Добро пожаловать!")

        @self.bot.message_handler(commands=['version'])
        def start_command(message):
            self.bot.send_message(message.chat.id, "Версия телеграмм бота " + self.version)
            self.bot.send_message(message.chat.id, "Версия терминала " + str("TODO: add version"))


        @self.bot.message_handler(commands=['file'])
        def start_command(message):
            self.bot.send_document(message.chat.id, open(r'log.xml', 'rb'))

        @self.bot.message_handler(commands=['last_message'])
        def start_command(message):
            with open('meridian_m_log.html', "r") as f:
                last_line = f.readlines()[-1]
                if len(last_line) > 4096:
                    for x in range(0, len(last_line), 4096):
                        self.bot.send_message(message.chat.id, last_line[x:x+4096])
                else:
                    self.bot.send_message(message.chat.id, last_line) 

        @self.bot.message_handler(commands=['test'])
        def handle_command_adminwindow(message):
            self.bot.send_message(chat_id=message.chat.id,
                             text="Выберите комнаду:",
                             reply_markup = self.makeKeyboard(),
                             parse_mode='HTML')

        @self.bot.callback_query_handler(func=lambda call: True)
        def handle_query(call):
            # format call.data ['value', 'download file', 'file']
            if (call.data.startswith("['value'")):
                #print(f"call.data : {call.data} , type : {type(call.data)}")
                #print(f"ast.literal_eval(call.data) : {ast.literal_eval(call.data)} , type : {type(ast.literal_eval(call.data))}")
                valueFromCallBack = call.data[1]
                keyFromCallBack = call.data[2]
                #print(f"1. {call.data} ")
                # ALERT MESSAGE
                self.bot.answer_callback_query(callback_query_id = call.id,
                                      show_alert = True,
                                      text = "Использована " + call.data[1] + " команда") # + keyFromCallBack)

            # format call.data ['key', 'file']
            if (call.data.startswith("['key'")):
                print(f"1. {call.data} ")
                keyFromCallBack = call.data[1]
                del self.stringList[keyFromCallBack]
                self.bot.edit_message_text(chat_id = call.message.chat.id,
                                      text = "Сообщение отредактиповано",
                                      message_id = call.message.message_id,
                                      reply_markup = self.makeKeyboard(),
                                      parse_mode = 'HTML') 

    def makeKeyboard(self):
        markup = types.InlineKeyboardMarkup()

        for key, value in self.stringList.items():
            markup.add(types.InlineKeyboardButton(text = value,
                                                  callback_data = "['value', '" + value + "', '" + key + "']"),
            types.InlineKeyboardButton(text = self.crossIcon,
                                       callback_data = "['key', '" + key + "']"))

        return markup    
    
    def run(self):
        self.bot.polling()


#bot = telebot.TeleBot('1836210575:AAEOEdeTr8f5YxkM1yXE_Pv468sRqdtKRaU')

if __name__ == '__main__':
    Tele = Telegram()
    Tele.run()
    '''
    @bot.message_handler(commands=['start'])
    def start_command(message):
        bot.send_message(message.chat.id, "Hello!")
    bot.polling()
    '''
    