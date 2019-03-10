import discord
from keep_alive import keep_alive
from discord.ext import commands

TOKEN = 'NTE4MzE4NzY1NDM2NTY3NTUy.DuPBmw.EWQZhHDDVLnxDdVi8QhKhIXuTlI'

client=commands.Bot(command_prefix='spam')


@client.event
async def on_message(message):
    channel = messgae.channel
    client.send_message(channel, 'xp grinding lol dont get mad')

keep_alive()
client.run(TOKEN)
