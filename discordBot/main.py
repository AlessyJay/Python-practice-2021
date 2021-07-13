import discord
from discord.ext import commands
import os

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '*')

@client.event
async def on_ready():
    print("Ready to serve!")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


client.run("ODM0NjU0MDU5Mjg5NzcyMDMy.YIECKg.bAZvSrlorBWEwBODmS-ki6PiL0Y")