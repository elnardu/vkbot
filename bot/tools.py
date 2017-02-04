import requests
from .vkapi import vkapi as vk

class Tools():
	def __init__(self):
		self.vk = vk

	def uploadPhotoForMes(self, loc):
		upload_url = self.vk.photos.getMessagesUploadServer()['upload_url']

		img = [('photo', ('pic.png', open(loc, 'rb')))]
		res = requests.post(upload_url, files=img)
		data = res.json()

		img = self.vk.photos.saveMessagesPhoto(**data)[0]
		img = 'photo' + str(img['owner_id']) + '_' + str(img['id'])
		return img