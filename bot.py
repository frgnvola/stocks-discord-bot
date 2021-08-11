import yfinance as yf
import pandas as pd
from discord.ext import commands
from fin_functions import getRecentData, today
import random

# TODO: add help command to show full commands list 

# Remove default help command so we can make our own
client = commands.Bot(command_prefix = '$', help_command=None)
GREETINGS_LIST = ["I feel like I’m back at the Green Dragon.", "It comes in pints?", "I am hungry. What is the time?", 
"The Eagles are coming! The Eagles are coming!", "We've had one, yes. What about Second Breakfast?", "Great! Where are we going?"]
COMMANDS_LIST = ["$info XXXX: display data for any single stock, doesn't have to be in your list",  "$add XXXX: add a stock to your list", 
"$showAll: display your current list", "$infoAll: display data for all stocks in your list "]
symbols = []

@client.event
async def on_ready():
    await client.get_channel(870028201924132394).send(random.choice(GREETINGS_LIST))
    await client.get_channel(870028201924132394).send("Type $help for a list of commands")

@client.command()
async def help(ctx):
    for entry in COMMANDS_LIST:
        await ctx.send(entry)

@client.command()
async def add(ctx, company_name):
    if company_name not in symbols:
        symbols.append(company_name)
        await ctx.send("Added {} to list at spot #{}".format(company_name, (len(symbols))))    
    else:       
        await ctx.send("{} Already exists at spot number {{}}".format(company_name, symbols.index(company_name)))

@client.command()
async def showAll(ctx):
    if not symbols:
        await ctx.send("Oi this list is empty!")
    for ticker in symbols:
        await ctx.send(ticker)

# TODO: implement intraday comparisons to make use of df data  from fin_functions
    # TODO: figure out how to host this (linode? aws?)
    # look into: event flows, event scheduling, event workers, event queue etc.

@client.command()
async def info(ctx, company_name):
    await ctx.send("Here's what {} is doing as of {}:".format(company_name, today))
    # await ctx.send(getRecentData(company_name))
    for entry in getRecentData(company_name):
        await ctx.send(entry)

@client.command()
async def infoAll(ctx):
    if not symbols:
        await ctx.send("Oi this list is empty!")
    for ticker in symbols:
        await ctx.send("Here's some data for {} - - - - - - - - -".format(ticker))
        for entry in getRecentData(ticker):
            await ctx.send(entry)


client.run('ODcwMDM3Njk1MzMyNzU3NTE1.YQG7vw.5vpBTFkhZwry')
