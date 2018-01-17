#!/usr/bin/env python
# -*- coding: utf-8 -*-

from client import twitter

twitter.rss2Tweet("https://bitcoinblog.de/feed/", "storage/bitcoin_de.pkl", "BTC_de_Blog")

