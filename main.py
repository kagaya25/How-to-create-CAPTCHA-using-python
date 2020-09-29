from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

audio = AudioCaptcha()
image = ImageCaptcha()

data = audio.generate('1234')
audio.write('1234', 'out.wav')

data = image.generate('1234')
image.write('1234', 'out.png')