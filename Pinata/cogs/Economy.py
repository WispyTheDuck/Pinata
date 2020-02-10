import discord
import json
import random
from discord.ext import commands, tasks
from discord.utils import get, find

class Economy(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

             

def setup(bot):
    bot.add_cog(Economy(bot))
    print('Economy has been loaded.')

def teardown(bot):
    bot.remove_cog(Economy(bot))
    print('Economy has been unloaded')



