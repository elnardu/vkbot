import requests, re, urllib.request, os
from requests.auth import HTTPBasicAuth

class ImageSearch():
	def __init__(self):
		self.images = []
		self.i = 0
		self.accountKey = '7eVcnP5VwK81iV4xGz0w0zAZ1lpZXnYUIZiNEiugwEA'    #accountKey for bing image search

	def search(self, query):
		req = "https://api.datamarket.azure.com/Bing/Search/Image?$format=json&$top=50&Adult=%27Off%27&Query=%27" + re.sub(' ', '+', query) + "%27"
		resp = requests.get(req, auth=HTTPBasicAuth(self.accountKey, self.accountKey))
		self.i = 0
		self.images = resp.json()['d']['results']

	def get(self):
		try:
			url = self.images[self.i]['MediaUrl']
			loc = self.download(url)
			while not loc:
				self.i += 1
				url = self.images[self.i]['MediaUrl']
				loc = self.download(url)
			self.i += 1
			return loc
		except IndexError:
			return None

	def download(self, url):
		location = os.path.dirname(os.path.abspath(__file__)) + '/../tmp/picsearch.jpg'
		try:
			urllib.request.urlretrieve(url, location)
			return location
		except Exception:    
			return None

imageSearch = ImageSearch()
__all__ = ['imageSearch']