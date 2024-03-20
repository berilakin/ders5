import discord
from discord.ext import commands
import random
import os



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def mem1(ctx):
    with open('resimler\mem1.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('resimler\mem2.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open('resimler\mem3.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem4(ctx):
    with open('resimler\mem4.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem5(ctx):
    with open('resimler\mem5.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem6(ctx):
    with open('resimler\mem6.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)



@bot.command()
async def rastgele(ctx):
    #rastgele resim seç
    random_img = random.choice(os.listdir('mem1 , mem2 , mem3 , mem4 , mem5 , mem6'))
    with open(f'resimler\mem1 , mem2 , mem3 , mem4 , mem5 , mem6/{random_img}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

# Resim gönder
    await ctx.send(f'Bir {random_img} memi!', file=picture)


    def animals(ctx):
        # Klasör yoksa oluşturun
        if not os.path.exists('animals'):
            os.makedirs('resimler/animals')

        # Rastgele resim seç
        random_animal = random.choice(os.listdir('resimler/animals'))
        with open(f'animals/ animal1 , animal2 , animal3 , animal4{random_animal}', 'rb') as f:
            picture = discord.File(f)


        # Resim gönder
        animal = f'Bir {random_animal} memi!'

bot.run("............")

