import discord
from discord.ext import commands
import asyncio
from random import choice
import discord
import random
from discord.ext import commands
from random import choice

class AdminCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lockdown(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        role = ctx.guild.default_role

        if role not in channel.overwrites:
            overwrites = {
                role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            if ctx.channel != channel:
                await ctx.send(f"I have put {channel.mention} on lockdown.")
            else:
                await ctx.message.delete()
            await channel.send(embed=discord.Embed(title="This channel is now under lockdown", color=discord.Colour.orange()))
        elif channel.overwrites[role].send_messages is True or \
                channel.overwrites[role].send_messages is None:
            overwrites = channel.overwrites[role]
            overwrites.send_messages = False
            await channel.set_permissions(role, overwrite=overwrites)
            if ctx.channel != channel:
                await ctx.send(f"I have put {channel.mention} on lockdown.")
            else:
                await ctx.message.delete()
            await channel.send(embed=discord.Embed(title="This channel is now under lockdown.", color=discord.Colour.orange()))
        else:
            overwrites = channel.overwrites[role]
            overwrites.send_messages = True
            await channel.set_permissions(role, overwrite=overwrites)
            if ctx.channel != channel:
                await ctx.send(f"I have removed {channel.mention} from lockdown.")
            else:
                await ctx.message.delete()
            await channel.send(embed=discord.Embed(title="This channel is no longer under lockdown.", color=discord.Colour.orange()))


    async def on_voice_state_update(self, member, before, after):
        if not self.active: return
        if not member.id == self.bot.user.id: return
        if before.channel == after.channel: return
        if self.allowed: self.allowed = False; return
        try:
            self.allowed = True
            await member.move_to(before.channel)
            print("Someone tried to move u from \"{b}\" to \"{a}\" on guild \"{s}\" lol imagine ".format(b=before.channel,a=after.channel,s=member.guild.name))
        except discord.Forbidden:
            print("Insufficient permissions to move yourself back to \"{n}\" on server lol fucking loser got removed \"{s}\"".format(n=before.channel,s=member.guild.name))
            self.allowed = False

    @commands.command()
    async def emojis(self, ctx):
        for emoji in ctx.guild.emojis:
            await asyncio.sleep(0.6)
            await ctx.send(f':{emoji.name}:\t{emoji.id}')

    @commands.command
    async def quote(self, ctx):
        """Get a random quote from the quote board."""
        quotes_channel = ctx.guild.get_channel(868249377553121361)
        quotes = []
        async for message in quotes_channel.history():
            quotes.append((message.content, message.author))
        quote, author = choice(quotes)
        await ctx.send(quote)
        await ctx.send(f"Contributed by {author}.")

    @commands.command(aliases=["Choose"])
    async def choose(self, ctx, *, choices: str):
        """Chooses one from many possibilities."""
        choiceslist = choices.split("|")
        choice = random.choice(choiceslist)
        if len(choiceslist) < 2:
            await ctx.send(ctx, content="2+ Options, separated with ``|``",  ttl=5)
        else:
            em = discord.Embed(colour=any(self))
            em.add_field(name="Options", value=choices, inline=False)
            em.add_field(name="Choice", value="<:clyde:273922151856209923> | My Answer is ``{}``".format(choice))
            await ctx.send(ctx, embed=em)

    @commands.command()
    async def bans(self, ctx):
        '''See a list of banned users in the guild'''
        try:
            bans = await ctx.guild.bans()
        except:
            return await ctx.send('You dont have the perms to see bans.')

        em = discord.Embed(title=f'List of Banned Members ({len(bans)}):')
        em.description = ', '.join([str(b.user) for b in bans])

        await ctx.send(embed=em)






def setup(client):
    client.add_cog(AdminCommands(client))