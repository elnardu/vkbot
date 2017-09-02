

class Conv():
	def __init__(self):
		self.id = None
		self.chat_id = None

	def setUser(self, id, chat_id):
		self.id = int(id)
		self.chat_id = int(chat_id)

	def handleMes(self, message):
		return {
			"chat_id": self.chat_id,
			"forward_messages": message['id']
		}
		
	def createMessage(self, text):
		return {
			'user_id': self.id,
			'message': text
		}