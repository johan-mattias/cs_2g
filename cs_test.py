from cmu_graphics import *
from playsound import playsound
Rect(50,50,150,150, fill='blue')

bob = Image('bob.png', 20, 20)
playsound('1812.mp3')
#music = Sound('https://s3.amazonaws.com/cmu-cs-academy.lib.prod/sounds/1812-overture-finale.mp3')
# really great stuff
print(overture)
print(music)
#
# print(dir(overture))

#overture.play()
music.play()
bob.width=60
bob.height=60




cmu_graphics.run()