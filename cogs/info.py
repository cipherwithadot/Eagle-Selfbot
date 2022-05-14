import discord
from datetime import datetime, timezone
from discord.ext import commands
boi = 0x2f3137


class lookup(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='inv')
    async def inv(self, ctx):
        print('inv link generated')
        embed = discord.Embed(
            title="use this sellfbot",
            description=" [__download!__](https://github.com/tobbyy/selfbot)",
            color=boi,
            timestamp=datetime.now(),
        )
        embed.set_footer(text="star")
        await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        kekw = "%a , %d %b %Y %I:%M %p"
        ogornah = sorted(ctx.guild.members, key=lambda member: member.joined_at).index(member) + 1
        role = [role for role in member.roles]
        thefuckingembedretardedassdiscord = discord.Embed(timestamp=ctx.message.created_at, color=boi)
        thefuckingembedretardedassdiscord.set_author(name=str(member), icon_url=member.avatar_url)
        thefuckingembedretardedassdiscord.set_thumbnail(url=member.avatar_url)

        thefuckingembedretardedassdiscord.add_field(name="ID:", value=member.id, inline=False)
        thefuckingembedretardedassdiscord.add_field(name="Display Name:", value=member.display_name, inline=False)

        thefuckingembedretardedassdiscord.add_field(name="Registered", value=member.created_at.strftime(kekw), inline=False)
        thefuckingembedretardedassdiscord.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                        inline=False)
        thefuckingembedretardedassdiscord.add_field(name="Position:", value=f"{ogornah}/{len(ctx.guild.members)}", inline=False)

        thefuckingembedretardedassdiscord.add_field(name="Roles:", value="".join([role.mention for role in role]), inline=False)
        thefuckingembedretardedassdiscord.add_field(name="Highest Role:", value=member.top_role.mention, inline=False)
        thefuckingembedretardedassdiscord.set_footer(text=f"𝙧𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙙 𝙗𝙮 {ctx.author.name}", icon_url=ctx.author.avatar_url)
        print(member.top_role.mention)
        await ctx.send(embed=thefuckingembedretardedassdiscord)

    @commands.command()
    async def serverinfo(self, ctx):
        thefuckingname = ctx.guild.name
        create_server = ctx.guild.created_at
        owner_server = ctx.guild.owner
        server = ctx.message.guild
        role_count = len(server.roles)
        emoji_count = len(server.emojis)
        channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])

        em = discord.Embed(timestamp=ctx.message.created_at, color=boi)
        em.set_author(name=str(thefuckingname), icon_url=ctx.guild.icon_url)
        em.set_thumbnail(url=ctx.guild.icon_url)

        em.add_field(name="Owner", value=owner_server, inline=False)
        em.add_field(name='Region', value=server.region, inline=False)
        em.add_field(name='Members', value=server.member_count, inline=False)
        em.add_field(name="Created On", value=create_server.strftime("%a, %#d %B %Y"), inline=False)
        em.add_field(name='Text Channels', value=str(channel_count), inline=False)
        em.add_field(name='Number of Roles', value=str(role_count))
        em.add_field(name='Number of Emotes', value=str(emoji_count))

        await ctx.send(embed=em)


def setup(client):
    client.add_cog(lookup(client))