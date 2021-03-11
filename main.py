import discord
import os
from discord.ext import commands
from keep_alive import keep_alive
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Osaa Gotowy')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('Osa zdążysz?'):
    await message.channel.send('Zdążę? Zdążę')

  if msg.startswith('Osa jak tam giełda?'):
    await message.channel.send('Trzeba inwestować w odpowiednich momentach a potem sprzedawać. Zawsze po lekcji i w trakcie lekcji jadę na giełdę.')

  if msg.startswith('Osa jesteś strasznie zimny'):
    await message.channel.send('Hej wszystkim, jestem osa, kocham was ale nie jestem KURWA MAĆ ZIMNY!')

  if msg.startswith('Osa tak tak tak'):
    await message.channel.send('TAK TAK TAK TAK TAK')

  if msg.startswith('Osa ile kobiet wyruchałeś?'):
    await message.channel.send('A ile zjadłeś kromek chleba w twoim życiu?')

  if msg.startswith('Osa w co grasz?'):
    await message.channel.send('GTA ONLINE RP to jest PRAWDZIWE życie PRAWDZIWA policja!')

  if msg.startswith('Osa jak tam?'):
    robótka = [
        "Policja mnie goni!",
        "Rucham klaudię",
        "Eksportuję samochody",
        ]
    await message.channel.send((random.choice(robótka)))

  if msg.startswith('Osa kocham cię'):
    await message.channel.send('Ja was wszystkich kocham')

  if msg.startswith('Osa pomocy'):
    await message.channel.send('Zbiór komend\n- Osa kocham cię\n- Osa zdążysz?\n- Osa jak tam giełda?\n- Osa jesteś strasznie zimny\n- Osa tak tak tak\n- Osa ile kobiet wyruchałeś?\n- Osa w co grasz?\n- Osa jak tam?')

keep_alive()
client.run(os.getenv('TOKEN'))