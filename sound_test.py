import os
from cmu_graphics import *
from playsound import playsound

Rect(50,50,150,150, fill='blue')
playsound(os.path.abspath('1812.mp3'))
bob = Image('bob.png', 20, 20)
overture = Sound('file:///' + os.path.abspath('1812.mp3'))
print('file://' + os.path.abspath('1812.mp3'))
print(overture)
#
# print(dir(overture))

overture.play()
bob.width=60
bob.height=60




cmu_graphics.run()