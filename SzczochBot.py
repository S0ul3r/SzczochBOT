#Necessary imports
import discord
from discord.ext import commands
import configparser
import os

#Bot prefix
client = commands.Bot(command_prefix = "!")

# Read our config file and stora data from it
config = configparser.ConfigParser()
config.read("auth.ini")
discordKey = config.get('discord', 'TOKEN')

#==========================================#
#======            LOADUP            ======#     
#==========================================#
@client.event
async def on_ready():
    print('==== Bot is starting ====')

    print('==== Bot is loading cogs ====')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename[:-3]} loaded.')
    
    print('==== Bot has finished initialization ====')

#==========================================#
#======          COMMANDS            ======#     
#==========================================#

#Load cogs
@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

#Unload cog
@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

#When user types ping, bot sends it's latency.
@client.command()
async def ping(ctx):
	await ctx.send(f'{round(client.latency * 1000)} ms')
	print("command worked cmd=pong")

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
    \n!stock - shows the stock for each account type```')

client.run(discordKey)