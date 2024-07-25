# bot.py
# Python libraries
import os
import asyncio
from datetime import datetime, timedelta, timezone

# External libraries
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord.app_commands import Choice

# .env variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Variables for bot initialization
INTENTS = discord.Intents.default()
INTENTS.message_content = True
BOT = commands.Bot(command_prefix="!", intents=INTENTS)
CHOMPING=False

@BOT.event
async def on_ready():
    try:
        synced = await BOT.tree.sync()
        print(f"Synced {len(synced)} commands(s).")
    except Exception as exception:
        print(exception)

@app_commands.describe(rate="Chomping rate [chomps/s]. Min: 1; Max: 3")
@BOT.tree.command(name="chomp", description="Chomps messages at desired rate [chomps/s].")
async def chomp(interaction: discord.Interaction, rate: int = 1):
    global CHOMPING
    print("Chomping...")
    now = datetime.now()
    rate = 3 if rate > 3 else rate
    rate = 1 if rate < 1 else rate
    async for guild in BOT.fetch_guilds(limit=None):
        channel = [channel for channel in await guild.fetch_channels() if channel.name == interaction.channel.name][0]
        try:
            await interaction.response.send_message("**OM NOM NOM NOM NOM!**")
            CHOMPING=True
            async for message in channel.history(limit=None, oldest_first=False):
                if (not CHOMPING): break
                if (((datetime.utcnow().replace(tzinfo=None) - message.created_at.replace(tzinfo=None) > timedelta(minutes=1)) or (message.author != BOT.user)) and (not message.pinned)):
                    print("Chomped! -> " + message.content)
                    await message.delete()
                    await asyncio.sleep(1.0/rate)  # Avoid rate limits
        except discord.Forbidden:
            print(f"Permission error in channel {channel.name}")
        except discord.HTTPException as e:
            print(f"HTTP error in channel {channel.name}: {e}")
        CHOMPING=False

@BOT.tree.command(name="shut", description="Stops the CHOMP.")
async def shut(interaction: discord.Interaction):
    global CHOMPING
    if (not CHOMPING):
        await interaction.response.send_message("**???**", ephemeral=True)
    else:
        CHOMPING=False
        await interaction.response.send_message("**MMMM DELICIOUS**", ephemeral=True)

BOT.run(TOKEN)