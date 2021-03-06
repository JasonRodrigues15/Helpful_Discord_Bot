import discord
import random
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix=".")
client.remove_command("help")
token = open("token.txt", "r").read()
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
@client.command()
@commands.has_role("Clearer")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Deleted {amount} messages")@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You are not allowed to use that command")
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command used.")
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member, role)
@client.command()
async def info(ctx):
    embed = discord.Embed(
        title="Helpful Bot",
        description="This is a bot used to help manage a server with common commands.",
        colour=discord.Colour.dark_blue()

    )

    embed.set_footer(text="Bot by Jason Rodrigues")
    embed.set_image(url="https://cdn.discordapp.com/attachments/750142801051648130/751157271815389254/black-and-white-handshake-clipart-3.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/750142801051648130/751157271815389254/black-and-white-handshake-clipart-3.png")
    embed.set_author(name=".info", icon_url="https://cdn.discordapp.com/attachments/750142801051648130/751157271815389254/black-and-white-handshake-clipart-3.png")
    embed.add_field(name=".help", value="Use the .help command for a full list of all commands", inline=False)

    await ctx.send(embed=embed)
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    help_embed = discord.Embed(
        colour=discord.Colour.dark_blue()
    )

    help_embed.set_author(name='Help')
    help_embed.add_field(name='.ping', value='Returns Pong!', inline=False)
    help_embed.add_field(name='.ping', value='Returns the latency', inline=False)
    help_embed.add_field(name='.coin', value='Flips a coin', inline=False)
    help_embed.add_field(name='.info', value='Displays the info card', inline=False)
    help_embed.add_field(name='.clear', value='Clears specified number of messages', inline=False)

    await ctx.send("Check your direct messages, I have sent you a help message.")
    await author.send(embed=help_embed)
client.run(token)