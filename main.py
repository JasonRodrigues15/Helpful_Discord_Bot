import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix=".")
token = open("token.txt", "r").read()
client.run(token)
status = cycle(['.info for information', '.help for commands'])
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(""))
    change_status.start()
    print('The bot is ready to run.')
@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
