import discord
import random
from discord.ext import commands, tasks
from discord.utils import get, find


class Misc(commands.Cog):

    def __innit__(self, bot):
     self.bot = bot


    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good."]
        embed = discord.Embed(color=discord.Color.teal(), description='8ball result')
        embed.add_field(name='Results', value=f'Question: {question}\nAnswer: {random.choice(responses)}')

        await ctx.send(embed=embed)

    @commands.command(aliases=['roll', 'dice'])
    async def rolldice(self, ctx):
        numbers = [
                   "1",
                   "2",
                   "3",
                   "4",
                   "5",
                   "6"]
        embed = discord.Embed(color=discord.Color.teal(), description='Rolldice')
        embed.add_field(name='You got: ', value=f'{random.choice(numbers)}')

        await ctx.send(embed=embed)

    @commands.command(aliases=['cf', 'flip', 'coin'])
    async def coinflip(self, ctx):
        coin = [
                "heads",
                "tails"]
        embed = discord.Embed(color=discord.Color.teal(), description='Coinflip')
        embed.add_field(name='Results: ', value=f'{random.choice(coin)}')
        await ctx.send(embed=embed)

    @commands.command()
    async def duck(self, ctx):
        embed = discord.Embed(color=discord.Color.teal(), description='The duck song')
        embed.add_field(name='LinK: ', value='https://youtu.be/MtN1YnoL46Q')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))

def teardown(bot):
    bot.remove_cog(Misc(bot))



