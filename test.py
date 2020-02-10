#Have python installed with pip, https://www.youtube.com/watch?v=dX2-V2BocqQ
#Run this in your command prompt
#pip install discord.py
#made by pineapplejuice
#join my discord https://discord.gg/x8fatV2
#=============================================#

#Necessary imports
import discord
from discord.ext import commands

#Paste the bot token in place of "TOKEN HERE", while leaving the "".
TOKEN = "TOKEN HERE"

#Place your desired bot prefix in between the quotes where "PREFIX HERE" currently is, while leaving the "".
client = commands.Bot(command_prefix = "PREFIX HERE")

#==========================================================================#
#       Commands explained here so you can make your own bot
#       @client.command()
#       async def NAME_OF_YOUR_COMMAND_GOES_HERE(ctx):
#       	await ctx.send('THIS IS WHAT THE BOT WILL TYPE IN THE DISCORD')
#       	print("WHAT YOU PUT HERE WILL BE PUT IN THE TERMINAL")


#Posts in channel when someone joins the discord.
@client.event
async def on_memver_join(member):
	print(f"{member} has joined a server")

#Posts in channel when member leaves the discord.
@client.event
async def on_memver_remove(member):
	print(f"{member} has left a server")

#==========================================#
#		Now for some fun commads

#When user types ping, bot sends pong back.
@client.command()
async def ping(ctx):
	await ctx.send('pong')
	print("command worked cmd=pong")

#Sends discord invite
@client.command()
async def disocrd(ctx):
	await ctx.send('https://discord.gg/x8fatV2')
	print("command worked cmd=discord")

#When user types hi, bot replys with hi.
@client.command()
async def hello(ctx):
	await ctx.send("Hello")
	print("command worked cmd=Hello")

#Logout command for logging the bot out.
@client.command()
async def logout(ctx):
	await client.logout()

			#Put your comands Under this 
#=======================================================#

















#====================================================================================#
#This is where your program is run, do not put anything below this or the bot will not work. Do not replace TOKEN with the token.
client.run(TOKEN)