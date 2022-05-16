from cmu_graphics import *

Rect(50,50,150,150, fill='blue')

bob = Image('bob.png', 20, 20)
overture = Sound('1812.mp3')
print(overture)
overture.play()
bob.width=60
bob.height=60




cmu_graphics.run()