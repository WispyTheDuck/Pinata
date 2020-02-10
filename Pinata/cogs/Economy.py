import discord
import json
import random
from discord.ext import commands, tasks
from discord.utils import get, find

class Economy(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot


    @commands.command()
    async def work(self, ctx):
        with open('users.json', "r") as f:
            if user.id not in ['users.json']:
                user = json.load(f)

            userID = (f"{user.id}"),
            wallet = 0,
            bank = 0

            with open('users.json', 'w') as f:
                json.dump(user, f, indent=4)
             

def setup(bot):
    bot.add_cog(Economy(bot))
    print('Economy has been loaded.')

def teardown(bot):
    bot.remove_cog(Economy(bot))
    print('Economy has been unloaded')



