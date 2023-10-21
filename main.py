import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from cogs.ashwin import AshwinCog
from cogs.greeting import ExampleCog

# Load the env file
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.add_cog(ExampleCog(bot));
    await bot.add_cog(AshwinCog(bot));


bot.run(os.getenv("DISCORD_TOKEN"))
