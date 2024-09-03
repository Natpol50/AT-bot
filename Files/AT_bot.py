import os
import subprocess
import logging




"""
//////////////////
///////BOOT///////
//////////////////
"""

def bootup_function():
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
    def log_init():
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

        log_folder = f'{pathlib.Path(__file__).parent.absolute()}/logs'

        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        log_file = os.path.join(
            log_folder,
            f"{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}.log"
        )

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        logging.info("Script started.")
    
    flag_file = "Firasatar&a&.flag"  # Flag to indicate first-time setup

    if not os.path.exists(flag_file):
        import Dependency_installer as install

        dependencies = [
            'discord.py',
            'googletrans==4.0.0-rc.1',
            'typing',
            'requests',
            'configparser',
            'windows-curses',
            'Pillow',
            'deepl'
        ]

        total_size = 0
        dependencies_to_install = []

        print("As this is the first time the script is running, dependencies will be installed.")

        # Attempt to install pathlib separately
        try:
            subprocess.check_call(['pip', 'install', 'pathlib'])
        except subprocess.CalledProcessError as e:
            print(f"There was an error installing pathlib: {e}.")
            input("\nPress enter to open the bug report page [https://github.com/Natpol50/AT-bot/issues]")
            subprocess.run(['powershell', '-Command', f"start-Process {'https://github.com/Natpol50/AT-bot/issues'}"])
            input('Press enter to exit...')
            exit()

        log_init()
        logging.info("First-time setup, installing dependencies")

        # Determine the size of each dependency and prepare the installation list
        for dep in dependencies:
            dep_size = install.get_package_size(dep)
            if dep_size > 0:
                dependencies_to_install.append(dep)
            elif dep_size == -1:
                print(f"Error retrieving size for package {dep}")
            total_size += dep_size

        # Install thoses dependencies (OR NOT)
        if dependencies_to_install:
            option = input(
                f"You need to install these dependencies: {dependencies_to_install}.\n"
                f"The total size is approximately {total_size:.2f} MB.\n"
                "Do you wish to proceed (Y/N)? "
            )
            if option.lower() not in ["y", "yes"]:
                exit()

            install.install_packages(dependencies_to_install)
            

        # Create the flag file to indicate setup has been completed
        with open(flag_file, "w") as file:
            file.write(
                "A simple flag indicating that the script has run before.\n"
                "Asha thanks you for reading this, but seriously, don't you have anything else to do?"
            )
        del install
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


def Bot_picker(input_list):
    """
    Displays a CLI menu to choose an item from the input_list using the curses library.

    Args:
    - input_list(list): A list of strings to be displayed as selectable options.

    Returns:
    - str: The selected item from the input_list.
    """

    # Initialize the curses environment
    stdscr = curses.initscr()
    curses.cbreak()  # Disable line buffering
    stdscr.keypad(True)  # Enable special keys (e.g., arrow keys)
    curses.noecho()  # Do not display typed characters

    selected_index = 0  # Track the currently selected index

    try:
        while True:
            stdscr.clear()  # Clear the screen
            
            # Display instruction text
            stdscr.addstr("\nChoose a bot, or choose 'New bot' to create a new bot/profile.\n\n")

            # Display the list with one element highlighted
            for index, element in enumerate(input_list):
                if index == selected_index:
                    stdscr.addstr(f"{index + 1}. {element}\n", curses.A_REVERSE)  # Highlight selected item
                else:
                    stdscr.addstr(f"   {element}\n")

            stdscr.refresh()  # Refresh the screen to reflect changes

            key = stdscr.getch()  # Get user input

            # Navigate through the list
            if key == curses.KEY_DOWN:
                selected_index = min(selected_index + 1, len(input_list) - 1)
            elif key == curses.KEY_UP:
                selected_index = max(selected_index - 1, 0)
            elif key == 10:  # Enter key
                break  # Exit the loop to return the selected item

    finally:
        # Cleans up the curses environment
        curses.endwin()

    return input_list[selected_index]

def config_init():
    """
    Sets up the configuration file for ATbot, 
    it allows the user to select multiple profiles.
    
    Args:
    - None

    Returns:
    - None
    """
    # There, we initialise the configuration file, we must not forget to make it accessible from everything.
    global config, config_file
    config = configparser.ConfigParser()
    config_file = f'{pathlib.Path(__file__).parent.absolute()}/config.ini'

    if not os.path.exists(config_file):
        with open(config_file, 'w') as file:
            file.write(" ")  # Create an empty config file

def setup_environment():
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
    global selected_bot


    # First, we welcome the user.
    Displays.Welcome()
    os.system('cls')  # Clear the screen
    
    # And then, ask the user which bot he wanna use.
    os.system("title ATbot - Config Picker")
    config.read(config_file)
    bot_list = config.sections()
    bot_list.append('New bot')  # Adds a 'New bot' option, for multiple profiles.
    selected_bot = Bot_picker(bot_list)
    print(" ")

    os.system('cls')

    if selected_bot == 'New bot':
        # Handle new bot creation
        os.system("title ATbot - New Bot")
        selected_bot = input("Choose a name for the new bot: ")

        # First, we get and verify the discord bot API key.
        Displays.DS_api()
        discord_key_valid = False
        while not discord_key_valid:
            discord_api_key = input("\nDiscord bot API key (token): ")
            print("Starting Discord token verification...")
            logging.info("Starting Discord token verification.")
            discord_key_valid = Tokenverif.DS_token(discord_api_key)
            if not discord_key_valid :
                print('Please, provide a correct bot token')
        print("The token seems good, continuing...")
        logging.info("Token verification was successful, continuing...")

        # Then, we do the same thing with the Deepl one.
        Displays.DPL_api()
        deepl_key_valid = False
        while not deepl_key_valid:
            deepl_api_key = input("\nDeepl API key: ")
            print("Starting Deepl token verification...")
            logging.info("Starting Deepl token verification.")
            deepl_key_valid = Tokenverif.DPL_token(deepl_api_key)
        print("The token seems good, continuing...")
        logging.info("Token verification was successful, continuing...\n")

        # And finally write the bot informations onto the config file.
        config[f"{selected_bot}"]={
        "discord" : discord_api_key,
        "deepl" : deepl_api_key
        }                               
        with open(config_file,"w") as File_object:
            config.write(File_object)

def bot_bootup(selected_bot, config_file, config):
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
    global Discord_api_key, Deepl_translator, gt, bot, startup_time
    startup_time = datetime.datetime.now()

    # Set the console window title
    os.system(f"title Bot : {selected_bot} , Starting...")

    # Print and log the configuration file path
    print(f'\nConfig file is {config_file}\n')
    logging.info(f'\nConfig file is {config_file}\n')

    # Test connectivity to Discord.com
    try:
        response = requests.get("https://discord.com/", timeout=5)
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
    gt = Translator()

    # Set up the Discord bot
    print(f"Running on discord.py version {discord.__version__}")
    logging.info(f"Running on discord.py version {discord.__version__}")

    intents = discord.Intents.default()
    intents.message_content = True
    intents.reactions = True  # Set permissions for the bot

    bot = commands.Bot(command_prefix='ATbot.', intents=intents)
    bot.remove_command('help')  # Remove the default help command


"""
//////////////////////
///////Bot code///////
//////////////////////
"""

# First, we load everything to avoid any bot not defined error, then we load the bot code.
bootup_function()
del bootup_function


config_init()
setup_environment()
bot_bootup(selected_bot,config_file,config)
del Bot_picker
del config_init
del setup_environment

def ASCII(image_url, width, height):
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
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an error for bad HTTP responses

        # Open the image and resize it while maintaining aspect ratio
        img = Image.open(BytesIO(response.content))
        img = img.resize((width, height))

        # Convert the image to grayscale
        img = img.convert("L")

        # Invert the colors to fit ASCII art conventions (dark = ASCII char, light = space)
        img = Image.eval(img, lambda x: 255 - x)

        # Create the ASCII art
        ascii_img = ""
        for i in range(height):
            for j in range(width):
                pixel_value = img.getpixel((j, i))
                ascii_char = ASCII_CHARS[pixel_value * (len(ASCII_CHARS) - 1) // 255]
                ascii_img += ascii_char
            ascii_img += "\n"

        return ascii_img

    except Exception as e:
        # Log the error and return a user-fwiendly message 0v0
        logging.error(f"An error occurred while converting the image to ASCII: {e}")
        return "An ewwor occuwed, no image, sowwy >-<. Pwease twy again l8tr."

        
 

def format_uptime(uptime):
    """
    Formats a timedelta object into a human-readable string representing uptime.

    Args:
    - uptime (datetime.timedelta): The timedelta object representing the uptime.

    Returns:
    - uptime_str (str): A string representing the uptime in days, hours, minutes, and seconds.
    """
    days = uptime.days
    seconds = uptime.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Initialize an empty list to collect time units
    time_units = []

    # Add days,hours,minutes and seconds to the list if greater than zero
    if days > 0:
        time_units.append(f"{days} day{'s' if days > 1 else ''}")
    if hours > 0:
        time_units.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes > 0:
        time_units.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds > 0:
        time_units.append(f"{seconds} second{'s' if seconds > 1 else ''}")

    # Join the time units with commas, and ensure proper formatting
    uptime_str = ', '.join(time_units)

    return uptime_str



@tasks.loop(seconds=60)
async def status():
    """
    Updates the bot's status and logs the uptime every 60 seconds.
    It allows us the have a rough idea of how long the bot has ran, especially if no errors are risen.

    Args:
    - None

    Returns:
    - None
    """
    # Calculate the uptime and server count, to update status of both the bot, and the console.
    uptime = datetime.datetime.now() - startup_time
    server_count = len(bot.guilds)
    
    # Set the status message based on the number of servers
    if server_count == 1:
        status_message = f'{server_count} server'
    else:
        status_message = f'{server_count} servers'
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_message))
    
    # Log the uptime and update the console title
    uptime_str = format_uptime(uptime)
    logging.info(f"The bot has been running for {uptime_str}.")
    os.system(f"title Bot : {selected_bot} , Uptime : {uptime_str}.")

           


@bot.event
async def on_ready():
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
    bot_info = f"Connected as {bot.user.name} (ID: {bot.user.id})"
    print(f"\n{bot_info}\n")
    print(ASCII(bot.user.avatar, 20, 10))
    logging.info(bot_info)

    # List bot permissions in each guild
    for guild in bot.guilds:
        print(f"Permissions in guild: {guild.name}")
        logging.info(f"Permissions in guild: {guild.name}")

        try:
            for channel in guild.channels:
                try:
                    # Get and print permissions for the bot in each channel
                    permissions = channel.permissions_for(guild.me)
                    channel_info = f"    - {channel.name}: {permissions}"
                    print(channel_info)
                    logging.info(channel_info)
                except Exception as e:
                    error_message = f"Failed to retrieve permissions for channel '{channel.name}': {e}"
                    print(error_message)
                    logging.error(error_message)
        except Exception as error:
            guild_error_message = f"Error processing channels in guild '{guild.name}': {error}"
            print(guild_error_message)
            logging.error(guild_error_message)

        print(" ")

    # Start the status update loop and synchronize the bot's tree
    status.start()
    await bot.tree.sync()
        

class MyModal(discord.ui.Modal, title = "test modal"):
    text_to_translate = discord.ui.TextInput(label="Text to Translate", style = discord.TextStyle.long, placeholder= "Bonjour tout le monde ! ", required= True,)

    async def on_submit(self, interaction : discord.Interaction):
        embed = discord.Embed(title= "Translation command" ,description= "")
        
        embed.set_author( name= interaction.user.display_name, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed, ephemeral= True)

@bot.tree.context_menu(name='translation')
async def trad(interaction : discord.Interaction , user : discord.Member):
    await interaction.response.send_modal(MyModal())
    logging.info(f'{user} used translation app')














@bot.tree.command(name ='trsend', description = 'Send a translated message with the bot', )
@discord.app_commands.describe(text_to_send = "The message you wanna send using the bot.", translate_langage = "The langage you want your message to be in." )
@discord.app_commands.rename(text_to_send = "message", translate_langage = "langage")
async def trasend(interaction : discord.Interaction, text_to_send : str , translate_langage : str ):
    logging.info(f"Translate request from {interaction.user.display_name} ({interaction.user.name}) using trsend with \"{translate_langage}\" langage.")
    if translate_langage in langues_n_invert or translate_langage in langues_n_gt_invert  : 
        if translate_langage in langues_n_invert : 
            try :
                embed = discord.Embed(title= f"Translation to {translate_langage}" ,description= f"{Deepl_translator.translate_text(text_to_send, target_lang=langues_n_invert[translate_langage])}")
                embed.set_author( name= interaction.user.display_name, icon_url=interaction.user.avatar)
                await interaction.response.send_message(embed=embed)
            except Exception as e :
                logging.error(f"Error while using Deepl (Deepl module) : {e}")
                logging.info(f'Switching to googletrans module')
                await interaction.channel.send(f'(Due to an error, the translation switched to Google translate, it might be less accurate)')
                translation = gt.translate(text_to_send, dest=langues_n_gt_invert[translate_langage])
                embed = discord.Embed(title= f"Translation to {translate_langage}" ,description= f"{translation.text}")
                embed.set_author( name= interaction.user.display_name, icon_url=interaction.user.avatar)
                await interaction.response.send_message(embed=embed)
        elif translate_langage in langues_n_gt_invert :
            try :
                translation = gt.translate(text_to_send, dest=langues_n_gt_invert[translate_langage])
                await interaction.channel.send(f'(Deepl does not support that langage, the translation switched to Google translate, it might be less accurate)')
                embed = discord.Embed(title= f"Translation to {translate_langage}" ,description= f"{translation.text}")
                embed.set_author( name= interaction.user.display_name, icon_url=interaction.user.avatar)
                await interaction.response.send_message(embed=embed)
            except Exception as e :
                logging.critical(f"Error while using Google translate (googletrans module) : {e}")
    else :
        await interaction.response.send_message(f"Error, \"{translate_langage}\" is not a valid langage.", ephemeral=True)

@trasend.autocomplete("translate_langage")
async def trasend_autocompletion(interaction: discord.Interaction, tmp_typing: str) -> typing.List[discord.app_commands.Choice[str]]:
    return_list = []
    filtered_lang_ch_auto = [langage_choice for langage_choice in lang_ch_auto if tmp_typing.lower() in langage_choice.lower()]
    max_choices = 25
    for langage_choice in filtered_lang_ch_auto[:max_choices]:
        return_list.append(discord.app_commands.Choice(name=langage_choice, value=langage_choice))

    return return_list


@bot.tree.command(name='invitest', description='test 2 , invisible')
async def invitest(interaction : discord.Interaction ):
    await interaction.response.send_message('voici un test, invisible', ephemeral=True)

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
            await message.reply(f'Translation refused, the country selected does not have a langage defined. (at the time, the country is either Belgium or Switzerland)')
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
