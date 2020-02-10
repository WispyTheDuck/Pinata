
# To-Do List:
# 1. Add a channel feature for the say command.
# 2. Give the update command a better outline.

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

class Chat(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot


    @commands.command()
    async def updates(self, ctx, *, msg):
        await ctx.message.delete()
        embed = discord.Embed(color=discord.Color.teal())
        embed.add_field(name='Updates!', value=f'{msg}')

        await ctx.send(embed=embed)


    @commands.command()
    async def announce(self, ctx, *, msg):
        await ctx.message.delete()
        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name='Announcements!', value=f'{msg}')

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        embed = discord.Embed(color=discord.Color.orange())
        embed.add_field(name='**Pinata Bot**', value=f'{msg}')
        embed.set_footer(text="You're all chicken nuggets.")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Chat(bot))

def teardown(bot):
    bot.remove_cog(Chat(bot))
    print('Chat is unloaded.')
