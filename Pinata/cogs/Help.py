
# To-Do List
# 1. Nothing yet.

import discord
from discord.ext import commands

# Defining Class
class Help(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot


    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(color=discord.Color.green(), description='**__Please specify a category.__**')
        embed.add_field(name='__Categories__: ', value="`Misc`, `Moderation`, `Information`, `Levels`")
        await ctx.send(embed=embed)

    @help.command(aliases=['moderation'])
    async def Moderation(self, ctx):
        embed = discord.Embed(color=discord.Color.green(), description='**__Moderation Commands__**')
        embed.add_field(name="```ban @member```", value='Bans a member from the server.')
        embed.add_field(name="```Kick @member```", value='Kicks a member from the server.')
        embed.add_field(name="```Clear <number of msgs>```", value='Clears a certain amount of messages in a channel.')

        await ctx.author.send(embed=embed)

    @help.command(aliases=['misc'])
    async def Misc(self, ctx):
        embed = discord.Embed(color=discord.Color.green(), description='**__Misc Commands__**')
        embed.add_field(name='```Ping```', value='Just a regular ping command.')
        embed.add_field(name='```8ball <question>```', value='Ask it a question and it will respond with a random answer.')
        embed.add_field(name='```Rolldice```', value='Rolls a dice and gives you a number between 1 and 6.')
        embed.add_field(name='```Coinflip```', value='Flips a coin and lands on heads or tails.')
        embed.add_field(name='```Duck```', value='Sends a link to the duck song.')

        await ctx.author.send(embed=embed)

    @help.command(aliases=['info', 'information'])
    async def Information(self, ctx):
        embed = discord.Embed(color=discord.Color.green(), description='**__Information Commands__**')
        embed.add_field(name='```Info```', value='Displays the bots information.')
        embed.add_field(name='```Userinfo @member```', value='Displays your or another users information.')
        embed.add_field(name='```avatar [member]```', value='Shows another persons avatar.')

        await ctx.author.send(embed=embed)

    @help.command(aliases=['levels'])
    async def Levels(self, ctx):
        embed = discord.Embed(color=discord.Color.red(), description='**__Level Commands__**')
        embed.add_field(name='```COMING SOON```', value='**COMING SOON**')

        await ctx.author.send(embed=embed)

# Setting up the cog
def setup(bot):
    bot.add_cog(Help(bot))
    print('Help is loaded.')

def teardown(bot):
    bot.remove_cog(Help(bot))
    print('Help is unloaded.')
