#!/usr/bin/env python
# -*- coding: utf-8 -*-

from client import twitter

twitter.rss2Tweet("https://www.btc-echo.de/feed/", "storage/btc_echo.pkl", "BitcoinEcho")

