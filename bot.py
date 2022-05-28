import subprocess
import time 
import discord 
from discord.ext import commands 
import random 
import sys

client = commands.Bot(command_prefix = 'somethingelse')
client.remove_command('help')
TOKEN = '(token)'

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
    embed.add_field(name="say", value="makes the bot say your message (e.x. !say (message).", inline=True)
    embed.add_field(name="correct", value="chooses which person is correct (e.x. !correct guy1 guy2).", inline=True)
    embed.add_field(name="responses", value="Shows all autoresponses", inline=True)
    embed.set_footer(text="")
    await ctx.send(embed = embed)

@bot.command()
async def say(ctx, *, arg):
	await ctx.send(arg)

@bot.command()                                
async def mention(ctx,  member: discord.Member, *, arg):
        await ctx.message.delete()                                                                                                                 
        await ctx.send(f'{member.mention} {arg}')

@bot.command()
async def correct(ctx, arg1, arg2):
        members = [(arg1), (arg2)]
        await ctx.send(f'{random.choice(members)} is correct.')

@bot.command()
async def slay(ctx):
	await ctx.message.delete()
	await ctx.send("SLAYYYYYYYYYYYYYY")
@bot.command()
async def responses(ctx):
    embed=discord.Embed(title="Responses")
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="")
    embed.add_field(name="rpis out of stock", value="Looks for keywords 'raspberry', 'out', and 'stock' ", inline=True)
    embed.add_field(name="tutorials", value="Looks for keywords 'raspberry' and 'tutorials'", inline=True)
    embed.set_footer(text="")
    await ctx.send(embed = embed)

@bot.event
async def on_message_delete(message):
    msg = str(message.author)+ " deleted message in #"+str(message.channel)+'('+str(message.channel.id)+')'+': '+str(message.content)
    print(msg)
    with open("deleted_messages.txt", "a") as n:
        n.write(f'{message.author} deleted message in #{message.channel}({message.channel.id}): {message.content}' + '\n')

@bot.event

async def on_message(message):

	if message.author.bot:
		return

	if 'purple' in message.content:
		
		await message.channel.send("I LOVE LEAN 😈😈😈😈💜💜💜💜💜💜💜")
	

	if "botty" in message.content and "sucks" in message.content:
		list = ["please stfu respectfully. You don't look good either.", "Thats all you got?", "damn, imagine trying to roast a bot.", "come again?", "Shut up your breath stinks", "well, you look like a well groomed dingleberry."]
		await message.channel.send(random.choice(list))
	user = message.author
	if discord.utils.get(user.roles, name="Blueberry") is None:
		if "raspberry" in message.content and "out" in message.content and "stock" in message.content:
			await message.channel.send(""" <#915461470257565737>
https://discord.com/channels/204621105720328193/915461470257565737/937183329483116544
		
																				""")

	if "raspberry" in message.content and "tutorial" in message.content:
		await message.channel.send("""<#915461470257565737> 
https://discord.com/channels/204621105720328193/915461470257565737/967612506535243818
																				""")
		if 'SLAYYYY' in message.content:
			await message.channel.send('SLAYYYY')

	await bot.process_commands(message)

bot.run(TOKEN)

