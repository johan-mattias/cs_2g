from cmu_graphics import *

player = Rect(200,200,30,30)

def movePlayer():
    player.centerX += 1
    player.centerY += 1

def onStep():
    movePlayer()

cmu_graphics.run()