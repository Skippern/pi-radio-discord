#!/usr/bin/python3

import sys
import asyncio
import time
import json
import platform
import discord

from lib.PTTBot import *

__VERSION__='0.0.1'

print("Python: {}".format(sys.version.split('\n')[0]))

BOT_CONF = {}

with open('conf.json') as f:
    BOT_CONF = json.load(f)

try:
    bot = PTTBot()
except:
    raise
