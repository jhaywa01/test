import json
import random
import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

TOKEN = 'NTEyNjQ3MzY2OTE0ODY3MjEw.DuDL6A.lq7SA4w-VX2dGYDz5diIBBwR8dQ'

client = commands.Bot(command_prefix='.', status=discord.Status.online, activity=discord.Game(name='Fortnite'))
client.remove_command('help')

os.chdir('C:/Users/jhayw/Documents/python')

@client.event
async def on_ready():
    print("I'm Ready! I'm Ready! I'm Ready!")
    print(client.user)

@client.command(pass_context=True)
async def ping(ctx):
    await client.say('pong!')

@client.event
async def on_message(message):
    channel = message.channel
    if 'check me out' in message.content:
        await client.send_message(channel, 'yo im good.')


@client.command(pass_context=True)
async def readlist(ctx):
    channel = ctx.message.channel
    await client.send_file(destination=channel, fp='C:/Users/jhayw/Documents/python/bot/blacklist.txt', filename='blacklist.txt', content='Here it is', tts=None)

@client.command(pass_context=True)
async def addlist(ctx, arg1):
    channel = ctx.message.channel
    file = open('blacklist.txt', 'a')
    file.write(arg1)
    await client.send_file(destination=channel, fp='C:/Users/jhayw/Documents/python/bot/blacklist.txt', filename='blacklist.txt', content='Here is the updated one', tts=None)

@client.command(pass_context=True)
async def verify(ctx):
    author = ctx.message.author
    role = discord.utils.get(author.server.roles, name='Regular')
    if 'New' in author.roles:
        await client.add_roles(author, role)
        await client.say('Your verified')
    else:
        await client.say('Nice try, but your already verified! if this is a mistake, please contact a staff member in #support')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    channel = ctx.message.channel
    embed = discord.Embed(colour = discord.Colour.blue())

    embed.set_author(name = 'Help')
    embed.add_field(name = '.ping', value = 'Returns Pong/ Tells you that the bot is working', inline = False)
    embed.add_field(name = '.verify', value = 'type this if you have not been verified. removes New role and adds Regular', inline = False)
    embed.add_field(name = '.addlist', value = 'type this syntax and the word to add to blacklist', inline = False)
    embed.add_field(name = '.readlist', value = 'type this to download / read blacklist', inline = False)
    embed.add_field(name = 'prefix', value = 'Prefix=. (period)', inline = False)

    await client.send_message(channel, embed = embed)

keep_alive()
client.run(TOKEN)
