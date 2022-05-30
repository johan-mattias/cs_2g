from cmu_graphics import *

from level.level1 import *

with open('highscore.txt') as f:
    highscore = f.readline()
print(highscore)

drawScene()

Label(highscore, 100, 100)
highscore = int(highscore)
highscore += 5
with open('highscore.txt', 'w') as f:
    f.write(str(highscore))

player = Rect(20, 20, 30, 30)

cmu_graphics.run()