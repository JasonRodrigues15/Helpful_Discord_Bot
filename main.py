import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix=".")
token = open("token.txt", "r").read()
client.run(token)
