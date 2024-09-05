import os
import subprocess
import logging




"""
//////////////////
///////BOOT///////
//////////////////
"""

def bootup_function() -> None:
    """
    Verifies if everything seems right and initialize logging.
    
    This function will : 
     - Verify if the script has been used before (if not, installs the required libraries)
     - Initialize the logging

    It's also meant to verify if there's an update to the bot (coming soon)
    
    Args:
    - None
    
    Returns:
    - None
    """
    def log_init() -> None:
        """
        Initialize logging for the script.
        Used after the first time setup flag has been checked

        Args:
        - None
    
        Returns:
        - None
        """
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
    
    Flag_file = "Firasatar&a&.flag"  # Flag to indicate first-time setup

    if not os.path.exists(Flag_file):
        import Dependency_installer as install

        Dependencies = [
            'discord.py',
            'googletrans==4.0.0-rc.1',
            'typing',
            'requests',
            'configparser',
            'windows-curses',
            'Pillow',
            'deepl'
        ]

        Total_size = 0
        Dependencies_to_install = []

        print("As this is the first time the script is running, Dependencies will be installed.")

        # Attempt to install pathlib separately, as pathlib is needed for the logging to work. (refer to log_init() function)
        try:
            subprocess.check_call(['pip', 'install', 'pathlib'])
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
            option = input(
                f"You need to install these dependencies: {Dependencies_to_install}.\n"
                f"The total size is approximately {Total_size:.2f} MB.\n"
                "Do you wish to proceed (Y/N)? "
            )
            if option.lower() not in ["y", "yes"]:
                exit()

            install.install_packages(Dependencies_to_install)
            
        del install
        # Create the flag file to indicate setup has been completed
        with open(Flag_file, "w") as File:
            File.write(
                "A simple flag indicating that the script has run before.\n"
                "Asha thanks you for reading this, but seriously, don't you have anything else to do?"
            )
        
    else:
        log_init()
        logging.info("Script has already run before, skipping dependency installation.")





"""
///////////////////////////////////////////////////
/////// Configuration,bootup and setting up ///////
///////////////////////////////////////////////////
"""


import discord
from discord.ext import commands , tasks
import deepl
from discord.interactions import Interaction
from googletrans import Translator
import typing
from listlist import *
import requests
import configparser
import curses
import Tokenverif
from io import BytesIO
from PIL import Image
import asyncio
import pathlib
import datetime
import Displays


def bot_picker(input_list) -> str:
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
    os.system('cls')  # Clear the screen
    
    # And then, ask the user which configuration he wanna use.
    os.system("title ATbot - Config Picker")
    Config.read(Config_file)
    Bot_list = Config.sections()
    Bot_list.append('New bot/config')  # Adds a 'New bot/config' option, for multiple profiles.
    Selected_bot = bot_picker(Bot_list)
    print(" ")

    os.system('cls')

    if Selected_bot == 'New bot':
        # Handle new bot creation
        os.system("title ATbot - New Bot/config")
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
    os.system(f"title Bot : {selected_bot} , Starting...")

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


"""
//////////////////////
///////Bot boot///////
//////////////////////
"""

# First, we load everything to avoid any bot not defined error, then we load the bot code.
bootup_function()
del bootup_function


config_init()
setup_environment()
bot_bootup(Selected_bot,Config_file,Config)
del bot_picker
del config_init
del setup_environment

def ASCII(image_url, width, height) -> str:
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
    os.system(f"title Bot : {Selected_bot} , Uptime : {Uptime_str}.")

           


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
    # Clear the command line interface
    os.system('cls')

    # Print bot connection details
    Bot_info = f"Connected as {bot.user.name} (ID: {bot.user.id})"
    print(f"\n{Bot_info}\n")
    print(ASCII(bot.user.avatar, 25, 10))
    logging.info(Bot_info)

    # List bot permissions in each guild
    for Guild in bot.guilds:
        print(f"Permissions in guild: {Guild.name}")
        logging.info(f"Permissions in guild: {Guild.name}")

        try:
            for Channel in Guild.channels:
                try:
                    # Get and print permissions for the bot in each channel
                    permissions = Channel.permissions_for(Guild.me)
                    Channel_info = f"    - {Channel.name} [Permission integer : {permissions.value}]"
                    print(Channel_info)
                    logging.info(Channel_info)
                except Exception as e:
                    Error_message = f"Failed to retrieve permissions for channel '{Channel.name}': {e}"
                    print(Error_message)
                    logging.error(Error_message)
        except Exception as error:
            Guild_error_message = f"Error processing channels in guild '{Guild.name}': {error}"
            print(Guild_error_message)
            logging.error(Guild_error_message)

        print(" ")

    # Start the status update loop and synchronize the bot's tree (Slash commands)
    status.start()
    await bot.tree.sync()
        


"""
//////////////////////
///////Bot code///////
//////////////////////
"""


def gd_translator(text_to_translate: str, translate_language: str) -> tuple[str, str]:
    """
    Translation handler to avoid code repetition (DRY principle). This function detects which translation service 
    (Google Translate or DeepL) to use, preferring DeepL when available, and should be hable to handle most errors.

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
    if translate_language in Deepl_language_dict_inverted:
        logging.info("Language appears to be supported by DeepL. Attempting translation with DeepL.")

        try:
            Translated_text = Deepl_translator.translate_text(
                text_to_translate, 
                target_lang=Deepl_language_dict_inverted[translate_language]
            )
            Translator_name = "dpl"
            logging.info("Translation with DeepL successful.")

        except Exception as e:
            # Handle specific error codes from DeepL (Making logs easier to read)
            if e.code == 456:
                logging.error("DeepL translation quota exceeded for this billing period.")
                print("DeepL translation quota exceeded for this billing period.")
            elif e.code == 413:
                logging.error("The message is too large to be processed by DeepL.")
                print("Message is too large to be processed.")
            else:
                logging.error(f"Unexpected error during DeepL translation: {e}")

            # Fallback to Google Translate (GT), do not check if language is supported by GT, as it is the case for all languages as in the 05/09/2024 (european date)
            logging.info("Switching to Google Translate due to DeepL error.")
            try:
                Translated_text = Google_translator.translate(
                    text_to_translate, 
                    dest=Google_language_dict_inverted[translate_language]
                ).text
                Translator_name = "gt"
                logging.info("Translation with Google Translate successful after DeepL failure.")

            except Exception as e:
                logging.critical(f"Error using Google Translate after DeepL failure: {e}")
                logging.critical(f"Failed to translate message '{text_to_translate}' to '{translate_language}'.")
                Translated_text = "An error occurred; the bot could not complete the translation. Please contact support."
                Translator_name = "ERROR"

    # If DeepL doesn't support the language, check if Google Translate does
    elif translate_language in Google_language_dict_inverted:
        logging.info("Language appears to be supported by Google Translate.")

        try:
            Translated_text = Google_translator.translate(
                text_to_translate, 
                dest=Google_language_dict_inverted[translate_language]
            ).text
            Translator_name = "gt"
            logging.info("Translation with Google Translate successful.")

        except Exception as e:
            logging.critical(f"Error using Google Translate: {e}")
            logging.critical(f"Failed to translate message '{text_to_translate}' to '{translate_language}'.")
            Translated_text = "An error occurred; the bot could not complete the translation. Please contact bot owner or support."
            Translator_name = "ERROR"

    # If neither translation service supports the language, log the issue and informs the user
    else:
        logging.error(f"Unsupported language '{translate_language}' for both DeepL and Google Translate.")
        Translated_text = f"Error: '{translate_language}' is not supported by the current translation services used by this bot."
        Translator_name = "ERROR"

    return Translated_text, Translator_name

        

@bot.tree.command(name='trsend', description='Send a translated message with the bot')
@discord.app_commands.describe(text_received="The message you want to send using the bot.",translate_langage="The language you want your message to be in.")
@discord.app_commands.rename(text_received="message",translate_langage="langage")
async def trasend(interaction: discord.Interaction,text_received: str,translate_langage: str) -> None:
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
    await interaction.response.send_message('Message received, processing...', ephemeral=True)
    Translated_text, Translator_name = gd_translator(text_to_translate = text_received, translate_language = translate_langage)

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

@trasend.autocomplete("translate_langage")
async def trasend_autocompletion(
    interaction: discord.Interaction,  # Taking the interaction just in case
    tmp_typing: str
) -> typing.List[discord.app_commands.Choice[str]]:
    """
    Provides autocomplete suggestions for the 'translate_langage' parameter in the 'trasend' command.

    Args:
    - interaction (discord.Interaction): The interaction object that triggered the autocomplete.
    - tmp_typing (str): The current text input from the user for which to provide suggestions.

    Returns:
    - typing.List[discord.app_commands.Choice[str]]: A list of autocomplete choices that match the user's input.
    """
    # Initialize the list to hold autocomplete choices
    Return_list = []

    # Filter the available language choices based on user input
    filtered_lang_ch_auto = [
        langage_choice for langage_choice in lang_ch_auto
        if tmp_typing.lower() in langage_choice.lower()
    ]

    # Limit the number of choices to a maximum of 25
    max_choices = 25
    for langage_choice in filtered_lang_ch_auto[:max_choices]:
        Return_list.append(
            discord.app_commands.Choice(name=langage_choice, value=langage_choice)
        )

    return Return_list


@bot.event
async def on_raw_reaction_add(Reaction):
    if Reaction.user_id == bot.user.id:
        return
    channel = bot.get_channel(Reaction.channel_id)
    message = await channel.fetch_message(Reaction.message_id)
    
    flag = Reaction.emoji.name
    if flag in langues:
        user = await bot.fetch_user(Reaction.user_id)
        if langues[flag] == 'X' :
            await message.reply(f'Translation refused, the country selected does not have a langage defined. (at the time this version of the code was written, the country is either Belgium or Switzerland)')
            await message.remove_reaction(Reaction.emoji, user)
        else :
            logging.info(f"({message.guild.name}) Message in {message.channel.name}: \"{message.content}\" Reaction added by {Reaction.member} (message by {message.author.name} ({message.author.global_name})) for Deepl \"{langues[flag]}\" Translation .")
            logging.info(f"\"{Reaction.member}\" used the flag_{flag} reaction")
            if len(message.content) <= 0 :
                logging.info(f"No message, error handled correctly")
                await message.reply("Error, no text found.", mention_author= False)
                await message.remove_reaction(Reaction.emoji, user)
            else:
                try :
                    embed = discord.Embed(title= f"Deepl Translation to {lang_n[langues[flag]]}" ,description= f"{Deepl_translator.translate_text(message.content, target_lang=langues[flag])}")
                    embed.set_author( name= user, icon_url= user.avatar)
                    await message.reply(embed=embed, mention_author= False)
                    await message.remove_reaction(Reaction.emoji, user)
                except Exception as e : 
                    try :
                        logging.error(f'Error while using Deepl (Deepl module) : {e}')
                        logging.info(f'Switching to googletrans module')
                        translation = gt.translate(message.content, dest=langues_gt[flag])
                        embed = discord.Embed(title= f"Google Translation to {lang_n_gt[langues_gt[flag]]}" ,description= f"{translation.text}\n\n *:warning: Due to an error, the translation switched to Google translate, it might be less accurate*")
                        embed.set_author( name= user, icon_url= user.avatar)
                        await message.reply(embed=embed, mention_author= False)
                        await message.remove_reaction(Reaction.emoji, user)
                    except Exception as e : 
                        logging.critical(f'Error while using Google Translate (googletrans module) : {e}')
                        embed = discord.Embed(title= f"Sorry, {user}" ,description= f"For an unknown reason, the bot wasn't able to translate that message to {lang_n[langues[flag]]}, \n is this continues, please contact the owner of the bot or natpol50.")
                        embed.set_author( name= "ERROR", icon_url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrJ_BIHPu0Q0ZeOwRso3svFNrvYEN_uw7GyA&usqp=CAU")
                        await message.reply(embed=embed, mention_author= False)
                        await message.remove_reaction(Reaction.emoji, user)
    elif flag in langues_gt:
        user = await bot.fetch_user(Reaction.user_id)
        logging.info(f"({message.guild.name}) Message in {message.channel.name}: \"{message.content}\" Reaction added by {Reaction.member} (message by {message.author.name} ({message.author.global_name})) for google traduction \"{langues_gt[flag]}\" Translation.")
        logging.info(f"\"{Reaction.member}\" used the flag_{flag} reaction")
        
        if len(message.content) <= 0 :
            logging.info(f"No message, error handled correctly")
            await message.reply("Error, no text found.", mention_author= False)
            await message.remove_reaction(Reaction.emoji, user)
        else:
            try :
                translation = gt.translate(message.content, dest=langues_gt[flag])
                embed = discord.Embed(title= f"Google Translation to {lang_n_gt[langues_gt[flag]]}" ,description= f"{translation.text}")
                embed.set_author( name= user, icon_url= user.avatar)
                await message.reply(embed=embed, mention_author= False)
                await message.remove_reaction(Reaction.emoji, user)
            except Exception as e : 
                logging.critical(f'Error while using google translate (googletrans module) : {e}')
                embed = discord.Embed(title= f"Sorry, {user}" ,description= f"For an unknown reason, the bot wasn't able to translate that message to {lang_n_gt[langues_gt[flag]]}, \n is this continues, please contact the owner of the bot or natpol50.")
                embed.set_author( name= "ERROR", icon_url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrJ_BIHPu0Q0ZeOwRso3svFNrvYEN_uw7GyA&usqp=CAU")
                await message.reply(embed=embed, mention_author= False)
                await message.remove_reaction(Reaction.emoji, user)



bot.run(Discord_api_key)

input()
