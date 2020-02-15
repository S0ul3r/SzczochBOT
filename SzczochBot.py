#Necessary imports
import discord
import os, time, datetime, random, asyncio, aiohttp, json, discord, time
from discord.ext import commands

#Bot prefix
client = commands.Bot(command_prefix = "!")

#==========================================================================#
#       Commands explained here so you can make your own bot
#       @client.command()
#       async def NAME_OF_YOUR_COMMAND_GOES_HERE(ctx):
#       	await ctx.send('THIS IS WHAT THE BOT WILL TYPE IN THE DISCORD')
#       	print("WHAT YOU PUT HERE WILL BE PUT IN THE TERMINAL")


#Check if the bot is ready
@client.event
async def on_ready():
    print('Bot is running.')

#Posts in channel when someone joins the discord.
@client.event
async def on_memver_join(member):
	print(f"{member} has joined a server")

#Posts in channel when member leaves the discord.
@client.event
async def on_memver_remove(member):
	print(f"{member} has left a server")

#==========================================#
#======          COMMANDS            ======#     
#==========================================#

#When user types ping, bot sends pong back.
@client.command()
async def ping(ctx):
	await ctx.send('Pong')
	print("command worked cmd=pong")

#Sends discord invite
@client.command()
async def discord(ctx):
	await ctx.send('https://discord.gg/mNJ3QV')
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

#Help command to display avaiable commands
@client.command()
async def helpme(ctx):
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
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('spotify.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)

            break

        print(f"  > User {ctx.author} generated a Spotify Account at time {datetime.datetime.now()}")
        await ctx.send(f"{User}:{PassFixed}")


client.run('Njc2NDUzNjMwMDM0ODM3NTQ0.XkF7Vw.HQVasoU3EQSG3vatBgYAdA5ilMw')