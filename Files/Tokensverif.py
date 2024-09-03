import discord
import logging
from discord.ext import commands
import deepl

def DS_token(token):
    bot = commands.Bot(command_prefix='none', intents = discord.Intents.default())
    logging.info("Started the discord token checker")
    @bot.event
    async def on_ready():
        logging.info(f"Logged in as {bot.user.name}")
        print(f"Logged in as {bot.user.name}")
        await bot.close()
        return True
    
    @bot.event
    async def on_error(event, *args, **kwargs):
        if event == 'on_ready':
            print("Token verification failed.")
            logging.info("Token verification failed.")
            return False
        await bot.close()

    try:
        bot.run(token)
    except discord.LoginFailure:
        print("Token verification failed.")
        logging.info("Token verification failed.")
        return False

def DPL_token(token):
    logging.info("Started the deepl token checker")
    try :
        Traduire = deepl.Translator(token)
        print("Trying translation of \' Ceci est un test \' to EN-GB langage")
        logging.info("Trying translation of \' Ceci est un test \' to EN-GB langage")
        Tester = Traduire.translate_text('Ceci est un test', target_lang='EN-GB')
        print(f"Result : {Tester}")
        logging.info(f"Result : {Tester}")
        return True
    except : 
        print("Token verification failed.")
        logging.info("Token verification failed.")
        return False
    

def Namegrab(token):
    bot = commands.Bot(command_prefix='none', intents = discord.Intents.default())
    logging.info("Started the discord Bot Namegrabber")
    @bot.event
    async def on_ready():
        logging.info(f"Logged in as {bot.user.name}")
        print(f"Logged in as {bot.user.name}")
        Nam = bot.user.name
        await bot.close()
        return Nam
    @bot.event
    async def on_error(event, *args, **kwargs):
        if event == 'on_ready':
            print("Bot name grabber failed.")
            logging.info(" Bot name grabber failed.")
            return False
        await bot.close()

    try:
        bot.run(token)
    except discord.LoginFailure:
        print("Bot name grabber failed.")
        logging.info(" Bot name grabber failed.")
        return False
