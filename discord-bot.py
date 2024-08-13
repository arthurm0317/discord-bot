import discord, time, random, youtube_dl
from discord.ext import commands
from discord import FFmpegPCMAudio
# from selenium import webdriver
# from selenium.webdriver.common.by import By

intents = discord.Intents.default()
intents.message_content = True
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# navegador=webdriver.Chrome(options=options)

bot=commands.Bot(command_prefix='', intents=intents)
# site='https://www.sofascore.com/pt/time/futebol/corinthians/1957'
# navegador.get(site)
# time.sleep(1)
# tempo=navegador.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/span[2]/span')

@bot.listen('on_message') 
async def on_message(message):
    user_name= message.author.name
    if user_name=='ás' or user_name=='as6920':
        await message.channel.send("VAI TOMAR NO CU JOÁS")
    if message.content.lower()=='corinthians':
        await message.channel.send('VAI CORINTHIANS')
    if message.content.lower()=='gol deles':
        await message.channel.send('reação honesta', file=discord.File('C:/Users/arthu/programas/python/vinte_tres/midia/gaviao.png'))
        # await message.add_reaction("")
    if message.content.lower()=='gol nosso':
        await message.channel.send('reação honesta', file=discord.File('C:/Users/arthu/programas/python/vinte_tres/midia/gaviao_feliz.png'))
    if message.content.lower()=='timão' or message.content.lower()=='timao':
        with open('img.txt', "r") as file:
            imgs=file.readlines()
        q=len(imgs)
        numAleatorio=random.randint(0,q-1)
        finalImg=imgs[numAleatorio]
        await message.channel.send(finalImg)
    if message.content.lower()=="as brabas":
        with open('brabas.txt', 'r') as file:
            brabas=file.readlines()
        q=len(brabas)
        ftAleatoria=random.randint(0, q-1)
        ftBrabasFinal=brabas[ftAleatoria]
        await message.channel.send(ftBrabasFinal)



# @bot.command()
# async def tocar(ctx, url):
#     voice_channel = ctx.author.voice.channel
#     if not voice_channel:
#         await ctx.send("Você não está em um chat de voz.")
#         return

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }

#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=False)
#         if 'entries' in info:
#             info = info['entries'][0]
#         url2 = info['url']

#     voice_client = await voice_channel.connect()
#     voice_client.play(FFmpegPCMAudio(url2))
#     await ctx.send(f'Tocando: {info["title"]}')

# @bot.command()
# async def sair(ctx):
#     voice_client=ctx.voice_client
#     if voice_client:
#         await voice_client.disconnect()
#         await ctx.send('Desconectado do canal de voz')
#     else:
#         await ctx.send('Limpe sua boca antes de mandar o corinthinas sair de um lugar que ele não está')

@bot.event
async def on_ready():
    channel_id=1144409113195978832
    channel = bot.get_channel(channel_id)
    print('connected')
    if channel:
        await channel.send("VAMO VAMO CORINTHIANS")

bot.run('your key here')