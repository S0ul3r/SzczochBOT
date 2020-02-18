import discord, os, time, datetime, random
from discord.ext import commands

class Accounts(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Post spotify account
    @commands.command(pass_context=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def spotify(self, ctx):
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

    #Post netflix account
    @commands.command(pass_context=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def netflix(self, ctx):
        author = ctx.message.author
        with open('netflix.txt', 'r') as (f):
            text_spo = f.readlines()
            while True:
                randomline = random.choice(text_spo)
                part = randomline.split(':')
                User = part[0]
                Pass = part[1]
                PassFixed = Pass.rstrip()
                if len(randomline) == 0:
                    continue
                with open('netflix.txt', 'w') as (c):
                    for line in text_spo:
                        if line.strip('\n') != f"{User}:{PassFixed}":
                            c.write(line)
                break
            print(f"  > User {ctx.author} generated a Netflix Account at time {datetime.datetime.now()}")
            await ctx.send(f"```Username:{User}\nPassword:{PassFixed}```")

def setup(client):
    client.add_cog(Accounts(client))