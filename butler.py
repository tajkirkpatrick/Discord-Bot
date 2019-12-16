import discord
from discord.ext import commands
import os
import json

bot = commands.Bot(command_prefix='!')

with open('config.json', 'r') as config:
    data = json.load(config)
    TOKEN = data['token']


@bot.event
async def on_ready():
    print("Bot Is Ready")
    print(discord.__version__)

@bot.command(aliases=['Search', 'Find', 'find'])
async def search(ctx, *, args):

    search_string = "https://www.google.com/search?q="

    for space in args:
        if space == ' ':
            args = args.replace(" ", "+")
    else:
        pass

    link = str(search_string) + str(args)

    embed = discord.Embed(title=f"Search results: {args}", url=link)
    embed.add_field(name="A Google Search turned this up:", value=link)

    await ctx.send(embed=embed)


@bot.command(aliases=['hi', 'hey'])
async def hello(ctx):
    await ctx.send(f"Hi There {ctx.author.mention}")


@bot.command(aliases=['purge'], hidden=True)
async def clear(ctx, amount=2):
    if amount <= 0:
        await ctx.send("Yroo, I can't purge 0 messages. Try again!")

    await ctx.channel.purge(limit=amount)


@bot.command(hidden=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command(hidden=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command(hidden=True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(f"{extension} cog, reloaded!")
    await ctx.send(f'{extension} cog, reloaded!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)
