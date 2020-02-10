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
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, msg):
        txt = ["You're all chicken nuggets.,
               "Nyoooooooooooooooooooooom",
               "Quack.",
               "Look at all those chickens!",
               "Minecraft is better than Fortnut.",
               "twitter.com/WispyTheDuck"]
        
        await ctx.message.delete()
        embed = discord.Embed(color=discord.Color.orange())
        embed.add_field(name='**Pinata Bot**', value=f'{msg}')
        embed.set_footer(text=f"{random.choice(txt)}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Chat(bot))

def teardown(bot):
    bot.remove_cog(Chat(bot))
    print('Chat is unloaded.')
