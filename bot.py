from aiohttp import request
import discord
from discord.ext import commands
import random


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)
img_name =  ["1.jpg", "2.jpg", "3.jpg", "Oh-no.gif"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

ms = [('M2L1/imagenes/Oh-no.gif', 'rb'),"","",]
@bot.command()
async def mem(ctx):
    with open('M2L1/imagenes/Oh-no.gif') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    import os
    print(os.listdir('images'))
    with open(f'images/{random.choice(img_name)}', 'rb') as f:
            picture = discord.File(f)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = request.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
bot.run('MTE1OTY1NDU1Mzc4MDc2MDYwNg.G7QNJi.gFUfoKSviq3F-Xywc1mTZaMRz4mDZjqOmDEdeI')
