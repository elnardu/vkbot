import time, logging
from .checker import Checker
from .tools import Tools
from .vkapi import vkapi as vk
from .config import config


logger = logging.getLogger(__name__)
logging.getLogger("requests").setLevel(logging.WARNING)

import coloredlogs
coloredlogs.DEFAULT_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# coloredlogs.install(level="DEBUG")
coloredlogs.install()


class Bot():
	def __init__(self):
		logger.info("Starting bot...")

		self.vkapi = vk
		self.usernames = {}
		self.checker = Checker(self)
		self.tools = Tools()
		self.update_interval = config['UPDATE_INTERVAL']

		logger.info("Bot started")

	def start_update_loop(self):
		logger.info("Started update loop with update interval {}sec".format(self.update_interval))
		self.lastmessage_id = self.vkapi.messages.get(count = 1)['items'][0]['id']

		# self.handleMessages(self.vkapi.messages.get(count = 1)['items'])

		while True:
			try:
				messages = self.vkapi.messages.get(last_message_id = self.lastmessage_id)['items']
				self.handleMessages(messages)
				time.sleep(self.update_interval)
			except Exception as e:
				logger.error(e)

	def handleMessages(self, messages):
		for message in messages:
			self.lastmessage_id = max(self.lastmessage_id, message['id'])
			message['_user'] = self.getUsername(message['user_id'])
			logger.info('> {} {}({}): {}'.format(*(message['_user']), message['user_id'] , message['body']))
			ans = self.check(message)
			if ans:
				self.handleAnswers(ans)

	def check(self, message):
		if not message['body']:
			return
		return self.checker.check(message)

	def handleAnswers(self, messages): 
		if type(messages) is list:
			for message in messages:
				self.sendMessage(message) # send messages by one if messages is list
		else:
			self.sendMessage(messages)

	def sendMessage(self, message):
		if message.get('_photo'):
			attachment = self.tools.uploadPhotoForMes(message.get('_photo'))
			message['attachment'] = attachment
			message.pop('_photo')

		self.vkapi.messages.send(**message)
		if message.get('attachment'):
			logger.info('< {}'.format(message.get('attachment')))
		else: 
			logger.info('< {}'.format(message.get('message')))

	def getUsername(self, id):
		name = self.usernames.get(id)
		if not name:
			data = self.vkapi.users.get(user_ids = id, lang = 'ru')[0]
			self.usernames[id] = [data['first_name'], data['last_name']]
			name = [data['first_name'], data['last_name']]
		return name

