from io import BytesIO

from captcha.image import ImageCaptcha

#image = ImageCaptcha(fonts=['./Xephyr Expanded Italic.ttf'])

image=ImageCaptcha(fonts=['/usr/lib/python2.7/site-packages/captcha/data/DroidSansMono.ttf'])

#data=image.generate('1234')
#assert isinstance(data,BytesIO)
#image.write('1234', 'out.png')


for i in range(0,1000):
	data = image.generate(str(i))
	image.write(str(i), './train/'+str(i)+'.png')
