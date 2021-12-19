import discord
import uwufier as u
import os

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.delete()
    await message.channel.send('---------------------------------------------- \n' +  message.author.mention + ' sent: \n' + u.uwufy(message.content))

client.run(open(os.path.join('token'), "r").read())