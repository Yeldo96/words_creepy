import discord
from discord.ext import commands


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


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


bot.run('MTE1OTY1NDU1Mzc4MDc2MDYwNg.G7QNJi.gFUfoKSviq3F-Xywc1mTZaMRz4mDZjqOmDEdeI')