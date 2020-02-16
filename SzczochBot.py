#Necessary imports
import discord
from discord.ext import commands
import configparser
import os

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

    print('==== Bot is loading cogs ====')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f'cogs.{filename[:-3]} loaded.')

    print(f'Connected to {len(client.servers)} servers:')
    for server in client.servers:
        print(f'- {server.name}')
    
    print('==== Bot has finished initialization ====')

#==========================================#
#======          COMMANDS            ======#     
#==========================================#

#Load cogs
@client.command()
async def load(ctx,extension):
	client.load_extension(f'cogs.{extension}')

#Unload cogs
@client.command()
async def unload(ctx,extension):
	client.unload_extension(f'cogs.{extension}')

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

client.run('Njc2NDUzNjMwMDM0ODM3NTQ0.Xkkzmg.zASBgMTVq-lgXUZQhIhuz-vpxHc')