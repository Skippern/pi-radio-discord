# pi-radio-discord
**Discord to Motorola Radio on Raspberry Pi Bot**

The purpose is to create a private PTT discord channel that listens to a Motorola UHF radio,
and selected users having the ability to talk back over the radio. 

# Background

The project started with an idea by the project creators during the Convention 2020 LAN event
in Kristiansund, Norway. 

# Equipment during development

* Motorola DM 3400 stationary VHF tranciver
* Raspberry Pi with Raspian OS
* Discord server

# Install requirements

* Python3
* discord.py
* logging python module
* Discord server with a PTT voice channel named `radio`

# Config file

You need to create a config file named `config.json` with the following content
```json
{
    "DISCORD_BOT_KEY": "<your_discord_bot_application_key>"
}
```

# Motorola Pinning

TBC

# Raspberry Pinning

TBC

