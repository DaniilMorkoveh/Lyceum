from flask import Flask, request
import logging
import json
import random
import requests

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


class Weather():
    def __init__(self, city):
        self.API = 'api_n'
        self.req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.API}')

    def info(self):
        if self.req.status_code == 500:
            return 'Something is wrong'
        else:
            weather1 = self.req.json()
            print(weather1)
            return (f'{weather1["name"]}, {weather1["sys"]["country"]}: '
                    f'{weather1["main"]["temp"]}*F, {weather1["weather"][0]["main"]}')


@app.route('/', methods=['POST'])
def main():
    logging.info(f'Request: {request.json!r}')
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info(f'Response: {response!r}')
    return json.dumps(response)


def handle_dialog(res, req):
    user_id = req['session']['user_id']

    if req['session']['new']:
        res['response']['text'] = 'Please, print your nickname'
        return

    else:
        for entity in req['request']['nlu']['tokens']:
            city = entity
        wwther = Weather(city)
        wwinfo = wwther.info()
        res['response']['text'] = wwinfo


if __name__ == '__main__':
    app.run()
