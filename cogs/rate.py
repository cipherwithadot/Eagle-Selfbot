import discord, random
from discord.ext import commands

class Fun(commands.Cog):
      def __init__(self, client):
            self.client = client
            self.colors = [0xffb2a3,0xff00ee]


            

    
      @commands.command(aliases=["gr", "homo"])
      async def gayrate(self, ctx, member: discord.Member = None):
            member = ctx.author if not member else member
            kojimu = random.randint(0, 100)
            if member == None:
                  embed = discord.Embed(
                  description=f"{kojimu}% gay", color=random.choice(self.colors))
                  embed.set_author(name=f"{ctx.author} is", icon_url=ctx.author.avatar_url)
                  embed.set_footer(text=f"requested by {ctx.author}")
                  await ctx.send(embed=embed)

            embed = discord.Embed(
                   description=f"{kojimu}% gay", color=random.choice(self.colors))
            embed.set_author(name=f"{member.name} is", icon_url=member.avatar_url)
            embed.set_footer(text=f"requested by {ctx.author}")
            await ctx.send(embed=embed)
                  



      
def setup(client):
    client.add_cog(Fun(client))