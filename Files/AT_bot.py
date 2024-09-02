import subprocess
import os
import logging

def log_init():
    log_folder = (f'{pathlib.Path(__file__).parent.absolute()}\logs')

    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    log_file = os.path.join(log_folder, f"{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}.log") # Name of the logfile will be YY-MM-DD_Hour-Minutes-seconds (Of the moment which the bot started)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s]: %(message)s",   # Specify the log file Naming schema
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("Script started.")
 
flag_file = "Firstr.flag"           # Specify the 1st time setup flag

if not os.path.exists(flag_file):
    print("As this is the first the script is running, the script will install the depedencies.")
    try:
        subprocess.check_call(['pip', 'install', 'pathlib'])
    except subprocess.CalledProcessError:
        print(f"Error installing: pathlib")
    import pathlib
    import datetime
    import install
    log_init()
    logging.info("First time setup, installing dependencies")
    install.libraries([
    'discord.py',
    'googletrans==4.0.0-rc.1',                  # Check if the first time setup flag is present and if not, install the dependencies using the install.py file
    'typing',
    'requests',
    'configparser',
    'windows-curses',
    'Pillow',
    'deepl'
])
    with open(flag_file, "w") as file:
        file.write("Flag indicating that the script has run")              # Create the first time setup flag
else:
    logging.info("Script as already ran before, skipping installing the dependencies ")



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




os.system("title ATbot, Welcome ! ") #Welcome page / Copyright ?
print("""                      .::^^^^:..                     
                :!J5GB#&&@@@&&&#BPY7~.               
            .!5B&@@@&&&&&&&&&&&&&&@@@&GJ^            
          ~5&@@&&###################&&@@@B?:         
        !B@@&###########################&@@&Y:       
      ^G@@&#######&&&&&&##################&@@&?      
     7&@&########&#YYPB#&&##################&@@G:    
    J@@&###&&&&&&&Y^^^^~JB&##############&&##&&@B:   
   7@@####&BGGPP55!^~::^~755PGB#&&&&##&&&GG&###@@B.  
  :&@&####&PY#BP?~:::~?JJ5#&@@@@@@@@@@@@@#B&###&@@J  
  ?@&#####&BJ#@@@&G?7JJJJ&@&#&&@@@@@@@@@@@@#####&@#. 
  P@&######&5J#@@@#JJJJJJP@@@@@@@@@@@@@@@@&#####&@@~ 
  B@&######&#J~G@@Y?JJJJJ?YPB##&@@@@@@@@&&######&@@! 
  P@&#######&B!!G#JJJJJJJ??J5G#&@@@@@@&&########&@@^ 
  7@&########&#PJJJJJJJ?J5B&@@@@@@@@&&##########&@B  
  .B@&########&&BYJJJJ?5#@@@@@@@@&#BB##&&&&#&&#&@@7  
   ~&@&#########&G?J?JB@@@@@@@@BYJ????5GGB##BB&@@5   
    !&@&########&G??Y#@@@@@@@#Y???????????JJ??YPP.   
     ^B@&#######&G?J#@@@@@@@G????????????????????^   
      .Y&@&#####&5?Y&GP#@@@G?????5GG5????????????7.  
        :Y&@&&###JJJJY&@@@#?????J#  #J??JG#5!?????:  
          :?G&@@GJJ?Y&@@@@Y7?????YP Y???Y5^ .?????^  
             :75B&#B#@@@@@&PJ??Y5Y???????!^~7?????:  
                 :~7Y5GGGGBBP?77??~^~!777777?????7   
                                         .!7???7!:         
         Welcome to Asha's Autotranslation bot ! 
        Please, do not claim property of this code   """)
input("""
      
               press enter to continue""")

os.system('cls') # Clearing CLI to have no waste 


def BotPicker(input_list):  # Bot / Profile picker, using the Curses library, create a fake GUI in CLI

    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)         
    curses.noecho()

    selected_index = 0

    while True:
        stdscr.clear()
        #Display instruction text
        stdscr.addstr("\n Choose a bot, or choose \'New bot\' to create a new bot/profile. \n \n ")
        # Display the list with one element highlighted
        stdscr.addstr("")
        for index, element in enumerate(input_list):
            if index == selected_index:
                stdscr.addstr(f"{index + 1}. {element}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(f"   {element}\n")

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_DOWN:
            selected_index = min(selected_index + 1, len(input_list) - 1)
        elif key == curses.KEY_UP:
            selected_index = max(selected_index - 1, 0)
        elif key == 10:  # Enter key
            curses.endwin()  # Clean up the curses environment
            return input_list[selected_index]

config = configparser.ConfigParser()
configfile = (f'{pathlib.Path(__file__).parent.absolute()}\config.ini')
if not os.path.exists(configfile):                 # Open/Create the config.ini file
    with open(configfile, 'w') as file:
        file.write(" ")


os.system("title ATbot, ConfigPicker ")        # Change windows name
config.read(configfile)
Botlist = config.sections()   # Pull the bot/config names
Botlist.append('New bot')     # Add the New bot option
Cbot =BotPicker(Botlist)      # Start the bot/profile picker 
print(" ")

os.system('cls') # Clearing CLI to have no waste 
os.system("title ATbot, New bot : ")
if Cbot == 'New bot' : 
    Name = input ("Choose a name for the new bot : ")
    os.system("title New bot, discord bot API key ")
    print("""                              .:~!7?JYY7.                    .?JJJ?7!^:.                            
                         :~7J5PGGP5J7~::..::^^~~~~!!!~~~^^::.:^~!7?Y5PPPY?!^.                       
                     .~?YPGGG5J7~~~!7?JY5PPPPGGGGGPYYYYYYYYYYYYJJ?7!!!7?YPGGPY7^.                   
                   :7YGGGPYJ???Y5PGGGGGGGGGGPPPPPG5777??????????JJJYYYYJ???J5PGG5?^                 
                  ~5GGP5YY5PPGGGGGPPPPPPPPPPPPPPPPPPBPJ?????????????????JJYYJYY5GGP~                
                 ~5GPPPPPGGGPPPPPPPPPPPPPPPPPPPPPPB@@@BPPPPPPPPPPPPY?????????JJYPGGP~               
                ~5GPPPPGPPPPPPPPPPPPPPPPPPPPPPPPPPB@@&5YYYYYYYYYPGG5???????????7?YPGP~              
               ^5GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB@@@GYJ??????7YGG5????????YB#GJ7JPG5^             
              .YGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB@@@@@@G55PY?JPBG5????????5&@@&J7?PGY.            
              ?GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB@@@&BGY??P5Y&@@#577??????JP#&#J??JPG?            
             !PGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB@@&YYB#BP##&@@@@&BPG##P????JYJ????JGG!           
            :5GPPPPPPPPPPPPPPPPPPPPGGGGGGPPPPPPPPPB@@&J5@@@@@@@&&&@@@@@@@B????????????5G5:          
            ?PPPPPPPPPPPPPPPPPPPGGGP5555PGGGPPPPPPG&@&5J&@@@&#B####B&@@@@P77???????????PG?          
           ^5GPPPPPPPPPPPPPPPPPGP?~:.  .:~?PGPPPPG5?55P#@@@&GB@@@@@#G#@@@@G5Y??????????YGP^         
           ?GPPPPPPPPPPPPPPPPPGJ:          :JGPPPG57P@@@@@@BPB@@@@@#PG@@@@@@#???????????PG?         
          ^5GPPPPPPPPPPPPPPPPGY             .YGPPG577?Y#@@@&GPGB#BGPP#@@@@BPY???????????5GP:        
          !PGPPPPPPPPPPPPPPPPG7              7GPPG57~  ~#@@@&#GGGGGB&@@@@P77????????????JPG!        
         .JGPPPPPPPPPPPPPPPPPGJ              YGPPG5?7!:?&@@@@@@@@@@@@@@@@B???????????????PGY        
         ^5GPPPPPPPPPPPPPPPPPPG?.          .JGPPPG5???7Y#&#GB#@@@@@&#GB&&G???????????????YGP:       
         !PPPPPPPPPPPPPPPPPPPPPG57:.    .^75GPPPPG5????7???77?5@@@B??7???7???JY5PY???????JPG~       
         ?GPPPPPPPPPPPPPPPPPPPPPGGP5YJJY5PGGPPPPPPP555555Y55YYY55Y?7????JY55PGGPPY????????PG7       
        .YGPPPPPPPPPPPPPPPPPPPPPGPGGGGGGGGPPPPPPPPPGGGGGGGPPPPP555YJY5PPPGPGPPPPPGP???????5G?       
        .YGPPPPPPPPPPGPB@@@@@@@GPGPPPPPPPPPPPP&@@@@@@@@@@@@@@&&#BPPPGGGGPPB@@@@@GPP??????5PGJ       
         ?PGGPPPPPPPGPG@@@@@@@@&PPPPGGGPPPPPPP&@@@@@@@@@@@@@@@@@@@#PPPP5PP#@@@@@BPP???J5PGGG7       
          ~YPGGPPPPPPP&@@@@&@@@@#PPP55PPGGGGPP&@@@@&BBB######&@@@@@&PPPJPP#@@@@@GPPJYPGGGG5~        
            ~JPGGGPP5#@@@@&G&@@@@BPG7 .:^~!YGP&@@@@&PP5?77!75GB@@@@@&PPPPP#@@@@@GPPGGGGPJ~          
              :!JPGPB@@@@&GPB@@@@@GPP^     7GP&@@@@&PG7     ^PP#@@@@@GPPPP#@@@@@GPGGPJ!:            
                :5PG@@@@@BPGP#@@@@&PP5.    ?GP&@@@@&PG7 ....!GP#@@@@@GPGPP#@@@@@GPP~.               
               .JPP&@@@@#PPYPG&@@@@#5GJ    7GP&@@@@&PP5Y5Y55P5G&@@@@&GG5PP#@@@@@GG5.                
               7PP#@@@@&GG5?PPG&@@@@BPG!   7GP&@@@@&BBBBBBBB#&@@@@@&BGY~PPB@@@@@GP5.                
              ^PPB@@@@&GPPPPPPPB@@@@@GPP^  7GP&@@@@@@@@@@@@@@@@@@@#BGJ.:PPB@@@@@GP5.                
             :YPG@@@@@@&&&&&&&&&@@@@@&PG5. ?GP&@@@@@@@@@@@@@@&&&#BPJ~  :PP#@@@@@GG5.                
            .JPP&@@@@@@@@@@@@@@@@@@@@@#5GJ 7GP&@@@@&GGGGGGGGPP5Y?!:    :PP#@@@@@GG5.                
            !PP#@@@@@#############@@@@@BPG!7GP&@@@@&PG?::::::..        :PP#@@@@@GG5.                
           ^5PB@@@@@#P5????????JPG&@@@@@GPP5PP&@@@@&PG!                :PP#@@@@@GG5.                
          :YPG@@@@@&GP~         ?GG&@@@@&PPGPP&@@@@&PG7                :PP#@@@@@GG5.                
          ?GG&@&&&&BP7          .5GB&&&&&#PGGG&&&&&&GG7                :PG#&&&&&BG5.                
          ^JY55555YJ!.           :J5PPPPPP5YJ5PPPPPP5J:                 !Y5PPPPP5Y~                 
             ....                  ........  ........                     .......                  \n""")

    print('  As you chose New bot, you\'ll need a discord bot API key. \n If you do not know how to get one, here\'s a tutorial : https://rapidapi.com/volodimir.kudriachenko/api/DiscordBot/details')
    Test = False
    while Test == False : 
        DSapi_k = input("\n Discord bot API key : ")
        print("Starting discord token verification...")       # Discord token verification using the Tokenverif.py file
        logging.info("Starting discord token verification.")
        Test = Tokensverif.DS_token(DSapi_k)
    logging.info("Token verification was successful, continuing...")

    
    os.system("title New bot, Deepl API key ")
    print("""
                                             ..::::::..                                             
                                          ..::::::::::::..                                          
                                      ..::::::::::::::::::::..                                      
                                  ..::::::::::::::::::::::::::::..                                  
                               ..::::::::::::::::::::::::::::::::::..                               
                           ..::::::::::::::::::::::::::::::::::::::::::..                           
                        .::::::::::::::::::::::::::::::::::::::::::::::::::.                        
                      .:::::::::::::::::...::::::::::::::::::::::::::::::::::.                      
                      :::::::::::::::.       .::::::::::::::::::::::::::::::::                      
                      :::::::::::::::         .:::::::::::::::::::::::::::::::                      
                      :::::::::::::::          .::::::::::::::::::::::::::::::                      
                      ::::::::::::::::.     ..    ..::::::::::::::::::::::::::                      
                      :::::::::::::::::::::::::..    ..:::::::::::::::::::::::                      
                      :::::::::::::::::::::::::::::..    .      .:::::::::::::                      
                      :::::::::::::::::::::::::::::::::.         .::::::::::::                      
                      ::::::::::::::::::::::::::::::::::.        .::::::::::::                      
                      ::::::::::::::::::::::::::::::.::::.      .:::::::::::::                      
                      ::::::::::::::::::::::::::..    ::::::..::::::::::::::::                      
                      ::::::::::::::::...  ....    ..:::::::::::::::::::::::::                      
                      :::::::::::::::.         ..:::::::::::::::::::::::::::::                      
                      :::::::::::::::         .:::::::::::::::::::::::::::::::                      
                      :::::::::::::::.       .::::::::::::::::::::::::::::::::                      
                      .::::::::::::::::.....:::::::::::::::::::::::::::::::::.                      
                        ..::::::::::::::::::::::::::::::::::::::::::::::::..                        
                            ..::::::::::::::::::::::::::::::::::::::::..                            
                                ..::::::::::::::::::::::::::::::::..                                
                                   ..:::::::::::::::::::::::::::.                                   
                                       ..:::::::::::::::::::::::                                    
                                           ..:::::::::::::::::::                                    
                                              ..::::::::::::::::                                    
                                                  ..::::::::::::                                    
                                                      ..::::::::                                    
                                                         ..:::::                                    
:::::::::::::..                                              ...                       .::::        
::::::::::::::::.                                                                      .::::        
::::.       .:::::.        ....:....             ....:....        ..    ....:...       .::::        
::::.         :::::      .::::::::::::.       .::::::::::::.     .:::..:::::::::::.    .::::        
::::.         .::::.   .::::..    .::::.     .::::.    ..::::.   .::::::... ...::::.   .::::        
::::.          ::::.   ::::.........::::.   .::::.........::::   .:::::        .::::.  .::::        
::::.         .::::.  .::::::::::::::::::   ::::::::::::::::::.  .::::.         ::::.  .::::        
::::.        .::::.   .::::..............   :::::..............  .:::::         ::::.  .::::        
::::.      ..::::.     .:::..      ...      .::::.       ...     .::::::.     .::::.   .::::.       
::::::::::::::::.       .::::::::::::::       .:::::::::::::.    .::::::::::::::::.    .::::::::::::
::::::::::::..            ..::::::::..          ..:::::::..      .::::...::::::..       ::::::::::::
                                                                 .::::                              
                                                                 .::::                              
                                                                 .::::                             """)
    
    print('  Now, you\'ll need a Deepl API (Free or Paid, both works fine for a reasonable amount of messages per month)\n If you do not know how to find yours, here\'s a tutorial : https://support.deepl.com/hc/en-us/articles/360020695820-Authentication-Key')
    
    Test = False
    while Test == False : 
        DPLapi_k = input("\n Deepl API key : ")
        print("Starting deepl token verification...")       # Deepl token verification using the Tokenverif.py file
        logging.info("Starting deepl token verification.")
        Test = Tokensverif.DPL_token(DPLapi_k)
    logging.info("Token verification was successful, continuing... \n")
    

    config[f"{Name}"]={
    "discord" : DSapi_k,
    "deepl" : DPLapi_k
    }                               # Writing the config into the config.ini file
    with open(configfile,"w") as fichier_objet:
        config.write(fichier_objet)
    Cbot = Name
os.system(f"title Bot : {Cbot} , Starting...")
print(f'\n Config file is {configfile} \n ')       # Confirming file position
logging.info(f'\n Config file is {configfile} \n ')

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
