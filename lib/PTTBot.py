#!/usr/bin/python3

import sys
import time
import json
import platform
import asyncio
import logging
import threading
import sounddevice as sd

import discord
from discord.ext import commands

import gpiozero
#import gpio
import RPi.GPIO as GPIO

from lib.radioSource import *
#import lib.chatSource

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT,initial=True)
#GPIO.setup(16,GPIO.IN,initial=False)
vhf_ptt = gpiozero.Button(16)

BOT_CONF = {}
with open('conf.json') as f:
    BOT_CONF = json.load(f)

logger = logging.getLogger("PTTBot")
logging.basicConfig(filename="/var/log/Motorola/PTT.log", level=logging.INFO, datefmt="%Y/%m/%d %H:%M:%S: ")

logger.info("discord.py version: {0}".format(discord.__version__))

class PTTBot:

    def __init__(self, *args, **kwargs):
#        super().__init__(self, *args, **kwargs)
        __version__="0.0.1"
        logger.info(f'PTT Bot version: {__version__}')
        self = commands.Bot(command_prefix='~', description="I talk on Radio")
        self.radioAudio = RadioAudioSource()
        self.voiceClient = None

        async def vhf_ptt_routine(self):
            print("Initiating VHF PTT")
            logger.info("[PTT]: VHF PTT initiated")
            await self.wait_until_ready()
            while not self.is_closed:
                if vhf_ptt.when_pressed:
                    print("Unmuted")
                    logger.info("[PTT]: Unmuted")
                if vhf_ptt.when_released:
                    print("Muted")
                    logger.info("[PTT]: Muted")
                await asyncio.sleep(1.3)

        async def periodicStateCheck(self):
            print("Initiating Periodic check")
            while True:
                await asyncio.sleep(0.25)

        @self.event
        async def on_ready():
            logger.info(f"[core]: Logged inn to Discord as {self.user.name}#{self.user.discriminator}")
            for i in self.get_all_channels():
                if i.name == "radio":
                    radio = i
            await radio.connect()
            self.loop.create_task(vhf_ptt_routine(self))
            self.loop.create_task(self.periodicStateCheck(self))
#            radio.listen(radioSink())

        @self.command(pass_context=True)
        async def kill(ctx):
            logger.info("[kill]: Killed by user")
            await discord.Client.close(self)

        self.run(BOT_CONF['DISCORD_BOT_KEY'])

