import random, datetime, re
from ..modules.countdown.main import genImage, tzone
from ..modules.imagesearchgoogle import imageSearch as iSearch


RESPONSES = {
	"привет": ["Привет, чел!", "Привет!", "Привет, {}!", "qq"],
	"пока": ["Прощай!", "Прощай, {}!", "Пока!", "Пока, {}!"],
	"как дела?": ["Отлично!", "Так себе.", "...", "Жизнь - тлен"],
	"ping": ["pong", "poooooooooooong", "ping", "Да здесь я", "Не мешай спать"],
	"я тебя люблю": ["<3", "А я тебя нет!", "Иди нафиг. Мне не до этого"],
	"молодец": ["Спасибо!", "Ты тоже молодец!"],
	"ты молодец": ["Спасибо!", "Ты тоже молодец!"],
	"кто": ["Мой выбор {} {}!", "Определенно это {} {}!", "Это {} {}!", "Я выбираю {} {}!"],
	"не расстраивайся": ["Да нормально все", "Спасибо {}"]
}

RESPNOTHING = ["Что?", "Я слушаю", "Дай мне поспать!", "{}, займись лучше делом!"] 

def dictResponses(text, message):
	variants = RESPONSES.get(text.lower())
	if variants:
		return random.choice(variants).format(*(message['_user']))

def respNothing(text, message):
	if not text:
		return random.choice(RESPNOTHING).format(*(message['_user']))

def countDown(text, message):
	if text == 'осталось':
		date = datetime.datetime(2017, 1, 9, 0, 0, 0, tzinfo=tzone)
		text = 'До конца каникул'
		path = genImage(text, date)

		return {
			'_photo': path 
		}

def countDownSher(text, message):
	if text.lower() in ['осталось до шерлока', 'шерлок', 'когда шерлок', 'когда шерлок?']:
		date = datetime.datetime(2017, 1, 9, 3, 0, 0, tzinfo=tzone)
		text = 'До новой серии Шерлока'
		path = genImage(text, date, photos_path='/sher/')

		return {
			'_photo': path 
		}

def imageSearch(text, message):
	if re.match('найди ', text):
		query = re.split('найди ', text)[1]
		iSearch.search(query)
		path = iSearch.get()
		if path:
			return {
				'_photo': path 
			}
		else:
			return "Картинок нет"


def mishaIdetNah(text, message):
	if str(message['user_id']) == "219431294":
		return {
			'message': 'Иди нахер',
			'forward_messages': message['id']
			}

active = [imageSearch, dictResponses, respNothing, countDown, countDownSher]