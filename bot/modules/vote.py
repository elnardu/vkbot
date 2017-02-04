

class Vote():
	def __init__(self):
		self.question = ""
		self.voted = []
		self.choices = []
		self.ans = {}

	def clear(self):
		self.question = ""
		self.voted = []
		self.choices = []
		self.ans = {}

	def set(self, question, choices):
		self.clear()
		self.question = question
		self.choices = choices
		print(self.question)
		return "Голосование началось!"

	def vote(self, id, choice):
		if id in self.voted:
			return "Ты уже голосовал!"
		else:
			self.voted.append(id)
			if not self.ans.get(choice):
				self.ans[choice] = 1
			else:
				self.ans[choice] += 1

			return "Голос учтен"

	def info(self):
		mes = ""
		mes += self.question + "\n"
		for i in range(0, len(self.choices)):
			mes += '\n'
			mes += '{}. {} - {}'.format(i, self.choices[i], self.ans.get(i))
		print(mes)
		return mes

vote = Vote()
__all__ = ['vote']


			