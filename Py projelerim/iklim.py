import discord
from discord.ext import commands

import os
print(os.listdir('iklim_foto'))

import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send(f"Merhaba! Ben {bot.user}, dünyamızı korumak için çevremizi temiz tutmalı ve karbon ayak izini azaltmalıyız. Bunun için sana bazı önerilerim var:")

@bot.command()
async def iklim_krizi(ctx):
    await ctx.send(f"İklim krizi, gezegenimizin karşılaştığı en büyük zorluklardan biridir. Karbon salınımını azaltmak için hep birlikte çalışmalıyız.")

@bot.command()
async def ne_yapabilirim(ctx):
    await ctx.send(f"1. Toplu taşıma kullanmak\n2. Gereksiz ışıkları kapatmak\n3. Gıda israfını önlemek\n4. Tek kullanımlık ürünler yerine yeniden kullanılabilir ürünler (matara, bez çanta, cam kavanoz gibi) kullanmak\n5. Atıkları çöpe atmadan önce ayrıştırmak\n6. Bulut depolamanı temizle, gereksiz veri transferi ve sunucuların çalışmasını azalt\n7. İkinci el kıyafetler ve sürdürülebilir üretim yapan markaları tercih et\n8. Giymediğin kıyafetleri dönüştür veya bağışla\n9. Ağaç dik, doğayı koru")

@bot.command()
async def karbon_ayak_izi(ctx):
    await ctx.send(f"karbon ayak izi, bir kişinin, kurumun veya ürünün doğrudan veya dolaylı olarak atmosfere saldığı sere gazlarının toplam miktarını ifade eder.")

@bot.command()
async def yardım(ctx):
    await ctx.send("**$selam** - Merhaba diyip kendini tanıtır. \n**$iklim_krizi** - İklim krizini açıklar. \n**$ne_yapabilirim** - İklim değişikliği ile mücadele için önerilerde bulunur. \n**$karbon_ayak_izi** - Karbon ayak izini açıklar. \n**$iklim_foto** - Rastgele bir iklim fotoğrafı gönderir.")

@bot.command()
async def iklim_foto(ctx):
    img_name = random.choice(os.listdir('iklim_foto'))
    with open(f'iklim_foto/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("..")
