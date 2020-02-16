#!/usr/bin/python3

import sys
import time
import json
import platform
import asyncio
import logging

import discord

logger = logging.getLogger("PTTBot")
logging.basicConfig(filename="/var/log/Motorola/PTT.log")

logger.info("discord.py version: {0}".format(discord.__version__))

class PTTBot:
    def __init__(self):
        __version__="0.0.1"
        logger.info(f'{__version__}')
        self = discord.ext.commands.Bot(command_prefix='~', description="I talk on Radio")
    
        @self.command(pass_context=True)
        async def kill(ctx):
            logger.info("[kill]: Killed by user")
            await discord.Client.close(self)


        self.run(BOT_CONF['DISCORD_BOT_KEY'])

