# ATbot - Discord Real-Time Translator 🦊

AT-bot (Asha's Translation Bot) is a Discord bot auto-hosting solution that provides real-time message translation capabilities using both DeepL and Google Translate APIs. Contrary to other 'black box' bots, i here focus on transparency and userdata control.

## Architecture & Logic

The bot uses a hybrid translation system to ensure maximum reliability:

* **DeepL Priority:** Leverages the DeepL API for superior contextual accuracy.
* **Google Translate Fallback:** If DeepL limits are reached or unconfigured, the bot automatically switches to Google Translate to maintain service continuity.
* **Multi-Config Engine:** Manage multiple bot instances or profiles directly through the built-in TUI at startup. (using Curses and Textuals)

## Features

* **Reaction-Based Translation:** React with a flag emoji (e.g., 🇫🇷, 🇺🇸, 🇯🇵) to receive an instant translation via DM.
* **Slash Command /trsend:** Send translated messages directly into a channel with full language autocompletion.
* **[HOST] Integrated TUI (Terminal User Interface):** An interactive setup wizard for first-time launches (no manual .env or .json editing required).
* **[HOST] Advanced Logging:** Comprehensive traceability for debugging and monitoring API calls.

## Prerequisites

Before installing ATbot, make sure you have:

- Windows operating system
- Python 3.8 or higher installed (Tested on Python 3.10.11 & 3.9.25)
- A Discord bot token ([How to get one](https://www.writebots.com/discord-bot-token/))
- A DeepL API key ([How to get one](https://support.deepl.com/hc/en-us/articles/360020695820-Authentication-Key))

## Installation (Windows & Unix-like systems)

* **Download:** Grab the [latest release](https://github.com/Natpol50/AT-bot/releases).
* **Launch:** Run `Start bot.bat`(windows) or `StartBot.sh` depending on your system
* **Setup Wizard:** Follow the terminal prompts to:
  * Name your configuration.
  * Link your Discord Token.
  * Add your DeepL API key (optional but recommended).

* **Technical Note:** On the first run, the script verifies the environment and installs necessary dependencies. If the process hangs, delete the Firstboot.flag file and restart.

## Roadmap & Future Evolutions
- [ ] **Webhook Mirroring:** Linking two channels for automatic bi-directional translation using Webhooks.
- [ ] **Translation Cache:** Implementing a SQLite database to cache frequent translations and save API quotas.
- [ ] **Cross-Platform Support:** Official Linux port (Dockerization planned).
- [ ] **Context Menu Integration:** Adding a "Translate" option via the Discord right-click menu (Apps).


## Basic troubleshooting

If you encounter issues:

1. Check if all prerequisites are installed
2. Verify your bot token and DeepL API key are valid
3. Ensure your bot has proper permissions in Discord
4. Check the logs folder for detailed error messages

## Logs

The bot automatically creates log files in the `logs` folder with timestamps. These can be useful for troubleshooting issues.

## Support

If you encounter any problems and chacked the Basic troubleshooting:
1. Check the [GitHub Issues](https://github.com/Natpol50/AT-bot/issues) page
2. Create a new issue with detailed information about your problem

If you have an idea not yet in the roadmap or find a bug:
1. Check existing Issues.
2. Open a new Issue with detailed information about your proposal.


## Credits

Created and maintained by Asha Geyon (Natpol50) 🦊


## License
This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0) - see the LICENSE file for details.
This means you are free to:

Share: Copy and redistribute the material in any medium or format
Adapt: Remix, transform, and build upon the material for any purpose, even commercially

Under these terms:

Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made
ShareAlike: If you modify the material, you must distribute your contributions under the same license as the original
