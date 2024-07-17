# Discord Message Chomper
## Description
A Discord bot written in Python made only to eat a channel's messages one by one.  
Commands are explained in the [Commands](#discord--commands) section.

**Be careful when setting up the bot's permissions and channels as it will delete ALL messages one by one, or until stopped.**

## Setup
Clone this repository with the following command:
```
git clone https://github.com/DreWulff/DiscordMessageChomper
```

Make sure all libraries/modules required are installed.

Create a .env file with the next lines, replacing the values in brackets:
```
#.env
DISCORD_TOKEN=[Token from your Discord bot]
DISCORD_GUILD=[Name of Discord server]
```

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
