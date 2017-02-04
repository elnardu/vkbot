import random, datetime, re
from ..modules.vote import vote as voter

def faq(command, args, message):
	if command == "faq":
		return "Правила: \n- Их нет"

def convBot(command, args, message):
	if command == "conv":
		pass

def vote(command, args, message):
	if command == "vote":
		if args[1] == "create":
			return voter.set(args[2], args[3:])
		elif args[1] == "info":
			return voter.info()
		elif args[1].isdigit():
			return voter.vote(message['user_id'], int(args[1]))


active = [faq, vote]