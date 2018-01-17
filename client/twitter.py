import time
import pickle
import feedparser
import os.path

from . import parameters


'''
Storage of already tweeted topics.
'''
class TweetStorage:
	_storage = {}
	_pkFile = ''

	def __init__(self, storageFile):
		self._pkFile = storageFile

	def addUrl(self, url, title):
		self._storage[url] = title

	def hasUrl(self, url):
		if url in self._storage:
			return True
		return False

	def save(self):
		with open(self._pkFile, 'wb') as f:
			pickle.dump(self._storage, f, pickle.HIGHEST_PROTOCOL)

	def load(self):
		if os.path.isfile(self._pkFile):
			with open(self._pkFile, 'rb') as f:
				self._storage = pickle.load(f)

'''
Common tweeter
'''
class Tweeter:
	_storage = None
	_viaUserRef = None

	def __init__(self, storage, viaUserRef):
		self._storage = storage
		self._viaUserRef = viaUserRef
		self._storage.load()

	def sendTweet(self, url, title):
		if not self._storage.hasUrl(url):
			message = url

			if self._viaUserRef:
				message += " via @" + self._viaUserRef

			parameters.twitterAPI.update_status(message)

			print("new tweet: \"" + title + "\"")

			self._storage.addUrl(url, title)
			self._storage.save()

'''
Tweet from RSS resource
'''
def rss2Tweet(rssFeed, storageFile, viaUserRef):
	data = feedparser.parse(rssFeed)

	tweeter = Tweeter(TweetStorage(storageFile), viaUserRef)

	for i in range(len(data['entries'])):
		title = data['entries'][i].title
		url = data['entries'][i].link

		tweeter.sendTweet(url, title)
		time.sleep(5)

