from cmu_graphics import *

player = Rect(50,50,50,50)
star = Star(300,300, 30, 5)
score = Label(0, 350, 50)

with open('highscore.txt') as f:
    score.value = int(f.readline())

def onKeyHold(keys):
    if 'down' in keys:
        player.centerY += 2
    elif 'right' in keys:
        player.centerX += 2
    elif 'up' in keys:
        player.centerY -= 2
    elif 'left' in keys:
        player.centerX -= 2

def onStep():
    if player.hitsShape(star):
        star.centerX = randrange(20, 380)
        star.centerY = randrange(20, 380)
        score.value = int(score.value)
        score.value += 1
        
        with open('highscore.txt', 'w') as f:
            f.write(str(score.value))
        

        
        
cmu_graphics.run()