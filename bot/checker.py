import re, random, logging
from .checks.simple import active as simpleChecks
from .checks.command import active as commandChecks
from .checks.phrase import active as phraseChecks
from .modules.convBot import Conv
logger = logging.getLogger(__name__)


class Checker():
	def __init__(self, bot):
		self.bot = bot
		self.userdef = {}
		self.convBot = Conv()

	def check(self, message):
		if self.convBot and int(message['user_id']) == self.convBot.id and not message.get('chat_id'):
			ans = self.convBot.handleMes(message)
			if ans:
				logger.info('convBot was triggered')
				return self.packMessage(ans, message)

		if message['body'][0] == '/':
			ans = self.command(message['body'][1:], message)
			if ans:
				return self.packMessage(ans, message)

		if re.match('(М|м)ила,?.*', message['body']):
			try:
				text = re.split('(М|м)ила,? ', message['body'])[2]
			except IndexError:
				text = None

			for fun in simpleChecks:
				ans = fun(text, message)
				if ans:
					logger.info(str(fun.__name__) + ' was triggered')
					return self.packMessage(ans, message)

			ans = self.userdef.get(text)
			if ans:
				logger.info('userdef was triggered')
				return self.packMessage(ans, message)


		for fun in phraseChecks:
			ans = fun(message['body'], message)
			if ans:
				logger.info(str(fun.__name__) + ' was triggered')
				return self.packMessage(ans, message)


	def packMessage(self, messages, orig_message):
		ans = []
		if not type(messages) is list:
			messages = [messages]
		
		for message in messages:
			if type(message) is str or type(message) is int:
				message = {
					'message': str(message)
				}

			if not message.get('user_id') and not message.get('chat_id'):
				if orig_message.get('chat_id'): 
					message['chat_id'] = orig_message['chat_id']
				else:
					message['user_id'] = orig_message['user_id']
			ans.append(message)

		return ans

	def command(self, text, message):
		arg = re.split('; ', text)
		if arg[0] == 'setcommand':
			if len(arg) < 3:
				return '/setcommand; [запрос]; [ответ]'
			self.userdef[arg[1]] = arg[2]
			print(self.userdef)
			return 'Ok'

		elif arg[0] == 'conv':
			if arg[1] == 'init':
				self.convBot.setUser(arg[2], message['chat_id'])
				return 'OK'
			elif arg[1] == 'send':
				return self.convBot.createMessage(arg[2])
		else:
			for fun in commandChecks:
				ans = fun(arg[0], arg, message)
				if ans:
					logger.info(str(fun.__name__) + ' was triggered')
					return ans