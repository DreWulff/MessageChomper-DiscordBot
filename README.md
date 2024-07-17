# Discord Message Chomper
## Description
A Discord bot written in Python made to eat a channel's messages one by one.  
Commands are explained in the [Commands](#discord--commands) section.

**Be careful when setting up the bot's permissions and channels as it will attempt to delete ALL messages one by one, unless stopped with the /shut command.**

## Setup
Clone this repository with the following command:
```
git clone https://github.com/DreWulff/MessageChomper-DiscordBot
```

Make sure all libraries/modules required are installed.

Create a .env file with the next lines, replacing the values in brackets:
```
#.env
DISCORD_TOKEN=[Token from your Discord bot]
DISCORD_GUILD=[Name of Discord server]
```

To obtain the token you must first have a Discord app/bot. To get started I would recommend to follow the official Discord Developer Portal documentation in [Building your first Discord app](https://discord.com/developers/docs/quick-start/getting-started).

## Run
To start the bot execute the command:
```
python bot.py
```

## Discord `/` Commands
* `/chomp [rate=1]`:
  * Starts deleting messages from newest to oldest at desired rate.
  * Rate of deleted messages will stay in the range between 1 and 3 messages per second.

* `/shut`:
  * Stops the deletion of messages.
