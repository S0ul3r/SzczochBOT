#Necessary imports
import discord
import os, time, datetime, random, asyncio, aiohttp, json, discord, time
from discord.ext import commands

#Paste the bot token in place of "TOKEN HERE", while leaving the "".
TOKEN = 'Njc2NDUzNjMwMDM0ODM3NTQ0.XkF7Vw.HQVasoU3EQSG3vatBgYAdA5ilMw'

#Place your desired bot prefix in between the quotes where "PREFIX HERE" currently is, while leaving the "".
client = commands.Bot(command_prefix = "!")

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

        print(Fore.GREEN + '')
        print(f"  > User {ctx.author} generated a Spotify Account at time {datetime.datetime.now()}")
        print(Fore.WHITE + '')
        await ctx.send(f"{User}:{PassFixed}")


client.run(TOKEN)