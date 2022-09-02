# Imports
import discord
import environment
import redditAPI
from discord.ext import tasks


# Intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Reddit
currentPost = redditAPI.getNewPost()

# Bot Events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    on_newPost.start()

# Updating new posts every 3 seconds
@tasks.loop(seconds=3)
async def on_newPost():
    global currentPost
    channel = client.get_channel(1009949302929506317)
    newPost = redditAPI.getNewPost()
    if newPost != currentPost:
        await channel.send(newPost[0])
        await channel.send(newPost[1])
        currentPost = newPost

@client.event
async def on_message(message):
    if message.author == client.user: 
        return

    if message.content.startswith('$top'):
        topPost = redditAPI.getTopPost()
        await message.channel.send(topPost[0] + '\n' + topPost[1])

client.run(environment.discordToken)