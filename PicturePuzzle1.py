#짱구 그림 퍼즐 v1  (PicturPuzzle by ahnjh05141)

from bangtal import *
import random

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

music = Sound('intro.mp3')
Sound.play(music)

Main = Scene('짱구 그림 퍼즐 v1','images/메인.png')
Lobby = Scene('짱구 그림 퍼즐 v1','images/배경.png')
inGame1 = Scene('퍼즐1','images/배경.png')

shuffles = 300
tile = 176
x = [368, 544, 720, 368, 544, 720, 368, 544, 720]
y = [468, 468, 468, 294, 294, 294, 118, 118, 118]

orig = Object('images/짱구원본.png')
p1 = Object('images/짱구1.png')
p2 = Object('images/짱구2.png')
p3 = Object('images/짱구3.png')
p4 = Object('images/짱구4.png')
p5 = Object('images/짱구5.png')
p6 = Object('images/짱구6.png')
p7 = Object('images/짱구7.png')
p8 = Object('images/짱구8.png')
p9 = Object('images/빈칸.png')

def picLocate():
    p1.locate(inGame1, x[0], y[0])
    p2.locate(inGame1, x[1], y[1])
    p3.locate(inGame1, x[2], y[2])
    p4.locate(inGame1, x[3], y[3])
    p5.locate(inGame1, x[4], y[4])
    p6.locate(inGame1, x[5], y[5])
    p7.locate(inGame1, x[6], y[6])
    p8.locate(inGame1, x[7], y[7])
    p9.locate(inGame1, x[8], y[8])
    orig.locate(inGame1, 368, 118)
picLocate()
orig.show()

def changeXY(i):
    i-=1
    if (x[8]==x[i]):
        if (-tile <= y[8]-y[i] <= tile):
            y[i],y[8] = y[8],y[i]
    elif (y[8]==y[i]):
        if (-tile <= x[8]-x[i] <= tile):
            x[i],x[8] = x[8],x[i]

def p1_onMouseAction(x,y,action):
    changeXY(1)
    picLocate()
p1.onMouseAction = p1_onMouseAction
def p2_onMouseAction(x,y,action):
    changeXY(2)
    picLocate()
p2.onMouseAction = p2_onMouseAction
def p3_onMouseAction(x,y,action):
    changeXY(3)
    picLocate()
p3.onMouseAction = p3_onMouseAction
def p4_onMouseAction(x,y,action):
    changeXY(4)
    picLocate()
p4.onMouseAction = p4_onMouseAction
def p5_onMouseAction(x,y,action):
    changeXY(5)
    picLocate()
p5.onMouseAction = p5_onMouseAction
def p6_onMouseAction(x,y,action):
    changeXY(6)
    picLocate()
p6.onMouseAction = p6_onMouseAction
def p7_onMouseAction(x,y,action):
    changeXY(7)
    picLocate()
p7.onMouseAction = p7_onMouseAction
def p8_onMouseAction(x,y,action):
    changeXY(8)
    picLocate()
p8.onMouseAction = p8_onMouseAction

startBut = Object('images/게임시작.png')
startBut.locate(Main, 720-210, 100)
startBut.show()
def startBut_onMouseAction(x,y,action):
    inGame1.enter()
startBut.onMouseAction = startBut_onMouseAction

shuffleBut = Object('images/셔플.png')
shuffleBut.locate(inGame1, 720-210, 20)
shuffleBut.show()
shuffleBut.setScale(0.8)
def shuffleBut_onMouseAction(x,y,action):
    orig.hide()
    p1.show()
    p2.show()
    p3.show()
    p4.show()
    p5.show()
    p6.show()
    p7.show()
    p8.show()
    p9.show()
    for i in range(shuffles):
        num = random.randint(1,9)
        changeXY(num)
        picLocate()
shuffleBut.onMouseAction = shuffleBut_onMouseAction

#===start===
startGame(Main)
