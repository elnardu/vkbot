import random
from ..modules.imagesearchgoogle import imageSearch as iSearch

RESPONSES = {
    "привет": ["Привет, чел!", "Привет!", "Привет, {}!", "qq"],
    "пока": ["Прощай!", "Прощай, {}!", "Пока!", "Пока, {}!"],
    "доброе утро": ["Доброе!", "Проснись и пой!", "Доброе утро, {}!"],
    "спокойной ночи": ["Спокойной", "Приятных сновидений, {}!", "До завтра!"],
    "спокойной": ["Спокойной", "Приятных сновидений, {}!", "До завтра!"],
    "дай пять": ["Держи &#9995;!", "&#9995;"],
    "ping": ["pong", "poooooooooooong", "ping", "Да здесь я", "Не мешай спать"],
    "кит": ["Синий киииит"]
}

def dictResponses(text, message):
	variants = RESPONSES.get(text.lower())
	if variants:
		return random.choice(variants).format(*(message['_user']))
	
def nextImage(text, message):
    if text.lower() in ['далее', 'дальше', 'next', 'еще', 'ещё']:
        path = iSearch.get()
        if path:
            return {
                '_photo': path 
            }
        else:
            return "Картинок нет"

active = [dictResponses, nextImage]