import os
import subprocess
import logging

def bootup_function():
    def log_init():
        """Initialize logging for the script."""
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
        import install

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

            install.libraries(dependencies_to_install)
            

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


bootup_function()
del bootup_function

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
import Tokensverif
from io import BytesIO
from PIL import Image
import asyncio
import pathlib
import datetime
import Displays


def Bot_picker(input_list):
    """
    Displays a CLI menu to choose an item from the input_list using the curses library.

    Parameters:
    - input_list: A list of strings to be displayed as selectable options.

    Returns:
    - The selected item from the input_list.
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
        # Clean up the curses environment
        curses.endwin()

    return input_list[selected_index]

def config_init():
    """
    Sets up the configuration file for ATbot, 
    it allows the user to select multiple profiles.
    """
    # We initialise the configuration file, we must not forget to make it accessible from everything.
    global config
    config = configparser.ConfigParser()
    global config_file
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
    """
    
    # First, we welcome the user.
    Displays.welcome()
    os.system('cls')  # Clear the screen

    # And then, ask the user which bot he wanna use.
    os.system("title ATbot - Config Picker")
    config.read(config_file)
    bot_list = config.sections()
    bot_list.append('New bot')  # Adds a 'New bot' option, for multiple profiles.
    global selected_bot
    selected_bot = Bot_picker(bot_list)
    print(" ")

    os.system('cls')

    if selected_bot == 'New bot':
        # Handle new bot creation
        os.system("title ATbot - New Bot")
        selected_bot = input("Choose a name for the new bot: ")

        # First, we get and verify the discord bot API key.
        Displays.Dis_api()
        discord_key_valid = False
        while not discord_key_valid:
            discord_api_key = input("\nDiscord bot API key: ")
            print("Starting Discord token verification...")
            logging.info("Starting Discord token verification.")
            discord_key_valid = Tokensverif.DS_token(discord_api_key)
        logging.info("Token verification was successful, continuing...")

        # Then, we do the same thing with the Deepl one.
        Displays.deepl()
        deepl_key_valid = False
        while not deepl_key_valid:
            deepl_api_key = input("\nDeepl API key: ")
            print("Starting Deepl token verification...")
            logging.info("Starting Deepl token verification.")
            deepl_key_valid = Tokensverif.DPL_token(deepl_api_key)
        logging.info("Token verification was successful, continuing...\n")

        # And finally write the bot informations onto the config file.
        config[f"{selected_bot}"]={
        "discord" : discord_api_key,
        "deepl" : deepl_api_key
        }                               
        with open(config_file,"w") as File_object:
            config.write(File_object)

# Call the setup function
config_init()
setup_environment()

del Bot_picker
del config_init
del setup_environment
    


Cbot = selected_bot

os.system(f"title Bot : {Cbot} , Starting...")
print(f'\n Config file is {config_file} \n ')       # Confirming file position
logging.info(f'\n Config file is {config_file} \n ')

try:
    response = requests.get("https://discord.com/", timeout=5)
    print ("The request to Discord.com was successfull \n")
except Exception as e:
    print ("The request to Discord.com was unsuccessfull")             # Discord connection test (redundancy)
    logging.critical("Connection to discord.com was unssuccessfull, the program closed.")
    logging.critical(f"Errorcode : {e}")
    print(f"Maybe bad internet ? Error code : {e}")
    input()
    quit()

discord_api_key = config.get(Cbot, 'discord') # Using the config file to get the API tokens for Deepl and Discord
deepl_api_key = config.get(Cbot,'deepl')



Traduire = deepl.Translator(deepl_api_key)

gt = Translator()

print(f"Running on discord.py version {discord.__version__}")               
logging.info(f"Running on discord.py version {discord.__version__}")     

intents=discord.Intents.default()
intents.message_content = True 
intents.reactions = True                 # Creating the bot autorisations to have access to what it need
bot = commands.Bot(command_prefix='ATbot.', intents=intents)
bot.remove_command('help')


def ASCII(image_url, width , height):
    ASCII_CHARS = "@B%8WM#*oahkbdpwmZO0QCJYXzcvnxrjft/\|()1[]-_+~<>i!lI;:,\"^`\'. "
    try:
        # Open and download the image from the URL
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))

        # Resize the image while maintaining aspect ratio
        img = img.resize((width, height))

        # Convert the image to grayscale
        img = img.convert("L")

        img = Image.eval(img, lambda x: 255 - x)  # Invert colors by subtracting from 255

        # Calculate the aspect ratio to adjust the aspect ratio of ASCII characters
        aspect_ratio = img.height / img.width
        new_height = int(aspect_ratio * width)

        # Create an ASCII image
        ascii_img = ""
        for i in range(new_height):
            for j in range(width):
                pixel_value = img.getpixel((j, i))
                ascii_img += ASCII_CHARS[pixel_value * (len(ASCII_CHARS) - 1) // 255]
            ascii_img += "\n"

        return ascii_img

    except Exception as e:
        logging.error(f"An error occured while converting profile picture of the bot to ASCII")
        return ("An ewwor occuwed, no image, sowwy >-<")
        
 
startup_time = datetime.datetime.now()

def format_uptime(uptime):
    days = uptime.days
    seconds = uptime.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    uptime_str = ""
    if days > 0:
        uptime_str += f"{days} day{'s' if days > 1 else ''}, "
    if hours > 0:
        uptime_str += f"{hours} hour{'s' if hours > 1 else ''}, "
    if minutes > 0:
        uptime_str += f"{minutes} minute{'s' if minutes > 1 else ''}, "
    uptime_str += f"{seconds} second{'s' if seconds > 1 else ''}"
    
    return uptime_str


@tasks.loop(seconds=10)
async def status():
        uptime = datetime.datetime.now() - startup_time
        server_count = len(bot.guilds)
        if server_count == 0 or server_count > 1 :
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{server_count} servers'))
        else : 
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{server_count} server'))
        logging.info(f"The bot has been running for {format_uptime(uptime)}.")
        os.system(f"title  Bot : {Cbot} , Uptime : {format_uptime(uptime)}.")
           


@bot.event
async def on_ready():
    os.system('cls') # Clearing CLI to have no waste 
    print(f"Connected as {bot.user.name} (ID : {bot.user.id}) \n ")
    print(ASCII(bot.user.avatar,20,10))
    logging.info(f"Connected as {bot.user.name} (ID : {bot.user.id})")
    print(" ")
    for guild in bot.guilds:
        print(f"Bot autorisations on {guild.name} (server) :")
        logging.info(f"Bot autorisations on {guild.name} (server) :")
        try:
            for channel in guild.channels:
                try:
                    permissions = channel.permissions_for(guild.me)                             # Confirming connection and displaying the servers and channels it have access to
                    print(f"    - {channel.name}: {permissions}")
                    logging.info(f"    - {channel.name}: {permissions}")
                except Exception as e:
                    print(f"Failed to post permission, the error is: {e}")
                    logging.error(f"Failed to post permission, the error is: {e}")
        except Exception as error:
            print(f"Error on Channel in guild.channels loop, the error is: {error}")
            logging.error(f"Error on Channel in guild.channels loop, the error is: {error}")
        print(" ")
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
                embed = discord.Embed(title= f"Translation to {translate_langage}" ,description= f"{Traduire.translate_text(text_to_send, target_lang=langues_n_invert[translate_langage])}")
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
                    embed = discord.Embed(title= f"Deepl Translation to {lang_n[langues[flag]]}" ,description= f"{Traduire.translate_text(message.content, target_lang=langues[flag])}")
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

bot.run(discord_api_key)

input()
