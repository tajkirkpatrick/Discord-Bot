import json
import os
from datetime import datetime

import discord
from discord.ext import commands

# TODO : Left off inside of schedule, need to recognize games happening yesterday & tomorrow relative to datetime.now()


class NBA(commands.Cog):

    def __init__(self, bot):
        self.__name__ = "NBA Extension"
        self.bot = bot
        self.schedule_array = []

    # * Listeners
    @commands.Cog.listener()
    async def on_ready(self):
        self.load_schedule()
        print(f'loaded cog: {self.__name__}')

    # * Commands
    @commands.command()
    async def schedule(self, ctx):
        today = datetime.now().date()
        today_str = today.strftime("%B %-d, %Y")
        today_compare = today.strftime("%Y-%m-%d")

        await ctx.send(f"Today's Date: {today_str}")

        for game in self.schedule_array:
            if game['date'] == today_compare:
                print(game)

        await ctx.send("Butler is working on the output")

    #  * Helpers
    def load_schedule(self):
        with open(os.path.join(os.path.dirname(__file__), 'assets/min_schedule.json')) as infile:
            data = json.load(infile)

            for game in data:
                self.schedule_array.append(game)


def setup(bot):
    bot.add_cog(NBA(bot))
