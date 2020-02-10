import discord
import datetime
from discord.ext import commands, tasks
from discord.utils import get, find

class Information(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot


    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(color=discord.Color.teal(), description=f'Bot Information')
        embed.add_field(name='Version', value='1.0.0')

        embed.add_field(name='Made By', value='Tadeo#6871')
        embed.add_field(name='Started On', value='November 14, 2019')
        embed.add_field(name='Running On', value='Manual labour')

        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(color=discord.Color.teal(), timestamp=ctx.message.created_at)

        embed.set_author(name=f'User Info - {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name='ID:', value=member.id)

        embed.add_field(name='Created At:', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p "))
        embed.add_field(name='Joined At:', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p "))

        embed.add_field(name=f'Roles ({len(roles)})', value=" ".join([role.mention for role in roles]))
        embed.add_field(name='Highest Role:', value=member.top_role.mention)

        await ctx.send(embed=embed)

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        
        embed = discord.Embed(color=discord.Color.teal())
        embed.set_author(name=f'{member}')
        embed.set_image(url=f'{member.avatar_url}')
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Information(bot))
    print('Information is loaded.')
