import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix=".")
token = open("token.txt", "r").read()
client.run(token)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(""))
    change_status.start()
    print('The bot is ready to run.')
