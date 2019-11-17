import discord
from discord.ext import commands


class NBA(commands.Cog):
    def __init__(self, bot):
        self.__name__ = "NBA Extension"
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'loaded cog: {self.__name__}')


def setup(bot):
    bot.add_cog(NBA(bot))
