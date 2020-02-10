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


class Moderation(commands.Cog):


    def __innit__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        role = get(member.guild.roles, name='Duck')
        if role in member.roles:
            await ctx.send("Cannot ban that user, try again.")
        else:            
            await ctx.message.delete()
            await member.kick(reason=reason)
            embed = discord.Embed(color=discord.Color.green(), description='Kick Results')
            embed.add_field(name='Successfully kicked', value=f'{member.name}')

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        role = get(member.guild.roles, name='LA_Staff')
        if role in member.roles:
            await ctx.send("Cannot ban that user, try again.")
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(color=discord.Color.green(), description='Ban')
            embed.add_field(name='User has succesfully been banned.', value="Shouldn't have done what you did!")

            await ctx.send(embed=embed)

            await member.send(f"You have been banned in {member.guild}, if you wish to appeal, DM WispyTheDuck#1615.")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to ban people / that user cannot be banned.")


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(color=discord.Color.teal(), description='Unban')
                embed.add_field(name=f'Unbanned {user.name}#{user.discriminator}', value='Welcome Back')

                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, role: discord.Role):
        if role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(color=discord.Color.orange())
            embed.add_field(name="`Role Update`", value=f'{member.name}#{member.discriminator} has been altered.')
            embed.add_field(name='Role: ', value=f'-{role}')

            await ctx.send(embed=embed)
        else:
            await member.add_roles(role)
            embed = discord.Embed(color=discord.Color.orange())
            embed.add_field(name="`Role Update`", value=f'{member.name}#{member.discriminator} has been altered.')
            embed.add_field(name='Role: ', value=f'+{role}')

            await ctx.send(embed=embed)
                                                            


def setup(bot):
    bot.add_cog(Moderation(bot))
    print('Moderation is loaded.')
    print('----------')

def teardown(bot):
    bot.remove_cog(Moderation(bot))
    print('Moderation is unloaded.')
