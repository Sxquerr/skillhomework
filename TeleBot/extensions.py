import requests
import json

class BotToken:

    _token = None

    def __init__(self, token):
        self.token = token

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, text):
        if text is None:
            raise TypeError("Вы не ввели токен!")  
        else:
            self._token = text

    def saving(self):
        print('Creating new file')
        file = open('Settings.txt', 'w')
        file.write(f"{self.token}")
        file.close()
        print('File is created')
    
    def config(self):
        return self.token
    
class Req:

    @staticmethod
    def get_price(base,quote,amount):
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}')
        result = json.loads(r.content)
        x = result.get(quote)
        try:
            sum = float(x) * float(amount)
            return round(sum, 3)
        except APIException as e:
            print('e')

class APIException(Exception):
    
    def __str__(self):
        return "Вы ввели не верные данные"
    