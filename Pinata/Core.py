# To-Do list:
# 1. Basic levelling system.
# 2. Make it better than the LA Bot because why not.


import discord
import random
import os
import datetime
import asyncpg
import asyncio
import json
import sys
from discord.ext import commands, tasks
from discord.utils import get, find
from itertools import cycle

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)


    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix = get_prefix)
bot.remove_command('help')


@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '>'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command()
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Your new prefix is: {prefix}')



for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename.startswith('_'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print('Online.')
    print('----------')

@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name='Guests')
    await member.add_roles(role)
    embed = discord.Embed(color=discord.Color.teal(), description=f'Welcome to the {member.guild} server!')
    embed.set_thumbnail(url=f'{member.avatar_url}')
    embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
    embed.set_footer(text='Duck Lounge - Server for ducks', icon_url=f'{member.guild.icon_url}')

    channel = bot.get_channel(id=671911866166935553)
    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    role = get(member.guild.roles, name='Guests')
    await member.remove_roles(role)
    embed = discord.Embed(color=discord.Color.orange(), description=f'Bye! Hope you enoyed your stay at the {member.guild}!')
    embed.set_thumbnail(url=f'{member.avatar_url}')
    embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
    embed.set_footer(text='Duck Lounge - Server for ducks', icon_url=f'{member.guild.icon_url}')

    channel = bot.get_channel(id=671911866166935553)
    await channel.send(embed=embed)



@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 671925047501258762:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == 'Updates':
            role = discord.utils.get(guild.roles, name='Updates')
        elif payload.emoji.name == 'Announcements':
            role = discord.utils.get(guild.roles, name='Announcements')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
            else:
                print('Member not found.')
            
        else:
            print("Role not found.")

@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 671925047501258762:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == 'Updates':
            role = discord.utils.get(guild.roles, name='Updates')
        elif payload.emoji.name == 'Announcements':
            role = discord.utils.get(guild.roles, name='Announcements')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
            else:
                print('Member not found.')
            
        else:
            print("Role not found.")

@bot.command()
async def status(ctx, arg):
    await ctx.message.delete()
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f'{arg}'))

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(color=discord.Color.teal(), description='Unload Successful')
    embed.add_field(name='Unloaded extension: ', value=f'{extension}')

    await ctx.send(embed=embed)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(color=discord.Color.teal(), description='Load Successful')
    embed.add_field(name='Loaded extension: ', value=f'{extension}')

    await ctx.send(embed=embed)

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(color=discord.Color.teal(), description='Reload successful.')
    embed.add_field(name='Reloaded extension: ', value=f'{extension}')

    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def apply(ctx, *args):
    member = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(color=discord.Color.orange())
    embed.add_field(name=f'**{member.name}#{member.discriminator}**s application.', value=f'{args}')
    channel = bot.get_channel(id=671951048977547275)
    await channel.send(embed=embed)
    


bot.run("token")
