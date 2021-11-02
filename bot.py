import subprocess
import time
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'somethingelse')
client.remove_command('help')
TOKEN = 'yourtokenhere'

description = '''Codeoffuns bot!'''
bot = commands.Bot(command_prefix='!', description=description, help_command=None)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def temp(ctx):
    """Says world"""
    await ctx.send(subprocess.run(["vcgencmd", "measure_temp"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip())

@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@bot.command()
async def source(ctx):
    """Source Code"""
    await ctx.send("https://github.com/codeoffun2/botty/tree/main")

@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def help(ctx):
    time.sleep(0.5)
    embed=discord.Embed(title="Help",
    url="http://discord.gg/HaJPgdV9bG")
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="")
    embed.add_field(name="Prefix", value="!",inline=False)
    embed.add_field(name="add", value="Adds two numbers ", inline=True)
    embed.add_field(name="hello", value="says world", inline=True)
    embed.add_field(name="temp", value="shows rpi temperature", inline=True)
    embed.add_field(name="help", value="shows this message", inline=True)
    embed.add_field(name="source", value="shows github link", inline=True)
    embed.set_footer(text="")
    await ctx.send(embed = embed)

bot.run(TOKEN)
