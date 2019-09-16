import pygame, sys
from pygame.locals import *
from random import randint
from clases import ClassEnemy,ClassPlayer,Others
import math

screenW, screenH = 1500, 800

# ----------define Colors------------
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (100,100,100)
blue = (0,0,255)
yellow = (255,255,0)

colors = [white,red,green,blue]

def collideOneToOne(obj1, obj2):
    if obj1.rect.bottom >= obj2.rect.top and obj1.rect.top < obj2.rect.top  :
        # obj1.rect.stop()
        obj1.rect.bottom = obj2.rect.top
        # print obj1.rect.bottom,obj1.rect.centery
    elif obj1.rect.top <= obj2.rect.bottom and obj1.rect.bottom > obj2.rect.bottom:
        obj1.rect.top = obj2.rect.bottom
        # print "arriba"
    elif obj1.rect.right >= obj2.rect.left and obj1.rect.left < obj2.rect.left :
        obj1.rect.right = obj2.rect.left
        # print "->"
    elif obj1.rect.left <= obj2.rect.right and obj1.rect.right > obj2.rect.left:
        obj1.rect.left = obj2.rect.right
        # print "<-"
    else:
        pass

def collisionObjects(obj1,objects):
    # print "len: ",len(objects)
    for obj2 in objects:
        if obj1 != obj2:
            if collisionRect(obj1,obj2):          
                collideOneToOne(obj1,obj2)
        else: 
            print "No colosion objects"


def collisionMult(obj1,bullets,ps):
    for b in bullets:
        if collisionRect(obj1,b):
            if ps == False:
                obj1.updateLife()
            bullets.remove(b)
        

def collisionRect(obj1, obj2):
    # print obj1.rect, obj2.rect
    if (obj1.rect.left < obj2.rect.left + obj2.rect.width and 
        obj1.rect.left + obj1.rect.width > obj2.rect.left and
        obj1.rect.top < obj2.rect.top + obj2.rect.height and
        obj1.rect.height + obj1.rect.top > obj2.rect.top):
        # print "collision"
        return True
    else:
        # print "no collision"
        return False

def collisionCircle(obj1, obj2):
    d = math.sqrt(abs(obj1.x - obj2.x)**2 + abs(obj1.y - obj2.y)**2)
    if obj1.r + obj2.r > d:
        return True
    else :
        return False


def CreateEnemies(num,c):
    l = []
    for i in range(num):
        tmpx , tmpy = randint(0,1500), randint(100,screenH/2)
        # sp = randint(1,3)
        # if tmpx == 0:
        #     ene = ClassEnemy.Enemy(0,tmpy,15,sp)
        # else:
        #     ene = ClassEnemy.Enemy(screenW,tmpy,15,sp)
        ene = ClassEnemy.Enemy((tmpx,tmpy))
        ene.start(randint(1,2),randint(1,2))
        c.add(ene)
        l.append(ene)
    return l

def CreatePieces():
    posPieces = [200,400,600,800]
    l = []
    for i in range(len(posPieces)):
        p = Others.Piece(posPieces[i],20,colors[i],40,40)
        # print p.rect.centerx,p.rect.centery
        l.append(p)
    return l

def Distance2Points(p1,p2):
    return math.sqrt(pow(p1.rect.centerx-p2.rect.centerx,2) + pow(p1.rect.centery-p2.rect.centery,2))



def GetPiece(player,p1):
    d = Distance2Points(player,p1)
    if player.rect.top <= p1.rect.bottom and ((player.rect.right > p1.rect.left and player.rect.left < p1.rect.right) or (player.rect.left < p1.rect.right and player.rect.right > p1.rect.left)) and d <= player.radius+p1.rect.height/2:
        return True
    else:
        return False



def PlayGame():
    pygame.init()
    screen = pygame.display.set_mode((screenW,screenH),0,32)
    pygame.display.set_caption("Juego 3")
    OnPlay = True
    clock = pygame.time.Clock()
    fps = 30
    pygame.key.set_repeat(1,500/fps)
    player = ClassPlayer.Player(screenW,screenH,20)
    # print "player: ",player.rect
    listObstacles = []
    # listObstacles.append(Others.Obstacle(0,500,150,20))
    # listObstacles.append(Others.Obstacle(0,300,150,20))
    # listObstacles.append(Others.Obstacle(screenW - 150,200,150,20))
    # listObstacles.append(Others.Obstacle(screenW - 150,500,150,20))
    # listObstacles.append(Others.Polygon(screen,yellow,[(200,300),(210,600),(500,345),(567,234),(520,400)]))

    enemies = pygame.sprite.Group()
    listEnemies = CreateEnemies(5,enemies)
    listPieces = CreatePieces()

    font = pygame.font.SysFont("Arial",20)
    listPiecesPuzzle = []
    
    puzzle = Others.Piece(screenW-200,screenH-100,(100,100,100),200,100)    
    # print puzzle.rect
    while True:
        #Pintando pantalla de color negro
        screen.fill(black)
        #creando obstaculos parael juego
        listObstacles.append(Others.Polygon(screen,yellow,[(500,400),(510,500),(600,450),(867,334),(600,300)]))
        listObstacles.append(Others.Polygon(screen,yellow,[(0,0),(30,50),(30,400),(65,510),(55,750),(0,800)]))
        listObstacles.append(Others.Polygon(screen,yellow,[(1500,0),(1500,800),(1450,745),(1450,300),(1400,200),(1430,0)]))
        # puzzle.drawing(screen)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if OnPlay == True:
                if event.type == pygame.KEYDOWN:
                    if event.key  == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_LEFT:
                        player.movimentLeft(screenW,screenH)
                    elif event.key == K_RIGHT:
                        player.movimentRight(screenW,screenH)
                    elif event.key == K_UP:
                        player.movimentUp(screenW,screenH)
                    elif event.key == K_DOWN:
                        player.movimentDown(screenW,screenH)
                    elif event.key == K_SPACE:
                        x,y = player.rect.center
                        player.shoot(x,y)
        #-------------------Piezas------------------
        for obj in listPieces:
            if pygame.sprite.spritecollideany(obj,enemies):
                obj.seguir = False
                obj.rect.left,obj.rect.top = obj.inix,obj.iniy
            elif collisionRect(player,puzzle) == False:
                if GetPiece(player,obj) == True:
                    obj.seguir = True
            else:
                listPiecesPuzzle.append(obj)     
                if event.type == pygame.KEYDOWN:
                    if event.key  == K_s:
                        obj.seguir = False   
            # print "puzzlelist:",len(puzzle.listSubObj)
            collisionObjects(obj,listPiecesPuzzle)
            # obj.GetPosPiece(player,screenW,screenH)
            obj.drawing(screen)

        
        player.drawing(screen,font)
        
        # collisionObjects(player,listObstacles)
        # for obs in listObstacles:
        #     # print obj.lis
        #     for ene in listEnemies:
        if listObstacles[0].polyRect(player.rect.left,player.rect.top,player.rect.width,player.rect.height):
            print "hay colision"
        else:
            print "no hay colision"

        # for obj in listObstacles:
        #     obj.drawing(screen)
            #collisionMult(obj,player.listShoots,True)
        
    
        if len(player.listShoots) > 0:
            for x in player.listShoots:
                x.drawing(screen)
                x.trayectory()
                if x.rect.top < 0:
                    player.listShoots.remove(x)
                # collisionMult(x,listObstacles,True)

        if len(listEnemies) > 0:
            for enemigo in listEnemies:
                # enemigo.comportamiento(player)
                enemigo.drawing(screen,font)
                enemigo.update(screenW,screenH)
                # enemigo.behavior(player)
                # collisionObjects(enemigo,listObstacles)
                # collisionMult(enemigo,player.listShoots,False)
                # if collisionRect(enemigo,player):
                #     player.updateLife()
                # if enemigo.state == False:
                #     listEnemies.remove(enemigo)
        else:
            listEnemies = CreateEnemies(5,enemies)

        pygame.display.update()

PlayGame()