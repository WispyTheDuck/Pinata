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

class Developer(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Developer(bot))
