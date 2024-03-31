#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6693428081:AAF09WrPXKNW1eIBiTpQZYiiWNqnXruRsGU")
    API_ID = int(os.environ.get("API_ID", "23004101"))
    API_HASH = os.environ.get("API_HASH", "a2e157e87728053027cbb156e41a832a")
    AUTH_USERS = "5409975736"

