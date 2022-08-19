# Imports
import os
import discord
import environment
import redditAPI

# Intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Reddit
top = redditAPI.getTopPost()

# Bot Events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: 
        return

    if message.content.startswith('$top'):
        await message.channel.send(top[0])
        await message.channel.send(top[1])

client.run(environment.discordToken)