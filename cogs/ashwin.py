import discord
from discord.ext import commands
from util.llmrequest import run


class AshwinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def orca(self, ctx):
        await ctx.send("Generating message")
        result = run("this is an orca prompt")

        await ctx.send(result)
        
    

def setup(bot):
    bot.add_cog(AshwinCog(bot))
