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
@client.event
async def on_member_join(member):
    print(f"{member} has joined a server")
@client.event
async def on_member_remove(member):
    print(f"{member} has left the server")
@client.command()
async def ping(ctx):
    await ctx.send(f"Latency is {round(client.latency * 1000)}ms")
@client.command(aliases=["test"])
async def coin(ctx, *, question):
    responses = [
        "The Coin Flipped to Heads",
        "The Coin Flipped to Tails"]

    await ctx.send(f"Prediction: {question}\nAnswer: {random.choice(responses)}")
@coin.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please add a prediction between Heads and Tails")
