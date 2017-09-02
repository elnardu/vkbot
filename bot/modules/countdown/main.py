from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, random, datetime

path = os.path.dirname(os.path.abspath(__file__))


tzone = datetime.timezone(datetime.timedelta(hours=6))

def genImage(text, date, loc = path+'/../../tmp/countdown.png', photos_path = '/photos/'):
	photos_path = path + photos_path
	photos = os.listdir(photos_path)
	im = Image.open(photos_path+random.choice(photos))
	# im = im.filter(ImageFilter.GaussianBlur(10))

	im_w, im_h = im.size
	draw = ImageDraw.Draw(im, im.mode)

	deltatime = date - datetime.datetime.now(tzone)
	day = deltatime.days
	hour = int(deltatime.seconds/3600)
	minute = round((deltatime.seconds - hour*3600)/60)

	text += "\n"

	if day == 31 or day == 1 or day == 21:
		text += "остался\n"+str(day)+" день"
	elif day == 22 or day == 23:
		text += "осталось\n"+str(day)+" дня"
	elif day == 25 or day == 26 or day == 0:
		text += "осталось\n"+str(day)+" дней"
	elif day >= 5:
		text += "осталось\n"+str(day)+" дней"
	elif day < 5:
		text += "осталось\n"+str(day)+" дня"
	
	text += "\n"

	if hour >= 22 or hour in [2, 3, 4]:
		text += str(hour) + " часа"
	elif hour == 21 or hour == 1:
		text += str(hour) + " час"
	elif hour <= 20 and hour >= 5:
		text += str(hour) + " часов"

	text += "\n"

	text += str(minute) + " мин"

	font = ImageFont.truetype(path+'/BebasNeue2.ttf', round(im_h/6))
	text_w, text_h = draw.multiline_textsize(text, font, spacing=10)
	draw.multiline_text((im_w/16, im_h/2 - text_h/2), text, '#ffffff', font, spacing=10)

	# xy = (im_w-700, im_h/2-250, im_w-200, im_h/2+250)

	# draw.pieslice(xy, 360-360*day/92-90, 270, fill='#ffffff')
	# draw.ellipse(xy, outline='#ffffff')

	im.save(loc, 'PNG')
	return loc


__all__ = ['genImage', 'tzone']
