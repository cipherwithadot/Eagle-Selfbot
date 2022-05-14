import discord
from discord.ext import commands
import random
import discord
from random import randint
from discord.ext import commands
import inspect
class textemotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def cookie(self, ctx):
        """🍪 roblosecurity cookie lol"""
        await ctx.message.edit(content="(  ' - ')-🍪")


    @commands.command(aliases=['mn'], pass_context=True)
    async def massnick(self, ctx, onlineonly: bool = False, *, newnick = None):
        """Changes the nickname of all users of the current guild to [newnick]
        Use it a second time to revert all nicknames with a 1 second delay"""
        print('Massnick active on Guild \"%s\" for %s members.'%(self.guild.name, len(self.users)) if self.active else 'Massnick inactive.')
        if not self.active:
            self.guild = ctx.message.guild
            for member in ctx.message.guild.members:
                if onlineonly and member.status == discord.Status.offline: continue
                if member.nick == newnick: continue
                try:
                    _nick = member.nick
                    await member.edit(nick=newnick)
                    self.users[member.id] = _nick
                    print("Saved {n}'s nick as {o}".format(n=member.name,o=member.nick))
                except discord.Forbidden: print("Unable to change {n}'s nick to {o}".format(n=member.name,o=member.nick))
            if len(self.users) == 0: return
            print(self.users)
            self.active = True
        else:
            self.active = False
            for id, oldnick in self.users.items():
                try:
                    if self.guild.get_member(id).nick == oldnick: continue
                except: pass
                try:
                    await self.guild.get_member(id).edit(nick=oldnick)
                    print("Reset {n}'s nick to {o}".format(n=self.guild.get_member(id).name,o=oldnick))
                except discord.Forbidden: print("Unable to reset {n}'s nick to {o}".format(n=self.guild.get_member(id).name,o=oldnick))


    @commands.command()
    async def magic(self, ctx):
        """(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ"""
        await ctx.message.edit(content="(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ")

    @commands.command()
    async def wtf(self, ctx):
        """Ծ_Ծ"""
        await ctx.message.delete()
        await ctx.send("Ծ_Ծ")


    @commands.command()
    async def angrytableflip(self, ctx):
        """(ノಠ益ಠ)ノ彡┻━┻"""
        await ctx.message.delete()
        await ctx.send("(ノಠ益ಠ)ノ彡┻━┻")

    @commands.command()
    async def lenny(self, ctx):
        """( ͡° ͜ʖ ͡°)"""
        await ctx.message.edit(content="(( ͡° ͜ʖ ͡°)")



    @commands.command()
    async def crosseye(self, ctx):
        await ctx.message.edit(content=("(◑‿◐)"))

    @commands.command()
    async def lenny(self, ctx):
        await ctx.message.edit(content="( ͡ᵔ ͜ʖ ͡ᵔ )")


    @commands.command()
    async def gunlenny(self, ctx):
        await ctx.message.edit(content="ᕦ(▀̿ ̿ -▀̿ ̿ )つ/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿")

    @commands.command()
    async def beamed(self, ctx):
        """((   ◑‿◐))>-- get beaameddd LMFAO"""
        await ctx.message.edit(content="(((   ◑‿◐))>-- get beaameddd LMFAO")



    @commands.command()
    async def source(self, ctx, *, command):
        '''See the source code for any command.'''
        source = str(inspect.getsource(self.bot.get_command(command).callback))
        fmt = '```py\n' + source.replace('`', '\u200b`') + '\n```'
        if len(fmt) > 2000:
            async with ctx.session.post("https://hastebin.com/documents", data=source) as resp:
                data = await resp.json()
            key = data['key']
            return await ctx.send(f'Command source: <https://hastebin.com/{key}.py>')
        else:
            return await ctx.send(fmt)



    @commands.command()
    async def basedcow(self, ctx):
        cnt = """```
 __________
 |        |
 | Fuck   |
 | blacks |
 |        |
 ¯¯¯¯¯¯¯¯¯¯
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
 ```"""

        em = discord.Embed(color=random.randint(0, 0xFFFFFF))
        em.description = cnt
        await ctx.send(embed=em)
        await ctx.message.delete()
        



def setup(bot):
    bot.add_cog(textemotes(bot))
