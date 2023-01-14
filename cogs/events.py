import disnake 
import requests
from disnake.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Account: {self.bot.user}")
        print(f"ID: {self.bot.user.id}")

def setup(bot):
    bot.add_cog(Events(bot))