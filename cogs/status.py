import discord, random, aiohttp
from discord import Permissions
from discord.ext import commands


class Status(commands.Cog):
      def __init__(self, client):
            self.client = client
            self.colors = [0xffb2a3,0xff00ee]

      @commands.command(aliases=['playing'])
      async def play(self, ctx, *, text):
       await ctx.message.delete()
       await self.client.change_presence(activity=discord.Game(name = text))
       embed = discord.Embed(description = f"**{ctx.author.mention}, Is now Playing {text}**", color=random.choice(self.colors))
       await ctx.send(embed=embed)

      @commands.command(aliases=['watching'])
      async def watch(self, ctx, *, text):
       await ctx.message.delete()
       await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= text))
       embed = discord.Embed(description = f"**{ctx.author.mention}, Is now Watching {text}**", color=random.choice(self.colors))
       await ctx.send(embed=embed)

      @commands.command(aliases=['listening'])
      async def listen(self, ctx, *, text):
        await ctx.message.delete()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name= text))
        embed = discord.Embed(description = f"**{ctx.author.mention}, Is Now To Listening {text}**", color=random.choice(self.colors))
        await ctx.send(embed=embed)

      @commands.command(aliases=['reset'])
      async def stop(self, ctx):
       await ctx.message.delete()
       await self.client.change_presence(activity=None, status=discord.Status.dnd)
       embed = discord.Embed(description = f"**{ctx.author.mention}'s Status Has Reset**", color=random.choice(self.colors))
       await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Status(client))