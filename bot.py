import subprocess
import time 
import discord 
from discord.ext import commands 
import random 
import traceback
import datetime

client = commands.Bot(command_prefix = 'somethingelse')
client.remove_command('help')
TOKEN = 'ODg4OTMzNDM4MTA1NzIyOTIw.GFO5b7.7jgp944U6eMPRgXyrP23VtUa2AVEq1Dl2Ezr_M'

description = '''Codeoffuns bot!'''
bot = commands.Bot(command_prefix='!', description=description, help_command=None)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("That command wasn't found! Sorry :(")

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

@bot.command()
async def ping(ctx,  member: discord.Member, *, arg):
	await ctx.message.delete()
	await ctx.send(f'{member.mention} {arg}')

@bot.event

async def on_message(message):
	if 'purple' in message.content:
		
		await message.channel.send("I LOVE LEAN 😈😈😈😈💜💜💜💜💜💜💜")
	

	if 'botty' and "suck" in message.content:
		list = ["please stfu respectfully. You don't look good either.", "Thats all you got?", "damn, imagine trying to roast a bot.", "come again?", "Shut up your breath stinks", "well, you look like a well groomed dingleberry."]
		await message.channel.send(random.choice(list))

	elif 'botty' in message.content:
		list = ["Hi there!", "please stfu respectfully.", "Damn. You're looking hot today."]
		await message.channel.send(random.choice(list))

		if 'SLAYYYY' in message.content:
			await message.channel.send('SLAYYYY')

	await bot.process_commands(message)

bot.run(TOKEN)

