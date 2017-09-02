from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, datetime

path = os.path.dirname(os.path.abspath(__file__))
tzone = datetime.timedelta(hours=6)
now = datetime.datetime.now()

config = {
	'margin': 50,
	'height': 140,
	'tstart': 180,
	'tmargin': 10,
	'width': 900
}

counters = {
	'До городской олимпы': datetime.datetime(2017, 2, 27),
	'До начала каникул': datetime.datetime(2017, 3, 20),
	'До начала лета': datetime.datetime(2017, 6, 1),
	# 'До городской олим': datetime.datetime(2017, 2, 27)

}

headerText = 'M' + datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=6))).strftime("%d/%m/%y %H:%M")
textSize = 100

def genImage():
	photos_path = path + '/../../tmp/public.png'
	im = Image.open(path + '/cover.png')
	im_w, im_h = im.size
	draw = ImageDraw.Draw(im)
	draw.line([
		config['width'],
		config['height'] + config['margin'],
		config['width'],
		im_h - config['margin']
		], fill='white', width=10)

	draw.line([
		config['margin'],
		config['height'],
		im_w - config['margin'],
		config['height']
		], fill='white', width=10)

	font = ImageFont.truetype(path+'/BebasNeue2.ttf', textSize)
	draw.text((config['margin'], config['height']/2 - textSize/2), headerText, fill="white", font=font)

	start = config['tstart']
	for c in counters:
		date = counters[c] - now + tzone
		date = str(date.days) + 'д.'
		# text = '{}: {}д'.format(c, date.days)
		draw.text((config['margin'], start), c, fill="white", font=font)
		draw.text((config['margin'] + config['width'], start), date, fill="white", font=font)
		start += config['tmargin']*2 + textSize



	im.save(photos_path, 'PNG')

genImage()