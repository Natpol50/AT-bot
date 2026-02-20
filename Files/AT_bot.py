# -----------------------------------------------------------------------------
#  AT_bot.py
#  Copyright (c) 2026 Asha the Fox 🦊
#  All rights reserved.
#
#  This is the main code for the ATbot project. 
#  The goal of ATbot is to give access to easy translation for free to as many people as possible.
#  To do so, the bot code is separated in multiple parts : 
#      Boot - All the parts dedicated to correctly starting the script.
#      Configuration - All the parts dedicated to configuring the bot.
#      bot loops - Ddefines all the bot looping tasks (or bootup ones)
#      Bot code - All the commands the bot does. 
#
# -----------------------------------------------------------------------------

__author__ = "Asha Geyon (Natpol50)"
__version__ = 1.5
__last_revision__ = '2026-02-20'

UPDATE_NOTICE = None
Dashboard_state = None
Dashboard_started = False


if __name__ != "__main__":
    print("This isn't a library module! What are you planning on doing?")

import os
import subprocess
import logging
import threading
import concurrent.futures
import sys


def clear_console() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def set_title(title: str) -> None:
    if os.name == "nt":
        os.system(f"title {title}")
    else:
        print(f"\33]0;{title}\a", end="", flush=True)




"""
//////////////////
///////BOOT///////
//////////////////
"""
# -----------------------------------------------------------------------------
#  AT_bot.py , boot
#  Copyright (c) 2024 Asha the Fox 🦊
#  All rights reserved.
#
#  This is the part of the script that check if everything's in order and then initialize logging.
#  It can also install the necessary packages if they are not installed.
#
#  Functions:
#      bootup_function() - Verifies if everything seems right for the script to run and initialize logging.
#
# -----------------------------------------------------------------------------

def bootup_function() -> bool:
    """
    Verifies if everything seems right for the script to run and initialize logging.
    
    This function will : 
     - Verify if the script has been used before (if not, installs the required libraries)
     - Initialize the logging

    It's also meant to verify if there's an update to the bot (coming soon)
    
    Args:
    - None
    
    Returns:
    - bool: wether the function finished correctly or not.
    """
    def log_init() -> bool:
        """
        Initialize logging for the script.
        Used after the first time setup flag has been checked

        Args:
        - None
    
        Returns:
        - bool: wether the function finished correctly or not.
        """
        try :
            import pathlib
            import datetime

            Log_folder = f'{pathlib.Path(__file__).parent.absolute()}/logs'

            if not os.path.exists(Log_folder):
                os.makedirs(Log_folder)

            Log_file = os.path.join(
                Log_folder,
                f"{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}.log"
            )

            logging.basicConfig(
                filename=Log_file,
                level=logging.INFO,
                format="%(asctime)s [%(levelname)s]: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            logging.info("Script started.")
            return True
        except Exception as e :
            return False        
    
    Flag_file = "Firstboot.flag"  # Flag to indicate first-time setup

    if not os.path.exists(Flag_file):
        import Dependency_installer as install

        Dependencies = [
            'discord.py==2.4.0',
            'googletrans==4.0.0-rc.1',
            'windows-curses==2.4.0',
            'Pillow==11.0.0',
            'deepl==1.19.1',
            'requests==2.32.3',
            'textual==0.76.0',
            'psutil==5.9.8'
        ]

        Total_size = 0
        Dependencies_to_install = []

        print("As this is the first time the script is running, Dependencies will be installed.")

        # Attempt to install pathlib separately, as pathlib is needed for the logging to work. (refer to log_init() function)
        try:
            subprocess.check_call(['pip', 'install', 'pathlib==1.0.1'])
        except subprocess.CalledProcessError as e:
            print(f"There was an error installing pathlib: {e}.")
            input("\nPress enter to open the bug report page [https://github.com/Natpol50/AT-bot/issues]")
            subprocess.run(['powershell', '-Command', f"start-Process {'https://github.com/Natpol50/AT-bot/issues'}"])
            input('Press enter to exit...')
            exit()

        log_init()
        del log_init
        logging.info("First-time setup, installing Dependencies")

        # Determine the size of each dependency and prepare the installation list
        for Dep in Dependencies:
            Dep_size = install.get_package_size(Dep)
            if Dep_size > 0:
                Dependencies_to_install.append(Dep)
            elif Dep_size == -1:
                print(f"Error retrieving size for package {Dep}")
            Total_size += Dep_size

        # Install thoses dependencies (OR NOT)
        if Dependencies_to_install:
            Option = input(
                f"You need to install these dependencies: {Dependencies_to_install}.\n"
                f"The total size is approximately {Total_size:.2f} MB.\n"
                "Do you wish to proceed (Y/N)? "
            )
            if Option.lower() not in ["y", "yes"]:
                exit()

            install.install_packages(Dependencies_to_install)
            
        del install
        # Create the flag file to indicate setup has been completed
        with open(Flag_file, "w") as File:
            File.write(
                "A simple flag indicating that the script has run before.\n"
                "Asha thanks you for reading this, but seriously, don't you have anything else to do?"
            )
        return True
        
    else:
        log_init()
        logging.info("Script has already run before, skipping dependency installation.")
        return True




def check_for_update() -> None:
    global UPDATE_NOTICE

    def parse_version(value: str) -> tuple:
        import re

        parts = re.findall(r"\d+", value)
        if not parts:
            return (0,)
        return tuple(int(p) for p in parts)

    VERSION_URL = "https://api.github.com/repos/Natpol50/AT-bot/releases/latest"
    try:
        response = requests.get(
            VERSION_URL,
            headers={"Accept": "application/vnd.github+json", "User-Agent": "ATbot"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        remote_tag = data.get("tag_name") or data.get("name") or ""
        remote_version = parse_version(remote_tag)
        local_version = parse_version(str(__version__))

        if remote_version > local_version:
            UPDATE_NOTICE = (
                f"A new version is available: {remote_tag} (current v{__version__}). "
                "Download from https://github.com/Natpol50/AT-bot/releases"
            )
            logging.warning(UPDATE_NOTICE)
    except requests.RequestException as e:
        print(f"There was an error while checking for new versions: {e}")
        logging.warning(f"There was an error while checking for new versions: {e}")


"""
///////////////////////////////////////////////////
/////// Configuration,bootup and setting up ///////
///////////////////////////////////////////////////
"""
# -----------------------------------------------------------------------------
#  AT_bot.py , config
#  Copyright (c) 2024 Asha the Fox 🦊
#  All rights reserved.
#
#  This is the part of the script that'll make the user choose a configuration and allows the bot to boot.
#
#  Functions:
#      bot_picker(input_list: list) - Displays a CLI menu to choose an item from the input_list using the curses library.
#      config_init() - Sets up the configuration file for ATbot.
#      setup_environment() - Sets up the initial environment for the ATbot configuration.

#
# -----------------------------------------------------------------------------

if bootup_function():
    import discord
    from discord.ext import commands , tasks
    import deepl
    from discord.interactions import Interaction
    from googletrans import Translator
    import typing
    from Lists import *
    import configparser
    import curses
    import Tokenverif
    from io import BytesIO
    from PIL import Image
    import asyncio
    import pathlib
    import datetime
    import Displays
    import requests
    import Dashboard
else:
    print("Initialization failed!")
    logging.critical("Initialization failed !")
    exit(1)


def bot_picker(input_list: list) -> str:
    """
    Displays a CLI menu to choose an item from the input_list using the curses library.

    Args:
    - input_list(list): A list of strings to be displayed as selectable options.

    Returns:
    - str: The selected item from the input_list.
    """

    # Initialize the curses environment
    Stdscr = curses.initscr()
    curses.cbreak()  # Disable line buffering
    Stdscr.keypad(True)  # Enable special keys (e.g., arrow keys)
    curses.noecho()  # Do not display typed characters

    Selected_index = 0  # Track the currently selected Index

    try:
        while True:
            Stdscr.clear()  # Clear the screen
            
            # Display instruction text
            Stdscr.addstr("\nChoose a bot/config, or choose 'New bot/config' to create a new bot/config.\n\n")

            # Display the list with one element highlighted
            for Index, Element in enumerate(input_list):
                if Index == Selected_index:
                    Stdscr.addstr(f"{Index + 1}. {Element}\n", curses.A_REVERSE)  # Highlight selected item
                else:
                    Stdscr.addstr(f"   {Element}\n")

            Stdscr.refresh()  # Refresh the screen to reflect changes

            Key = Stdscr.getch()  # Get user input

            # Navigate through the list, gosh i'd like to have a case statement in python
            if Key == curses.KEY_DOWN:
                Selected_index = min(Selected_index + 1, len(input_list) - 1)
            elif Key == curses.KEY_UP:
                Selected_index = max(Selected_index - 1, 0)
            elif Key == 10:  # Enter key
                break  # Exit the loop to return the selected item

    finally:
        # Cleans up the curses environment
        curses.endwin()

    return input_list[Selected_index]

def config_init() -> None:
    """
    Sets up the configuration file for ATbot, 
    it allows the user to select multiple profiles/config.
    
    Args:
    - None

    Returns:
    - None
    """
    # There, we initialise the configuration file, we must not forget to make it accessible from everything.
    global Config, Config_file
    Config = configparser.ConfigParser()
    Config_file = f'{pathlib.Path(__file__).parent.absolute()}/config.ini'

    if not os.path.exists(Config_file):
        with open(Config_file, 'w') as file:
            file.write(" ")  # Create an empty config file

def setup_environment() -> None:
    """
    Sets up the initial environment for the ATbot configuration.
    This includes creating a configuration file if it doesn't exist,
    allowing the user to pick or create a bot configuration, and verifying
    API keys for Discord and Deepl (We won't be needing a google translate one for now...).

    Args:
    - None

    Returns:
    - None
    """
    global Selected_bot


    # First, we welcome the user.
    Displays.Welcome()
    clear_console()  # Clear the screen
    
    # And then, ask the user which configuration he wanna use.
    set_title("ATbot - Config Picker")
    Config.read(Config_file)
    Bot_list = Config.sections()
    Bot_list.append('New bot/config')  # Adds a 'New bot/config' option, for multiple profiles.
    Selected_bot = bot_picker(Bot_list)
    print(" ")

    clear_console()

    if Selected_bot == 'New bot/config':
        # Handle new bot creation
        set_title("ATbot - New Bot/config")
        Selected_bot = input("Choose a name for the new bot/config: ")

        # First, we get and verify the discord bot API key.
        Displays.DS_api()
        Discord_key_valid = False
        while not Discord_key_valid:
            Discord_api_key = input("\nDiscord bot API key (token): ")
            print("Starting Discord token verification...")
            logging.info("Starting Discord token verification.")
            Discord_key_valid = Tokenverif.DS_token(Discord_api_key)
            if not Discord_key_valid :
                print('Please, provide a correct bot token')
        print("The token seems good, continuing...")
        logging.info("Token verification was successful, continuing...")

        # Then, we do the same thing with the Deepl one.
        Displays.DPL_api()
        Deepl_key_valid = False
        while not Deepl_key_valid:
            Deepl_api_key = input("\nDeepl API key: ")
            print("Starting Deepl token verification...")
            logging.info("Starting Deepl token verification.")
            Deepl_key_valid = Tokenverif.DPL_token(Deepl_api_key)
        print("The token seems good, continuing...")
        logging.info("Token verification was successful, continuing...\n")

        # And finally write the bot informations onto the config file.
        Config[f"{Selected_bot}"]={
        "discord" : Discord_api_key,
        "deepl" : Deepl_api_key
        }                               
        with open(Config_file,"w") as File_object:
            Config.write(File_object)

def bot_bootup(selected_bot, config_file, config) -> None:
    """
    Initializes and starts up the bot by performing the following tasks:
    1. Sets the console title and prints the configuration file location.
    2. Checks the connectivity to Discord's website.
    3. Retrieves API keys from the configuration file.
    4. Initializes Deepl and Google translators.
    5. Sets up the Discord bot with (what is think is) appropriate permissions and intents.

    Args:
    - selected_bot (str): The name of the bot to be started.
    - config_file (str): Path to the configuration file.
    - config (dict): Configuration dictionary containing API keys and other settings.

    Returns:
    - None

    Raises:
    - SystemExit: Exits the program if the request to Discord.com fails.

    
    """
    # Define global variables
    global Discord_api_key, Deepl_translator, Google_translator, bot, Startup_time
    Startup_time = datetime.datetime.now()

    # Set the console window title
    set_title(f"Bot : {selected_bot} , Starting...")

    # Print and log the configuration file path
    print(f'\nConfig file is {config_file}\n')
    logging.info(f'\nConfig file is {config_file}\n')

    # Test connectivity to Discord.com
    try:
        Response = requests.get("https://discord.com/", timeout=5)
        print("The request to Discord.com was successful\n")
    except Exception as e:
        print("The request to Discord.com was unsuccessful")
        logging.critical("Connection to discord.com was unsuccessful. The program will close.")
        logging.critical(f"Error code: {e}")
        print(f"Maybe bad internet? Error code: {e}")
        input("Press Enter to exit...")
        exit()

    # Retrieve API keys from the configuration file
    Discord_api_key = config.get(selected_bot, 'discord')
    Deepl_api_key = config.get(selected_bot, 'deepl')
    

    # Test API keys
    import Tokenverif

    if Tokenverif.DS_token(Discord_api_key) == False :
        print("The discord api key seems invalid")
        logging.critical("The discord api key seems invalid, closing program...")
        print(f"Maybe bad internet?")
        input("Press Enter to exit...")
        exit()
    elif Tokenverif.DPL_token(Deepl_api_key) == False :
        print("The deepl api key seems invalid ! Translation quality will lessen.")
        logging.warning("The deepl api key seems invalid. Not critical, just less quality. Continuing...")
        print(f"Maybe bad internet?")

    del Tokenverif
    
    # Initialize Deepl and Google translators
    Deepl_translator = deepl.Translator(Deepl_api_key)
    Google_translator = Translator()

    # Set up the Discord bot
    print(f"Running on discord.py version {discord.__version__}")
    logging.info(f"Running on discord.py version {discord.__version__}")

    Intents = discord.Intents.default()
    Intents.message_content = True
    Intents.reactions = True  # Set permissions for the bot

    bot = commands.Bot(command_prefix='ATbot.', intents=Intents)
    bot.remove_command('help')  # Remove the default help command


# First, we load everything to avoid any bot not defined error,
bootup_function()
del bootup_function
# Second, we check for any update
check_for_update()
del check_for_update
#Finally, we load the bot bootloader
config_init()

# Parse CLI arguments for auto-config selection
if len(sys.argv) > 1 and sys.argv[1].startswith("--config="):
    Selected_bot = sys.argv[1].split("=", 1)[1]
    Config.read(Config_file)
    if Selected_bot in Config.sections():
        logging.info(f"Using config from CLI: {Selected_bot}")
    else:
        print(f"Error: config '{Selected_bot}' not found.")
        print(f"Available configs: {Config.sections()}")
        exit(1)
else:
    setup_environment()

bot_bootup(Selected_bot,Config_file,Config)
Dashboard_state = Dashboard.DashboardState(state_path=pathlib.Path(__file__).parent / "dashboard_state.json")
Dashboard_state.load_from_file()
del bot_picker
del config_init
if 'setup_environment' in dir():
    del setup_environment

"""
//////////////////////
///////Bot loops///////
//////////////////////
"""
# -----------------------------------------------------------------------------
#  AT_bot.py , loops
#  Copyright (c) 2024 Asha the Fox 🦊
#  All rights reserved.
#
#  This is the part of the script that define and handle all the automated tasks the bot must do
#
#  Functions:
#      ASCII(image_url: str, width: int, height: int) - Converts an image from a URL to an ASCII art representation (allows us to display bot profile picture in CLIs).
#      format_uptime(uptime) - Formats a timedelta object into a human-readable string representing uptime (for status loop).
#      task.loop(seconds=60) : status() - Updates the bot's status and logs the current uptime every 60 seconds.
#      bot.event : on_ready() - Event handler for when the bot is ready, displays relevant bot information.
#
# -----------------------------------------------------------------------------




def ASCII(image_url: str, width: int = 20, height: int = 10) -> str:
    """
    Converts an image from a URL to an ASCII art representation.

    Args:
    - image_url (str): URL of the image to be converted.
    - width (int): Width of the resulting ASCII art.
    - height (int): Height of the resulting ASCII art.

    Returns:
    - str: ASCII art representation of the image, or an error message if conversion fails.
    """
    ASCII_CHARS = "@B%8WM#*oahkbdpwmZO0QCJYXzcvnxrjft/\\|()1[]-_+~<>i!lI;:,\"^`'. "

    try:
        # Download the image from the URL
        Response = requests.get(image_url)
        Response.raise_for_status()  # Raise an error for bad HTTP responses

        # Open the image and resize it while maintaining aspect ratio
        Img = Image.open(BytesIO(Response.content))
        Img = Img.resize((width, height))

        # Convert the image to grayscale
        Img = Img.convert("L")

        # Invert the colors to fit ASCII art conventions (dark = ASCII char, light = space)
        Img = Image.eval(Img, lambda x: 255 - x)

        # Create the ASCII art
        Ascii_img = ""
        for i in range(height):
            for j in range(width):
                Pixel_value = Img.getpixel((j, i))
                Ascii_char = ASCII_CHARS[Pixel_value * (len(ASCII_CHARS) - 1) // 255]
                Ascii_img += Ascii_char
            Ascii_img += "\n"

        return Ascii_img

    except Exception as e:
        # Log the error and return a user-fwiendly message 0v0
        logging.error(f"An error occurred while converting the image to ASCII: {e}")
        return "An ewwor occuwed, no image, sowwy >-<. Pwease twy again l8tr."

        
 

def format_uptime(uptime) -> str:
    """
    Formats a timedelta object into a human-readable string representing uptime.

    Args:
    - uptime (datetime.timedelta): The timedelta object representing the uptime.

    Returns:
    - uptime_str (str): A string representing the uptime in days, hours, minutes, and seconds.
    """
    Days = uptime.days
    Seconds = uptime.seconds
    Hours, Remainder = divmod(Seconds, 3600)
    Minutes, Seconds = divmod(Remainder, 60)

    # Initialize an empty list to collect time units
    Time_units = []

    # Add days,hours,minutes and seconds to the list if greater than zero
    if Days > 0:
        Time_units.append(f"{Days} day{'s' if Days > 1 else ''}")
    if Hours > 0:
        Time_units.append(f"{Hours} hour{'s' if Hours > 1 else ''}")
    if Minutes > 0:
        Time_units.append(f"{Minutes} minute{'s' if Minutes > 1 else ''}")
    if Seconds > 0:
        Time_units.append(f"{Seconds} second{'s' if Seconds > 1 else ''}")

    # Join the time units with commas, and ensure proper formatting
    Uptime_str = ', '.join(Time_units)

    return Uptime_str



@tasks.loop(seconds=60)
async def status() -> None:
    """
    Updates the bot's status and logs the uptime every 60 seconds.
    It allows us the have a rough idea of how long the bot has ran, especially if no errors are risen.

    Args:
    - None

    Returns:
    - None
    """
    # Calculate the uptime and server count, to update status of both the bot, and the console.
    Uptime = datetime.datetime.now() - Startup_time
    Server_count = len(bot.guilds)
    
    # Set the status message based on the number of servers WHY ISN'T THERE A CASE IN PYTHON GODAMNIT
    if Server_count == 1:
        Status_message = f'{Server_count} server'
    else:
        Status_message = f'{Server_count} servers'
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=Status_message))
    
    # Log the uptime and update the console title
    Uptime_str = format_uptime(Uptime)
    logging.info(f"The bot has been running for {Uptime_str}.")
    set_title(f"Bot : {Selected_bot} , Uptime : {Uptime_str}.")


def _set_avatar_async(url: str) -> None:
    """Fetch avatar, convert to ASCII, then push to dashboard state."""
    art = ASCII(url)
    if Dashboard_state and art:
        Dashboard_state.set_avatar(art)


@bot.event
async def on_ready() -> None:
    """
    Event handler for when the bot is ready.
    Clears the command line interface, prints bot information,
    and lists the bot's permissions in each server (guild) it is part of on the CLI.

    Args:
    - None

    Returns:
    - None
    """
    Bot_info = f"Connected as {bot.user.name} (ID: {bot.user.id})"
    logging.info(Bot_info)

    global Dashboard_started
    if not Dashboard_started:
        Dashboard_state.set_servers([Guild.name for Guild in bot.guilds])
        Dashboard_state.set_update_notice(UPDATE_NOTICE)
        Dashboard_state.set_bot_info(str(__version__), Config_file, bot_name=bot.user.name)
        # Build ASCII avatar in background to avoid blocking the event loop
        avatar_url = str(bot.user.display_avatar.url)
        _executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        _executor.submit(_set_avatar_async, avatar_url)
        Dashboard_started = True

    # Start the status update loop and synchronize the bot's tree (Slash commands)
    status.start()
    await bot.tree.sync()


@bot.event
async def on_guild_join(guild: discord.Guild) -> None:
    if Dashboard_state:
        Dashboard_state.set_servers([g.name for g in bot.guilds])
        Dashboard_state.add_event(f"Joined guild: {guild.name}")


@bot.event
async def on_guild_remove(guild: discord.Guild) -> None:
    if Dashboard_state:
        Dashboard_state.set_servers([g.name for g in bot.guilds])
        Dashboard_state.add_event(f"Left guild: {guild.name}")
        


"""
//////////////////////
///////Bot code///////
//////////////////////
"""

# -----------------------------------------------------------------------------
#  AT_bot.py , commands
#  Copyright (c) 2024 Asha the Fox 🦊
#  All rights reserved.
#
#  This is the part of the script that define and handle which and how the bots reacts to commands.
#
#  Functions:
#      gd_translator(text_to_translate: str, translate_language: str) - Translation handler to avoid code repetition (DRY principle)
#      bot.tree.command : trsend(interaction: discord.Interaction,text_received: str,translate_langage: str)  - Handles the translation and sending of a message using the bot.
#      @trsend.autocomplete : trsend_autocompletion( interaction: discord.Interaction, tmp_typing: str ) - Provides autocompletion suggestions for the 'translate_langage' parameter in the 'trsend' command.
#      bot.event : def on_raw_reaction_add(payload: discord.RawReactionActionEvent) - Event handler for when a reaction is added to a message, if reaction is a country flag, translates.
#
# -----------------------------------------------------------------------------

def detect_language(text: str) -> str:
    """
    Uses the DeepL API to detect the language of a given text.

    Args:
    - text (str): The text to detect the language of.

    Returns:
    - str: The detected language code, or an empty string if detection fails.
    """
    try:
        result = Deepl_translator.translate_text(text, target_lang="EN-GB")
        detected_language = result.detected_source_lang
        if Dashboard_state:
            Dashboard_state.record_api_call("deepl", ok=True)
        return detected_language
    except Exception as e:
        logging.error(f"An error occurred while detecting the language: {e}")
        if Dashboard_state:
            Dashboard_state.record_api_call("deepl", ok=False)
        return False
    
    


def gd_translator(text_to_translate: str, translate_language: str) -> tuple[str, str]:
    """
    Translation handler to avoid code repetition (DRY principle). This function detects which translation service 
    (Google Translate or DeepL) to use, preferring DeepL when available, and should be able to handle most errors.

    Args:
    - text_to_translate (str): The text to translate.
    - translate_language (str): The target language for translation.

    Returns:
    - Translated_text (str): The translated text.
    - Translator_name (str): The acronym of the translator used ('gt' for Google Translate, 'dpl' for DeepL), is also used to show errors to user if needed.
    """
    
    Translated_text: str = ""
    Translator_name: str = ""

    logging.info(f"gd_translator received a request to translate into '{translate_language}'.")

    # First, try to use DeepL if the target language is supported (deepl usually offer better accuracy)
    if translate_language in deepl_name_to_acronym and detect_language(text_to_translate):
        logging.info("Language appears to be supported by DeepL. Attempting translation with DeepL.")

        try:
            Translated_text = Deepl_translator.translate_text(
                text_to_translate, 
                target_lang=deepl_name_to_acronym[translate_language]
            )
            if Dashboard_state:
                Dashboard_state.record_api_call("deepl", ok=True)
            Translator_name = "dpl"
            logging.info("Translation with DeepL successful.")

        except Exception as e:
            logging.error(f"Unexpected error during DeepL translation: {e}")
            if Dashboard_state:
                Dashboard_state.record_api_call("deepl", ok=False)

            # Fallback to Google Translate (GT)
            logging.info("Switching to Google Translate due to DeepL error.")
            try:
                Translated_text = Google_translator.translate(
                    text_to_translate, 
                    dest=google_name_to_acronym[translate_language]
                ).text
                if Dashboard_state:
                    Dashboard_state.record_api_call("google", ok=True)
                Translator_name = "gt"
                logging.info("Translation with Google Translate successful after DeepL failure.")

            except Exception as e:
                logging.critical(f"Error using Google Translate after DeepL failure: {e}")
                logging.critical(f"Failed to translate message '{text_to_translate}' to '{translate_language}'.")
                if Dashboard_state:
                    Dashboard_state.record_api_call("google", ok=False)
                Translated_text = "An error occurred. The bot could not complete the translation. Please contact support."
                Translator_name = "ERROR"

    # If DeepL doesn't support the language, check if Google Translate does
    elif translate_language in google_name_to_acronym:
        logging.info("Language appears to be supported by Google Translate.")

        try:
            Translated_text = Google_translator.translate(
                text_to_translate, 
                dest=google_name_to_acronym[translate_language]
            ).text
            if Dashboard_state:
                Dashboard_state.record_api_call("google", ok=True)
            Translator_name = "gt"
            logging.info("Translation with Google Translate successful.")

        except Exception as e:
            logging.critical(f"Error using Google Translate: {e}")
            logging.critical(f"Failed to translate message '{text_to_translate}' to '{translate_language}'.")
            if Dashboard_state:
                Dashboard_state.record_api_call("google", ok=False)
            Translated_text = "An error occurred; the bot could not complete the translation. Please contact bot owner or support."
            Translator_name = "ERROR"

    # If neither translation service supports the language, log the issue and informs the user
    else:
        logging.error(f"Unsupported language '{translate_language}' for both DeepL and Google Translate.")
        Translated_text = f"Error: '{translate_language}' is not supported by the current translation services used by this bot."
        Translator_name = "ERROR"

    if Dashboard_state:
        Dashboard_state.record_translation(Translator_name, Translator_name != "ERROR")

    return Translated_text, Translator_name

        

@bot.tree.command(name='version', description='Show the bot version and repository link')
async def version(interaction: discord.Interaction) -> None:
    """
    Sends the bot version info only to the requesting user.

    Args:
    - interaction (discord.Interaction): The interaction object from the command.

    Returns:
    - None
    """
    if interaction.user.bot:
        return

    repo_url = "https://github.com/Natpol50/AT-bot"
    releases_url = f"{repo_url}/releases"
    message = (
        f"AT-bot version v{__version__} ({__last_revision__})\n"
        f"GitHub: {repo_url}\n"
        f"Releases: {releases_url}"
    )
    await interaction.response.send_message(message, ephemeral=True)



@bot.tree.command(name='trsend', description='Send a translated message with the bot')
@discord.app_commands.describe(text_received="The message you want to send using the bot.",translate_langage="The language you want your message to be in.")
@discord.app_commands.rename(text_received="message",translate_langage="langage")
async def trsend(interaction: discord.Interaction,text_received: str,translate_langage: str) -> None:
    """
    Handles the translation and sending of a message using the bot.

    1. Logs the translation request.
    2. Sends a temporary confirmation message to the user.
    3. Translates the input message.
    4. Sends the translated message via a webhook.
    5. Deletes the specific webhook after sending the message.

    Args:
    - interaction (discord.Interaction): The interaction object from the command.
    - text_received (str): The message to translate and send.
    - translate_langage (str): The target language for the translation.

    Returns :
    - None
    """
    logging.info(f"Translate request from {interaction.user.display_name} ({interaction.user.name}) using trsend with \"{translate_langage}\" language.")

    if interaction.user.bot:
        return
    elif not interaction.guild_id :
        await interaction.user.send("This command isn't meant to be used in DMs !")
    await interaction.response.send_message('Message received, processing...', ephemeral=True)
    Translated_text, Translator_name = gd_translator(text_to_translate = text_received, translate_language = translate_langage)
    if Dashboard_state:
        Dashboard_state.add_event(f"trsend {translate_langage} ({Translator_name}) by {interaction.user.display_name}")

    # Create a webhook with a name that includes the translator name, we grab the webhook id to allow it to delete just this one.
    Webhook = await interaction.channel.create_webhook(name=interaction.user.display_name+ " " + Translator_name)
    Webhook_id = Webhook.id

    try:
        # Send the translated text using the created webhook
        await Webhook.send(content=str(Translated_text),username=interaction.user.display_name,avatar_url=interaction.user.avatar)
    except Exception as e:
        logging.error(f"There was an error sending the fake user message in trsend function error is : {e}")

        # Delete the specific webhook after sending the message
    Webhooks = await interaction.channel.webhooks()
    for wh in Webhooks:
        if wh.id == Webhook_id:
            await wh.delete()
            break  # Exit the loop once the specific webhook is deleted

@bot.tree.command(name='AThelp', description='Show available commands and usage tips')
async def help_command(interaction: discord.Interaction) -> None:
    """
    Sends a short help message only to the requesting user.

    Args:
    - interaction (discord.Interaction): The interaction object from the command.

    Returns:
    - None
    """
    if interaction.user.bot:
        return

    message = (
        "AT-bot help (slash commands)\n"
        "- /trsend: Send a translated message as you.\n"
        "  Required: message, langage (target language).\n"
        "- /version: Show the bot version and GitHub links.\n"
        "\n"
        "Tip: You can also react with a flag emoji on a message to get a translation in DMs."
    )
    await interaction.response.send_message(message, ephemeral=True)

@trsend.autocomplete("translate_langage")
async def trsend_autocompletion( interaction: discord.Interaction, tmp_typing: str ) -> typing.List[discord.app_commands.Choice[str]]:
    """
    Provides autocompletion suggestions for the 'translate_langage' parameter in the 'trsend' command.

    Args:
    - interaction (discord.Interaction): The interaction object that triggered the autocomplete.
    - tmp_typing (str): The current text input from the user for which to provide suggestions.

    Returns:
    - typing.List[discord.app_commands.Choice[str]]: A list of autocomplete choices that match the user's input.
    """
    # Initialize the list to hold autocomplete choices and limit choices to 25 'prediction'
    Return_list = []
    Max_choices = 25

    # Filter the available language choices based on user input
    Filtered_autofill = [
        Langage_choice for Langage_choice in language_autofill_choices
        if tmp_typing.lower() in Langage_choice.lower()
    ]
 
    for Langage_choice in Filtered_autofill[:Max_choices]:
        Return_list.append(
            discord.app_commands.Choice(name=Langage_choice, value=Langage_choice)
        )

    return Return_list


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    """
    Event handler for when a reaction is added to a message.
    
    Args:
    - payload (discord.RawReactionActionEvent): The payload containing information about the reaction.
    """
    # Ignore reactions added by bots and phantom reactions
    if payload.member.bot:
        return
    elif not payload.guild_id :
        return
    Channel = bot.get_channel(payload.channel_id)
    Message = await Channel.fetch_message(payload.message_id)
    Flag = payload.emoji.name
    try :
        if Flag in deepl_flag_to_acronym :
            logging.info(f"\"{payload.member}\" used the flag_{Flag} reaction on a message by {Message.author}")
            logging.info("Deepl seems to be able to handle that language.")
            User = await bot.fetch_user(payload.user_id)
            if deepl_flag_to_acronym[Flag] == 'X':
                logging.info("It was Belgium or Switzerland, abort mission")
                await User.send(f'Translation refused, the country selected does not have a langage defined. (at the time this version of the code was written, the country is either Belgium or Switzerland)')
                await Message.remove_reaction(payload.emoji, User)
            else:
                if len(Message.content) <= 0 :
                    logging.info(f"Nevermind, message was empty")
                    await User.send("Error, no text found.")
                    await Message.remove_reaction(payload.emoji, User)
                else :
                    Translated_message, Translator = gd_translator(Message.content , deepl_acronym_to_name[deepl_flag_to_acronym[Flag]])
                    if Dashboard_state:
                        Dashboard_state.add_event(f"flag {Flag} -> {deepl_acronym_to_name[deepl_flag_to_acronym[Flag]]} ({Translator})")
        elif Flag in google_flag_to_acronym :
            logging.info(f"\"{payload.member}\" used the flag_{Flag} reaction on a message by {Message.author}")
            logging.info("Deepl seems to be able to handle that language.")
            User = await bot.fetch_user(payload.user_id)
            if len(Message.content) <= 0 :
                logging.info(f"Nevermind, message was empty")
                await User.send("Error, no text found.")
                await Message.remove_reaction(payload.emoji, User)
            else :
                Translated_message, Translator = gd_translator(Message.content , google_acronym_to_name[google_flag_to_acronym[Flag]])
                if Dashboard_state:
                    Dashboard_state.add_event(f"flag {Flag} -> {google_acronym_to_name[google_flag_to_acronym[Flag]]} ({Translator})")
    except Exception as e:
        logging.error(f"The bot wasn't able to handle a reaction translation. Error : {e}")
    
    try:
        await User.send(Message.content)
        await User.send(f"-> {Flag} ({Translator})")
        await User.send(Translated_message)
        await Message.remove_reaction(payload.emoji, User)
        del User
    except Exception as e:
        logging.error(f"The bot wasn't able to send the messages to the user {User.display_name}")
        del User









# We then, after we loaded everything, runs the bot.
def _run_bot() -> None:
    bot.run(Discord_api_key)


bot_thread = threading.Thread(target=_run_bot, daemon=True)
bot_thread.start()

Dashboard.start_dashboard(Dashboard_state)
