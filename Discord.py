import discord
import asyncio
import random
import requests
import googletrans
from googletrans import Translator
import os
import wikipedia

TOKEN = os.environ.get('BOT_TOKEN')


class Bot(discord.Client):

    async def on_ready(self):
        print(f'{self.user} подключён к Discord')
        for guild in client.guilds:
            print(
                f'{client.user} подключился к каналу:\n'
                f'{guild.name} (id: {guild.id})'
            )
        self.ln_src = 'ru'
        self.ln_dest = 'en'

    async def on_message(self, message):
        if message.content.startswith("!help"):
            await message.channel.send('''List of commands:
             !heads or tails - one of two things
             !time (number 1) h (number 2) m - set timer
             !trans - translation from source to destination
             !change - changing source or destination
             !wiki (title) - show wikipedia page''')
        if message.content.startswith("!time"):
            h, m = int(message.content.split()[1]), int(message.content.split()[3])
            await message.channel.send(f'{str(client.get_emoji(748200364351815852))} Timer set to go off in {h} hours and {m} minutes')
            await asyncio.sleep(h * 3600 + m * 60)
            await message.channel.send(
                f"The timer went off {str(client.get_emoji(748200275600212028))}")
        if message.content.startswith("!head or tails"):
            answer = random.randint(1, 2)
            if answer == 1:
                answer = 'Head!!!'
            else:
                answer = "Tails!!!"
            await message.channel.send("Get ready")
            await asyncio.sleep(3)
            await message.channel.send(f"{answer}")
        if message.content.startswith('!trans'):
            trw = message.content[12:]
            translator = Translator()
            result = translator.translate(trw, dest='ru').text
            await message.channel.send(result)
        if message.content.startswith('!change'):
            self.ln_src = message.content[8:10]
            self.ln_dest = message.content[11:13]
            await message.channel.send(f'{self.ln_src}-{self.ln_dest} are chosen')
        if message.content.lower().startswith('!wiki'):
            pg = wikipedia.page(wikipedia.search(message.content.lower()[10:])[0])
            await message.channel.send(f'{pg.title}\n{pg.content[:400]}\n\n{pg.url}')


client = Bot()
client.run(TOKEN)
