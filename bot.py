# Python libraries
import os
import asyncio

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

@BOT.tree.command(name="chomp", description="Chomps messages at 1[message/s].")
async def chomp(interaction: discord.Interaction):
    global CHOMPING
    if (CHOMPING):
        await interaction.response.send_message("**OM NOMING ALREADY**", ephemeral=True)
    else:
        channel = interaction.channel
        try:
            await interaction.response.send_message("**OM NOM NOM NOM NOM!**", ephemeral=True)
            CHOMPING=True
            async for message in channel.history(limit=None, oldest_first=False):
                if (not CHOMPING): break
                if (not message.pinned):
                    print("Chomped! -> " + message.content)
                    await message.delete()
                    await asyncio.sleep(1.0)
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