# ATbot - Discord Auto Translation Bot 🦊

Asha's Translation bot (or auto if you don't want my name here) is a Discord bot that provides real-time message translation capabilities using both DeepL and Google Translate APIs. It allows users to easily translate messages by either using commands or reacting with country flag emojis.


## Features

- Free
- Easily hostable
- Translation using the `/trsend` slash command
- Translation by reacting with country flag emojis
- Supports multiple bot configurations
- Uses DeepL API for higher quality translations when available
- Falls back to Google Translate if needed
- Built-in language autocompletion


## Coming soon

- More translations APIs
- A GUI
- Code overhaul someday
- Macos and Linux support
- Auto updates
- Please, request features, i've ran out of ideas


## Prerequisites

Before installing ATbot, make sure you have:

- Windows operating system
- Python 3.8 or higher installed (Tested on Python 3.10.11)
- A Discord bot token ([How to get one]([https://rapidapi.com/volodimir.kudriachenko/api/DiscordBot/details](https://www.writebots.com/discord-bot-token/)))
- A DeepL API key ([How to get one](https://support.deepl.com/hc/en-us/articles/360020695820-Authentication-Key))

## Installation

1. Download the latest release from [GitHub Releases](https://github.com/Natpol50/AT-bot/releases)
2. Extract the ZIP file to your desired location
3. Double-click `Start bot.bat` to launch the bot
   - On first run, the bot should install required dependencies, if error occurs. Please delete Firstboot.flag and restart the bot.
   - Follow the setup wizard to configure your bot token and DeepL API key

## Configuration

When you first run the bot, you'll need to:

1. Choose "New bot/config" when prompted
2. Enter a name for your configuration
3. Input your Discord bot token
4. Input your DeepL API key

The bot will verify both keys and save your configuration for future use.

## Usage

### Slash Command Translation
Use the `/trsend` command with the following parameters:
- `message`: The text you want to translate
- `language`: The target language (with autocompletion support)

Example:
```
/trsend message:Asha is an happy fox language:French
```

### Flag Reaction Translation
1. React to any message with a country flag emoji
2. The bot will send you a DM containing:
   - The original message
   - The translation
   - The translator used (DeepL or Google Translate)

## Multiple Bot Configurations

You can set up multiple bot configurations by:
1. Running `start_bot.bat`
2. Selecting "New bot/config"
3. Following the setup process for each new configuration

## Troubleshooting

If you encounter issues:

1. Check if all prerequisites are installed
2. Verify your bot token and DeepL API key are valid
3. Ensure your bot has proper permissions in Discord
4. Check the logs folder for detailed error messages

## Logs

The bot automatically creates log files in the `logs` folder with timestamps. These can be useful for troubleshooting issues.

## Support

If you encounter any problems:
1. Check the [GitHub Issues](https://github.com/Natpol50/AT-bot/issues) page
2. Create a new issue with detailed information about your problem

## Credits

Created by Asha Geyon (Natpol50) 🦊

## License
I'd like to put it under CC-BY-SA , i'll look further into it someday
