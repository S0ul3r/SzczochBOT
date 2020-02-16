#Necessary imports
import discord
from discord.ext import commands
import os, time, datetime, random, asyncio, aiohttp, json, discord, time
import configparser

#Bot prefix
client = commands.Bot(command_prefix = "!")

# Read our config file
client.cfgParser = configparser.ConfigParser()
client.cfgParser.read("auth.ini")

# Store the data from config file
discordKey = client.cfgParser.get("discord", "TOKEN")

#Check if the bot is ready
@client.event
async def on_ready():
    print('==== Bot is starting ====')

    print(f'Connected to {len(client.servers)} servers:')
    for server in client.servers:
        print(f'- {server.name}')
    
    print('==== Bot has finished initialization ====')


#==========================================#
#======          COMMANDS            ======#     
#==========================================#

#When user types ping, bot sends it's latency.
@client.command()
async def ping(ctx):
	await ctx.send(f'{round(client.latency * 1000)} ms')
	print("command worked cmd=pong")

#When user types hello, bot replys with hi.
@client.command(aliases=['Hi', 'Hello'])
async def hello(ctx):
	await ctx.send("Hello")
	print("command worked cmd=Hello")

#Logout command for logging the bot out.
@client.command()
async def logout(ctx):
	await client.logout()

#Help command to display avaiable commands and remove previous help command
client.remove_command("help")
@client.command()
async def help(ctx):
    await ctx.send('\n\t\nBot commands:\n```!spotify - generates a spotify account\
    \n!netflix - generates a netflix account\
    \n!hulu - generates a hulu account\
    \n!stock - shows the stock for each account type```')

#Print spotify account
@client.command(pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def spotify(ctx):
    author = ctx.message.author
    with open('spotify.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            part = randomline.split(':')
            User = part[0]
            Pass = part[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('spotify.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)
            break
        print(f"  > User {ctx.author} generated a Spotify Account at time {datetime.datetime.now()}")
        await ctx.send(f"```Username:{User}\nPassword:{PassFixed}```")

client.run(discordKey)