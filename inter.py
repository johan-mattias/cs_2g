 # Fill me in!
 #shapes
from cmu_graphics import *

app.background= 'Grey'
app.stepsPerSecond = 20
Timer = Label(90, 200, 30, fill='black', size=20)
app.steps = 0
app.start = False
app.Bouncetimer = 0
app.Reversetimer1 = 0
app.Reversetimer2 = 0
Bouncelabel = Label("WE BOUNCING IN HERE!",200,50,size=25,fill="white",visible=False)
#Gungnir = Sound('https://audio.jukehost.co.uk/4vwkHR4Spc8EWdXemVpVMPcpDmzBmWpX')
bruh = Label(0,150,50)
bruh2 = Label(0, 250,50)
#Cannon
Cannon1 = Group(
            Rect(10, 10, 30, 30, fill='black'),
            Rect(18, -5, 15, 14, fill='darkGrey')
                )

Cannon1.rotateAngle=130

Cannon2 = Group(
            Rect(365, 10, 30, 30, fill='black'),
            Rect(373, -5, 15, 14, fill='darkGrey')
                )
Cannon2.rotateAngle= -130     

Cannon3 = Group(
            Rect(10, 360, 30, 30, fill='black'),
            Rect(18, 345, 15, 14, fill='darkGrey')
                )
Cannon3.rotateAngle=50    

Cannon4 = Group(
            Rect(365, 360, 30, 30, fill='black'),
            Rect(373, 345, 15, 14, fill='darkGrey')
                )
Cannon4.rotateAngle=-50
Bullets = Group()
                
#Stars for buffs
Star1 = Star(0,0,25,45,fill='lightgreen',visible = False, opacity = 30)
Star2 = Star(0,0,25,45,fill='lightgreen',visible = False,opacity = 30)
Star3 = Star(0,0,28,30,fill="powderblue",visible = False, opacity = 60)
Star4 = Star(0,0,28,30,fill="powderblue",visible = False, opacity = 60)
stars = Group(Star1,Star2, Star3, Star4)

#Players
player1 = Group(
Oval(200,200,30,20, fill=rgb(77, 220, 234)),
Oval(200,195,25,20, fill=rgb(77, 240, 234)),

Polygon(190,203,188,212,189,222,190,214,191,212,192,207, fill=rgb(77, 220, 234)),
Polygon(200,206,198,211,202,217,202,222,204,219,203,215,201,211,203,207, fill=rgb(77, 220, 234)),
Polygon(211,203,213,207,214,211,215,216,217,222,214,219,212,212,209,207, fill=rgb(77, 220, 234)),
)
player1.centerX = 180
player1.dx = 0
player1.dy = 0
player1.ax = 1
player1.ay = 1

player2 = Group(
Oval(200,200,30,20, fill=rgb(214, 6, 72)),
Oval(200,195,25,20, fill=rgb(250, 2, 81)),

Polygon(190,203,188,212,189,222,190,214,191,212,192,207, fill=rgb(214, 6, 72)),
Polygon(200,206,198,211,202,217,202,222,204,219,203,215,201,211,203,207, fill=rgb(214, 6, 72)),
Polygon(211,203,213,207,214,211,215,216,217,222,214,219,212,212,209,207, fill=rgb(214, 6, 72)),
)
player2.centerX = 220
player2.dx = 0
player2.dy = 0
player2.ax = 1
player2.ay = 1
players = Group(player1, player2)
#score
for player in players:
    player.freeze = 0
scorep1 = Label(0,125,30, size= 20,fill="black")
scorep2 = Label(0,275,30, size= 20,fill="black")
#Freezetimers

# mynt
mynttot = Label(0,450,150,size = 20, fill="white")

mynt = Group(
    )

myntspawn = Label(0,450,200,size = 20,fill="white")

#powerUps
powerupsS = Group(
    )
powerupsD = Group(
    )
powerupsF = Group(
    )
PO = Label(0,450,450,size = 20,fill="white")
#def bulletsShoot(bulletX,bulletY,RandomPlayer)
#immunity
winbox = Group()
cont = Label("Press [space] for Menu", 200, 250, size=20)
winbox.add(cont)
winbox.visible = False
p1imtim = Label(0,450,200,size=20,fill=None)
p2imtim = Label(0,450,200,size=20,fill=None)
#winnerScreen
def winnerbox(color,bo,sco,wins):
    winbox.add(
    Circle(100,200,70,fill=color,border=bo,borderWidth=3),
    Circle(300,200,70,fill=color,border=bo,borderWidth=3),
    Rect(100,130,200,140,fill=color,border=bo,borderWidth=3),
    Line(103,133,103,267,fill=color,lineWidth=6),
    Line(297,133,297,267,fill=color,lineWidth=6),
    Label(wins + " wins with",200,180,fill="black",size=35,bold=True),
    Label(str(sco) + " points",200,215,fill="black",size=35,bold=True))
    cont.toFront()
def drawbox(color,bo):
    winbox.add(
    Circle(100,200,70,fill=color,border=bo,borderWidth=3),
    Circle(300,200,70,fill=color,border=bo,borderWidth=3),
    Rect(100,130,200,140,fill=color,border=bo,borderWidth=3),
    Line(103,133,103,267,fill=color,lineWidth=6),
    Line(297,133,297,267,fill=color,lineWidth=6),
    Label("DRAW",200,195,fill=rgb(250,2,81),size=45,bold=True))
    cont.toFront()
    
def CannonRotation():
    RandomCannon = randrange(1, 5)
    RandomPlayer = randrange(1, 3)
        
    if RandomCannon==1 and RandomPlayer==1:
        Cannon1.rotateAngle = angleTo(Cannon1.centerX, Cannon1.centerY, player1.centerX, player1.centerY)
        
    elif RandomCannon==1 and RandomPlayer==2:
        Cannon1.rotateAngle = angleTo(Cannon1.centerX, Cannon1.centerY, player2.centerX, player2.centerY)
        
    if RandomCannon==2 and RandomPlayer==1:
        Cannon2.rotateAngle = angleTo(Cannon2.centerX, Cannon2.centerY, player1.centerX, player1.centerY)
    elif RandomCannon==2 and RandomPlayer==2:
        Cannon2.rotateAngle = angleTo(Cannon2.centerX, Cannon2.centerY, player2.centerX, player2.centerY)
        
    if RandomCannon==3 and RandomPlayer==1:
        Cannon3.rotateAngle = angleTo(Cannon3.centerX, Cannon3.centerY, player1.centerX, player1.centerY)
    elif RandomCannon==3 and RandomPlayer==2:
        Cannon3.rotateAngle = angleTo(Cannon3.centerX, Cannon3.centerY, player2.centerX, player2.centerY)
        
    if RandomCannon==4 and RandomPlayer==1:
        Cannon4.rotateAngle = angleTo(Cannon4.centerX, Cannon4.centerY, player1.centerX, player1.centerY)
    elif RandomCannon==1 and RandomPlayer==2:
        Cannon4.rotateAngle = angleTo(Cannon4.centerX, Cannon4.centerY, player2.centerX, player2.centerY)
    x = 0
    y = 0
    if RandomCannon==1:
            x, y = getPointInDir(Cannon1.centerX,Cannon1.centerY, Cannon1.rotateAngle, 50)
            angle = Cannon1.rotateAngle
    if RandomCannon==2:
            x, y = getPointInDir(Cannon2.centerX,Cannon2.centerY, Cannon2.rotateAngle, 50)
            angle = Cannon2.rotateAngle
    if RandomCannon==3:
            x, y = getPointInDir(Cannon3.centerX,Cannon3.centerY, Cannon3.rotateAngle, 50)
            angle = Cannon3.rotateAngle
    if RandomCannon==4:
            x, y = getPointInDir(Cannon4.centerX,Cannon4.centerY, Cannon4.rotateAngle, 50)    
            angle = Cannon4.rotateAngle
    Bullet = Circle(x, y, 5, fill='black')
    Bullet.angle = angle
    
    Bullets.add(Bullet)

#'''
#'''
app.msped1 = 3
app.msped2 = 3
app.WallBounce = False
def onKeyHold(keys):
    if player1.top <= 0:
        if app.WallBounce == False:
            player1.top = 0
        else:
            player1.dy *= -1
            player1.dy += 15
    elif ('w' in keys):
        player1.dy-=app.msped1
    if player1.bottom >= 400:
        if app.WallBounce == False:
            player1.bottom = 400
        else:
            player1.dy *= -1
            player1.dy -= 15
    elif ('s' in keys):
        player1.dy+=app.msped1 
    if player1.left <= 0:
        if app.WallBounce == False:
            player1.left = 0
        else:
            player1.dx *= -1
            player1.dx += 15
    elif ('a' in keys):
        player1.dx-=app.msped1
    if player1.right >= 400:
        if app.WallBounce == False:
            player1.right = 400
        else:
            player1.dx *= -1
            player1.dx -= 15
    elif ('d' in keys):
        player1.dx+=app.msped1
    
    if player2.top <= 0:
        if app.WallBounce == False:
            player2.top = 0
        else:
            player2.dy *= -1
            player2.dy += 15
    elif ('up' in keys):
        player2.dy-=app.msped2
    if player2.bottom >= 400:
        if app.WallBounce == False:
            player2.bottom = 400
        else:
            player2.dy *= -1
            player2.dy -= 15
    elif ('down' in keys):
        player2.dy+=app.msped2 
    if player2.left <= 0:
        if app.WallBounce == False:
            player2.left = 0
        else:
            player2.dx *= -1
            player2.dx += 15
    elif ('left' in keys):
        player2.dx-=app.msped2
    if player2.right >= 400:
        if app.WallBounce == False:
            player2.right = 400
        else:
            player2.dx *= -1
            player2.dx -= 15
    elif ('right' in keys):
        player2.dx+=app.msped2
#'''
app.hiddentimer = 719

app.Win = False
def onKeyPress(keys):
    if "space" in keys and app.Win == True:
        Scene.value = "Menu"
        app.Win = False
        winbox.clear()
        app.hiddentimer = 719
        Bullets.clear()
        mynt.clear()
        powerupsS.clear()
        powerupsD.clear()
        powerupsF.clear()
        stars.visible = False
        scorep1.value = 0
        scorep2.value = 0
        player1.centerY = 200
        player2.centerY = 200
        player1.centerX = 180
        player2.centerX = 220
        player1.dx = 0
        player1.dy = 0
        player2.dx = 0
        player2.dy = 0

def onStep():
    #Player 1
    #dx
    if app.start == True:
        bruh.value = player1.freeze
        bruh2.value = player2.freeze
        app.steps += 1
        
        if app.hiddentimer > 0:
            app.hiddentimer -= 1
        Timer.value = app.hiddentimer//20
        for i in Bullets:
            x,y = getPointInDir(i.centerX, i.centerY, i.angle, 5)
            i.centerX = x
            i.centerY = y
            if i.centerY > 400 or i.centerY < 0:
                Bullets.remove(i)
            if i.centerX > 400 or i.centerY < 0:
                Bullets.remove(i)
        for player in players:
            
            if player.dx > 30 or player.dx < -30:
                player.ax = 3
            elif player.dx > 10 or player.dx < -10:
                player.ax = 2
            else:
                player.ax = 1
                
            if not(player.dx == 0):
                if player.dx < 0:
                    player.dx += player.ax
                if player.dx > 0:
                    player.dx -= player.ax
            #dy
            if player.dy > 30 or player.dy < -30:
                player.ay = 3
            elif player.dy > 10 or player.dy < -10:
                player.ay = 2
            else:
                player.ay = 1
            #decreasing acceleration
            if not(player.dy == 0):
                if player.dy < 0:
                    player.dy += player.ay
                if player.dy > 0:
                    player.dy -= player.ay
            #movement
            if player.freeze < 40:
                player.centerX += player.dx
                player.centerY += player.dy
            Star1.centerX = player1.centerX
            Star1.centerY = player1.centerY-4
            Star2.centerX = player2.centerX
            Star2.centerY = player2.centerY-4
            Star3.centerX = player1.centerX
            Star3.centerY = player1.centerY-4
            Star4.centerX = player2.centerX
            Star4.centerY = player2.centerY-4
            #Collision with wall
            if player.top <= 0:
                player.top = 0
            if player.bottom > 400:
                player.bottom = 400
            if player.left < 0:
                player.left = 0
            if player.right > 400:
                player.right = 400
            #collision with bullets
            player.freeze -= 1
            if player1.freeze < 0:
                if player1.hitsShape(Bullets) and (p1imtim.value < 1):
                    player1.freeze = 90
            if player2.freeze < 0:
                if player2.hitsShape(Bullets) and (p2imtim.value < 1):
                    player2.freeze = 90 
            elif player.freeze < 40 and player.freeze > 0:
                if app.hiddentimer%2 == 0:
                    player.opacity = 50
                else:
                    player.opacity = 100
            if player.freeze < 0:
                player.freeze = 0
                player.opacity = 100
            if player1.freeze > 40:
                Star3.visible = True
            else:
                Star3.visible = False
            if player2.freeze > 40:
                Star4.visible = True
            else:
                Star4.visible = False
        
                    
        #mynt
        myntspawn.value += 1
        if(mynttot.value <= 10):
            if myntspawn.value % 20 == 0:
                mynttot.value += 1
                for i in range(1,randrange(1,4)):
                    mynt.add(Circle(randrange(5,396),randrange(5,396),10,fill="gold"))
        for my in mynt.children:
            if my.hitsShape(player1):
                mynt.remove(my)
                scorep1.value += 1
                mynttot.value -= 1
            if my.hitsShape(player2):
                mynt.remove(my)
                scorep2.value += 1
                mynttot.value -= 1
        
            
        #powerUps
        powerup = randrange(1,300)
        #PO.value = powerup
        if powerup == 1:
            powerupsS.add(Circle(randrange(5,396),randrange(5,396),5,fill = "purple"))
        #if powerup == 2:
        #    powerupsD.add(Circle(randrange(5,396),randrange(5,396),5,fill = "red"))
        if powerup == 3:
            powerupsF.add(Circle(randrange(5,396),randrange(5,396),5,fill = "Green"))
        #Bouncy Wall
        for pow in powerupsS:
            if pow.hitsShape(player1):
                powerupsS.remove(pow)
                app.Bouncetimer = 5
            if pow.hitsShape(player2):
                powerupsS.remove(pow)
                app.Bouncetimer = 5
        #Immun powerup
        for pow in powerupsF:
            if pow.hitsShape(player1):
                powerupsF.remove(pow)
                p1imtim.value = 5
                player1.toFront()
                player2.toFront()
            if pow.hitsShape(player2):
                powerupsF.remove(pow)
                p2imtim.value = 5
                player1.toFront()
                player2.toFront()
        #Reverse kontroll för motståndare
        #for pow in powerupsD:
            #if pow.hitsShape(player1):
            #    powerupsD.remove(pow)
            #if pow.hitsShape(player2):
            #    powerupsD.remove(pow)
        if p1imtim.value>0:
            if myntspawn.value % 20 == 0:
                p1imtim.value-=1
            Star1.visible = True
            player1.toFront()
            player2.toFront()
        else:
            Star1.visible = False
        if p2imtim.value>0:
            if myntspawn.value % 20 == 0:
                p2imtim.value-=1
            Star2.visible = True
            player1.toFront()
            player2.toFront()
        else:
            Star2.visible = False
        #score/winner
        if Timer.value == 0:
            if scorep1.value == scorep2.value:
                drawbox(rgb(77,240,234),rgb(250,2,81))
            elif scorep1.value > scorep2.value:
                winnerbox(rgb(77,240,234),rgb(250,2,81),scorep1.value,"Blue")
            else:
                winnerbox(rgb(250,2,81),rgb(77,240,234),scorep2.value,"Red")
            winbox.visible = True
            app.start = False
            app.Win = True
        if app.Bouncetimer>0:
            if myntspawn.value % 20 == 0:
                app.Bouncetimer-=1
            app.WallBounce = True
            Bouncelabel.visible = True
        else:
            app.WallBounce = False
            Bouncelabel.visible = False
                
        
        if Diff.value == "Easy":
            if app.hiddentimer%20 == 0:
                CannonRotation()
        if Diff.value == "Medium":
            if app.hiddentimer%10 == 0:
                CannonRotation()
        if Diff.value == "Hard":
            if app.hiddentimer%5 == 0:
                CannonRotation()
    if Scene.value == "Menu":
        Menu.visible = True
        Information.visible = False
    elif Scene.value == "Info":
        Information.visible = True
        Menu.visible = False
    elif Scene.value == "Game":
        Information.visible = False
        Menu.visible = False
    
    
Timer.toFront()










#Meny och lite annat skit ligger här: Felix

#Hör börjar alla delar till menyn
Menu = Group(
Rect(0,0,400,400, fill=rgb(26,26,26)),
Label("InterGalactica",200,35, size=50, fill=rgb(77,240,234), border=rgb(250,2,81), bold=True),
)
StartSpel = Group(
    Circle(130,115,25, fill=rgb(77,240,234), border=rgb(250,2,81), borderWidth=3),
    Circle(270,115,25, fill=rgb(77,240,234), border=rgb(250,2,81), borderWidth=3),
    Rect(130,90,140,50, fill=rgb(77,240,234), border=rgb(250,2,81), borderWidth=3),
    Line(132,93,132,137, fill=rgb(77,240,234), lineWidth=5),
    Line(268,93,268,137, fill=rgb(77,240,234), lineWidth=5),
)
StartLabel = Label("Start Game",200,115, size=30, bold=True)
StartSpel.add(StartLabel)

Enkelt = Group(
    Circle(125, 285, 25, fill="lime")
    )
Enkelt.opacity = 100
Medel = Group(
    Circle(200, 285, 25, fill="yellow")
    )
Medel.opacity = 50
Svår = Group(
    Circle(275 , 285, 25, fill="red")
    )
Svår.opacity = 50

Svårigheter = Group(Enkelt,Medel,Svår)
Diff = Label("Easy", 1000, 1000)

SpelInfo = Group(
    Circle(130,115,25, fill=rgb(77,240,234), border=rgb(250,2,81), borderWidth=3),
    Circle(270,115,25, fill=rgb(77,240,234), border=rgb(250,2,81), borderWidth=3),
    Rect(130,90,140,50, fill=rgb(77,240,234), border=rgb(250,2,81), borderWidth=3),
    Line(132,93,132,137, fill=rgb(77,240,234), lineWidth=5),
    Line(268,93,268,137, fill=rgb(77,240,234), lineWidth=5),
    )
SpelInfo.centerY = 200
SpelInfoLabel = Label("Game Info",200,200, size=30, bold=True)
SpelInfo.add(SpelInfoLabel)

Menu.add(StartSpel, Svårigheter, SpelInfo)

Information = Group(
    Rect(0,0,400,400, fill=rgb(250,2,81)),
    Rect(5,5,390,390, fill=rgb(26,26,26) ,border=rgb(77,240,234), borderWidth=5),
    Label("Controls:", 200, 50, size=20, fill="white"),
    Label("The Blue Player is controlled WASD", 200, 70, size=15, fill="white"),
    Label("The Red Player is controlled with the Arrow Keys", 200, 90, size=15, fill="white"),
    
    Label("Cannon:", 200, 120, size=20, fill="white"),
    Label("The cannon will shot bullets at the player", 200, 140, size=15, fill="white"),
    Label("wich will Freeze the player if hit. Afterwards", 200, 160, size=15, fill="white"),
    Label("you will have a immuntiy period from the bullets", 200, 180, size=15, fill="white"),
    
    Label("Immunity PowerUp:", 200, 210, size=20, fill="white"),
    Label("Green blobs will randomly spawn on the map, the", 200, 230, size=15, fill="white"),
    Label("blobs will give you immunity to bullets for 5 seconds", 200, 250, size=15, fill="white"),
    
    Label("Trampoline:", 200, 280, size=20, fill="white"),
    Label("When one of the players collect a purple blob", 200, 300, size=15, fill="white"),
    Label("the walls will become Trampolines and the players", 200, 320, size=15, fill="white"),
    Label("will be able to bounce on them", 200, 340, size=15, fill="white"),
    )
    
    
InfoTbxBox = Group(
    Circle(320,360,20, fill=rgb(77,240,234), border=rgb(250,2,81), borderWidth=3),
    Circle(360,360,20, fill=rgb(77,240,234), border=rgb(250,2,81), borderWidth=3),
    Rect(320, 340, 40, 40, fill=rgb(77,240,234), border=rgb(250,2,81), borderWidth=3),
    Rect(320, 343, 40, 34, fill=rgb(77,240,234))
    )
InfoTbxLabel = Label("Back", 340,360, size=25, bold = True)
Information.add(InfoTbxBox,InfoTbxLabel)

Scene = Label("Menu", 1000, 1000)
#Här slutar alla delar till menyn

def onMouseMove(mouseX,mouseY):
    #Får texten att lysa upp när du har musen över knappen för respektive
    if StartSpel.hits(mouseX,mouseY):
        StartLabel.fill = "white"
    else:
        StartLabel.fill = "black"

    if SpelInfo.hits(mouseX,mouseY):
        SpelInfoLabel.fill = "white"
    else:
        SpelInfoLabel.fill = "black"
        
    if InfoTbxBox.hits(mouseX,mouseY):
        InfoTbxLabel.fill = "white"
    else:
        InfoTbxLabel.fill = "black"
        
    #Ändrar opacity på svårighets blobbarna om man har musen över    
    if Enkelt.hits(mouseX,mouseY) and Enkelt.opacity < 100:
        Enkelt.opacity = 75
    elif not Diff.value == "Easy":
        Enkelt.opacity = 50
    
    if Medel.hits(mouseX,mouseY) and Medel.opacity < 100:
        Medel.opacity = 75
    elif not Diff.value == "Medium":   
        Medel.opacity = 50
        
    if Svår.hits(mouseX,mouseY) and Svår.opacity < 100:
        Svår.opacity = 75
    elif not Diff.value == "Hard":
        Svår.opacity = 50
    
def onMousePress(mouseX,mouseY):
    #Ändrar Svårighet. Använd Diff.value == "(Svårgheten)" i koden
    if app.start == False:
        if StartSpel.hits(mouseX,mouseY):
            app.start = True
            Scene.value = "Game"
            #Gungnir.play(loop=True)
        
        if SpelInfo.hits(mouseX,mouseY):
            Scene.value = "Info"
        
        if InfoTbxBox.hits(mouseX,mouseY):
            Scene.value = "Menu"
            
        if Enkelt.hits(mouseX,mouseY):
            Diff.value = "Easy"
            Enkelt.opacity = 100
            Medel.opacity = 50
            Svår.opacity = 50
        if Medel.hits(mouseX,mouseY):
            Diff.value = "Medium"
            Medel.opacity = 100
            Svår.opacity = 50
            Enkelt.opacity = 50
        if Svår.hits(mouseX,mouseY):
            Diff.value = "Hard"
            Svår.opacity = 100
            Enkelt.opacity = 50
            Medel.opacity = 50


 
cmu_graphics.run()