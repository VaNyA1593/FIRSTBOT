import discord
from bot_logic import gen_pass
from bot_logic import coin

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("Bye!")
    elif message.content.startswith("$password"):
        await message.channel.send("Твой пароль: " + gen_pass(10))
    elif message.content.startswith("$coin"):
        await message.channel.send(coin())
    else:
        await message.channel.send(message.content)

client.run("MTIxMDk4MDA4NjMzMzk2ODUzNQ.GB8RgD.AlFR3Z_i5ykXj9CKUog8eZhQwF29X-dZqwHWts")
