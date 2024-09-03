# -----------------------------------------------------------------------------
#  Tokenverif.py
#  Copyright (c) 2024 Asha the Fox 🦊
#  All rights reserved.
#
#  This module provides functions to verify API tokens for Discord and DeepL.
#  It is intended to be used as a library to support the main script (AT_bot.py).
#  
#  Functions:
#      run_bot(bot, token) - Boots the discord bot (used in DS-token function)
#      DS_token(token) - Verifies the validity of a Discord bot token.
#      DPL_token(token) - Verifies the validity of a DeepL API token.
# -----------------------------------------------------------------------------

__author__ = "Asha Geyon (Natpol50)"
__version__ = 0.5
__all__ = ['run_bot', 'DS_token', 'DPL_token']

import discord
import logging
from discord.ext import commands
import deepl

def run_bot(bot, token):
    """
    Runs the bot with a given token.
    
    Args:
    - bot(commands.Bot): The bot instance
    - token(str): The bot token to run

    Returns:
    - bool: True if the token is valid, False otherwise
    """
    try:
        bot.run(token)
    except discord.LoginFailure as E:
        print("Token verification failed.")
        logging.info(f"Token verification failed. ({E})")
        return False

def DS_token(token):
    """
    Function to check the validity of a Discord bot token.
    
    Args:
    - token (str): The Discord bot token to verify.
    
    Returns:
    - bool: True if the token is valid, False otherwise (from the run_bot function).
    """
    logging.info("Started the Discord token checker.")
    bot = commands.Bot(command_prefix='none', intents=discord.Intents.default())
    return run_bot(bot, token)

def DPL_token(token):
    """
    Function to check the validity of a DeepL API token.
    
    Args:
    - token (str): The DeepL API token to verify.
    
    Returns:
    - bool: True if the token is valid, False otherwise.
    """
    logging.info("Started the DeepL token checker.")

    try:
        translator = deepl.Translator(token)
        logging.info("Attempting to translate 'Asha le renard semble content' to English (EN-GB).")
        result = translator.translate_text('Asha le renard semble content', target_lang='EN-GB')
        logging.info(f"Translation result: {result}")
        print(f"Translation result: {result} \n Everything seems right")
        return True
    except Exception as E:
        logging.error(f"Token verification failed: {E}")
        print("Token verification failed.")
        return False

if __name__ == "__main__":
    print("This is a library module and is not intended to be run directly, please use AT_bot.py .")