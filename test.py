from io import BytesIO

from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=['./Xephyr Expanded Italic.ttf'])


for i in range(0,1000):
	data = image.generate(str(i))
	image.write(str(i), './train/'+str(i)+'.png')