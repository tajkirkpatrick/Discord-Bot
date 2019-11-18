import discord
from discord.ext import commands
import os
import json


class NBA(commands.Cog):
    def __init__(self, bot):
        self.__name__ = "NBA Extension"
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'loaded cog: {self.__name__}')
        self.load_schedule()

    # * Helpers

    def load_schedule(self):
        with open(os.path.join(os.path.dirname(__file__), 'assets/min_schedule.json')) as infile:
            data = json.load(infile)

            for game in data:
                if game['date'] == '2019-11-17':
                    print(game)


def setup(bot):
    bot.add_cog(NBA(bot))
