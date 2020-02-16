#!/usr/bin/python3

import sys
import time
import json
import platform
import asyncio
import logging

import discord
from discord.ext import commands

BOT_CONF = {}
with open('conf.json') as f:
    BOT_CONF = json.load(f)

logger = logging.getLogger("PTTBot")
logging.basicConfig(filename="/var/log/Motorola/PTT.log", level=logging.INFO, datefmt="%Y/%m/%d %H:%M:%S: ")

logger.info("discord.py version: {0}".format(discord.__version__))

class PTTBot:
    def __init__(self):
        __version__="0.0.1"
        logger.info(f'{__version__}')
        self = commands.Bot(command_prefix='~', description="I talk on Radio")

        @self.event
        async def on_ready():
            logger.info(f"[core]: Logged inn to Discord as {self.user.name}#{self.user.discriminator}")
            for i in self.get_all_channels():
                print(f"{i.name}")
                if i.name == "radio"
                    radio = i
            await radio.connect()

        @self.command(pass_context=True)
        async def kill(ctx):
            logger.info("[kill]: Killed by user")
            await discord.Client.close(self)

        self.run(BOT_CONF['DISCORD_BOT_KEY'])

