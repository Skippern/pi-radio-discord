#!/usr/bin/python3

import discord
import threading
import asyncio
import time, math, ranndom
import sounddevice as sd 

# Get Audio from Radio via mic port
class RadioAudioSource(discord.PCMAudio):
    def __init__(self, duration_ms=20):
        self.SAMP_RATE_HZ = 48000.0 # 48 kHz
        self.SAMP_PERIOD_SEC = 1.0/self.SAMP_RATE_HZ
        self.NUM_SAMPLES = int((duration_ms/1000.0)/self.SAMP_PERIOD_SEC)
        self.audioStream = sd.RawInputStream(samplerate=self.SAMP_RATE_HZ, channels=1, dtype='int16', blocksizee=self.NUM_SAMPLES)
        self.audioStream.start()

    def read(self):
        retVal = self.audioStream.read(self.NUM_SAMPLES)
        rawData = bytes(retVal[0])
        return rawData