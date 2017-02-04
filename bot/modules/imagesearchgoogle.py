import requests, re, urllib.request, os

class ImageSearch():
	def __init__(self):
		self.images = []
		self.i = 0
		self.cx = '017358699897649552919:muspvxvgrca'
		self.apikey = 'AIzaSyCrsCIe1aiHBL074B9XoNqSpRkrvgOSjQU'

	def search(self, query):
		params = {
			'cx': self.cx,
			'key': self.apikey,
			'q': query,
			'searchType': 'image',
			'safe': 'off'
		}
		req = 'https://www.googleapis.com/customsearch/v1'
		resp = requests.get(req, params = params)
		self.i = 0
		self.images = resp.json()['items']
		# print(self.images)

	def get(self):
		try:
			url = self.images[self.i]['link']
			loc = self.download(url)
			while not loc:
				self.i += 1
				url = self.images[self.i]['link']
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