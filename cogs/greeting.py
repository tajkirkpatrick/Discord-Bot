import discord
from discord.ext import commands


class Greeting(commands.Cog):

    def __init__(self, bot):
        self.__name__ = "Greeting Extension"
        self.bot = bot

    # * Listeners
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'loaded cog: {self.__name__}')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention} to GANG MEMBERS on Discord.\n I am Butler, the GANG Butler'.format(member))

    # * Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')


def setup(bot):
    bot.add_cog(Greeting(bot))
