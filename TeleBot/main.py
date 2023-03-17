from extensions import *
import telebot
from telebot import types
import os

# Создаем файл с нашим токеном. В классе BotToken описана функция для записи токена.
# Данное решение обусловлено простым использованием для конечного пользователя без необходимости лезть в код.

def Settings():

    #При наличии файла функция пропускается
    # Проверяем существует ли файл с токеном, если да, то продолжаем, в другом случаи создаем.
    print("Здравствуй, пользователь!\nДля работы с ботом необходимо произвести первоначальные настройки")
    inits = input('Ввведи токен бота, которого ты создал до того как запустить программу :3: ')
    user_input = BotToken(inits)
    BotToken.saving(user_input)
    print("Вот и все хех :)\nТеперь текен для данного бота активен всегда.\nНо его всегда можно поменять!\n")


def main():

    # Функция перезаписи файла с токеном
    def resave():
        if os.path.isfile("Settings.txt"):
            os.remove("Settings.txt")
            Settings()
    
    # Условие при каждом включении программы для возможной замены токена при работе с разными ботами
    if os.path.isfile("Settings.txt"):
        quest = input("Здравстуйте снова! Хотите поменять токен?: Да/Нет ")

        if quest == "Да":
            resave()

    else:
        Settings()

    # Инициализируем нашего бота дав ему входные данные для работы.
    setup = open('Settings.txt', 'r')
    token = setup.readline()
    bot=telebot.TeleBot(token)

    # Стандартное приветствие для /start и помощь для /help
    @bot.message_handler(commands = ['start', 'help'])
    def help(message):
        
        if message.text == "/start":
            bot.send_message(message.chat.id, f'Здравствуй, {message.chat.username}, для дальнейшей работы используй комманду /values!')
        
        elif message.text == "/help":
            bot.send_message(message.chat.id, "В данном боте вы можете конвертировать валюты с актуальными ценами.\nДля конвертации доступны 3 валюты USD, EUR, RUB")
            bot.send_message(message.chat.id, "Пример конвертации: rub, usd, 10. Где первое значение это валюта из которой переводим, второе в которую и третье значение какое каличество валюты")


    # Функция описывающая вывод кнопок с валютами для дальнейших манипуляций
    # Для добавление новых кнопок использовать её
    @bot.message_handler(commands = ['values'])
    def values(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Конвертация валюты')
        markup.add(item1)
        bot.send_message(message.chat.id, "Для конвертации доступные такие валюты как: EUR, USD, RUB.\nЧтобы начать работу нажмите кнопку 'Конвертация валюты'. ", reply_markup = markup)


    #Функция, в которой принимаем значения пользователя и форматируем полученный словарь для читабельности и пустить данные в класс Req для работы с API
    @bot.message_handler(content_types = 'text')
    def values_message(message):

        if message.text == "Конвертация валюты":
            bot.send_message(message.chat.id, 'Введите валюту из которой конвертировать, в которую конвертировать и кол-во для конвертации через запятую\nДоступные валюты: EUR, USD, RUB')
       
        a = message.text
        f = a.split(',')
        
       # Конвертируем список удаляя пробелы и меняя точки на запятые для коректной работы
        if len(f) == 3:      
            result = Req.get_price(f[0].replace(' ','').upper(),f[1].replace(' ','').upper(),f[2].replace('.',',').replace(' ','').upper())
            bot.send_message(message.chat.id, f"Результат: {result} {f[1]}")

    bot.infinity_polling()


if __name__ == "__main__":
    main()
