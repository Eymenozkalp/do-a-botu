import discord
from discord.ext import commands
import random

# Intents ayarlarını oluştur
intents = discord.Intents.default()
intents.messages = True  # Mesajları dinle

# Botun prefix'i ve intents ile oluştur
bot = commands.Bot(command_prefix='!', intents=intents)

# Doğa ile ilgili bilgiler
nature_facts = [
    "Ağaçlar, havadaki karbondioksiti alarak oksijen üretir.",
    "Doğada 3 milyon farklı bitki türü vardır.",
    "Ormanlar, yeryüzünün en büyük karbondioksit emme kaynaklarından biridir.",
    "Bir ağaç, yılda yaklaşık 2.6 ton karbondioksiti emebilir.",
    "Küçük bir ormanın, sıcak havalarda 10 derece kadar serinletici etkisi olabilir."
]

# Bot hazır olduğunda mesaj gönderir
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

# Doğa bilgisi komutu
@bot.command(name='dogafakti')
async def nature_fact(ctx):
    fact = random.choice(nature_facts)
    await ctx.send(f'Doğa ile ilgili bir bilgi: {fact}')

# Botu çalıştırma
TOKEN = 'token'  # Buraya bot tokeninizi ekleyin
bot.run(TOKEN)
