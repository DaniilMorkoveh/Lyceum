import vk_api
import urllib
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from googletrans import Translator
import wikipedia

smesharik = ["Крош, Ежик, Нюша, Бараш, Совунья, Кар-Карыч, Пин, Копатыч, Лосяш, Биби"]


def main():
    vk_session = vk_api.VkApi(token='TOKEN')

    longpoll = VkBotLongPoll(vk_session, '204603779')

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])

            if event.obj.message['text'].startswith('!help'):
                vk.messages.send(user_id=event.obj['message']['from_id'],
                                 message="Команды: \n !smesharik - каков ты смешарик\n "
                                         "!h or t - орел или решка\n"
                                         "!trans - перевести\n"
                                         "!wiki (title) - страница википедии\n"
                                         "!group - ссылку на группу",
                                 random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].startswith('!h or t'):
                answer = random.randint(1, 2)
                if answer == 1:
                    answer = 'Head!!!'
                else:
                    answer = "Tails!!!"
                if event.from_user:
                    vk.messages.send(user_id=event.obj['message']['from_id'],
                                     message=f"{answer}",
                                     random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].startswith('!smesharik'):
                rand = random.randint(0, 9)
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"{smesharik[rand]}",
                                 random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].startswith('!group'):
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message='https://vk.com/public204603779',
                                 random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].startswith('!trans'):
                trw = event.obj.message['text'][6:]
                translator = Translator()
                trw2 = translator.translate(trw, dest='ru').text
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=trw2,
                                 random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].startswith('!wiki'):
                wikipedia.set_lang('ru')
                page = wikipedia.page(wikipedia.search(event.obj.message['text'][6:])[0])
                wk = f'{page.title}\n{page.content[:400]}\n\n{page.url}'
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=wk,
                                 random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Для вызова списка команд напишите !help",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
