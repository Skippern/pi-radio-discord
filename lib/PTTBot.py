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

