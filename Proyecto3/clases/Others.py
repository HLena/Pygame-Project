import pygame, sys
from pygame.locals import *
import math
from random import randint

class Circle():
    def __init__(self,cx,cy,r):
        self.radius = r
        self.centerx = cx
        self.centery = cy

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.ImgObj= pygame.Surface((w,h))
        self.ImgObj.fill((0,255,0))
        self.rect = self.ImgObj.get_rect()
        self.rect.x,self.rect.y = x,y

    def drawing(self,superf):
        superf.blit(self.ImgObj,self.rect)   

class Polygon(pygame.sprite.Sprite):
    def __init__(self,sc,color,lista):
        pygame.sprite.Sprite.__init__(self)
        self.vertices = lista
        pygame.draw.polygon(sc,color,lista)

    def polyRect(self,rx,ry,rw,rh):
        next = 0
        for current in range(len(self.vertices)):
            next = current + 1
            if next == len(self.vertices):
                next = 0
            vc = self.vertices[current]
            vn = self.vertices[next]
            collion, m = self.lineRect(vc[0],vc[1],vn[0],vn[1],rx,ry,rw,rh)
            if collion:
                return True
            inside = self.PolygonPoint(rx,ry)
            if inside: 
                return True
        return False
    
    def lineRect(self,x1,y1,x2,y2,rx,ry,rw,rh):
        left = self.lineLine(x1,y1,x2,y2,rx,ry,rx,ry+rh)
        right = self.lineLine(x1,y1,x2,y2,rx+rw,ry,rx+rw,ry+rh)
        top = self.lineLine(x1,y1,x2,y2,rx,ry,rx+rw,ry)
        bottom = self.lineLine(x1,y1,x2,y2,rx,ry+rh,rx+rw,ry+rh)
        if left or top or right or bottom:
            m =  (y2-y1)/x2-x1
            return True , m
        return False , 0
    
    def lineLine(self,x1,y1,x2,y2,x3,y3,x4,y4):
        uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
        uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
        if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
            return True
        return False

    def PolygonPoint(self,px,py):
        # print "obj:",i
        # px, py = lista[i][0],lista[i][1]
        collision = False
        next = 0
        for current in range(0,len(self.vertices)):
            next = current + 1
            if next == len(self.vertices):
                next = 0
            vc = self.vertices[current]
            vn = self.vertices[next]
            if (((vc[1] >= py and vn[1]< py) or (vc[1] < py and vn[1]>=py)) and (px < (vn[0]-vc[0])*(py-vc[1]) /(vn[1]-vc[1])+vc[0])):
                collision = not collision
        return collision
           

        

class Piece(pygame.sprite.Sprite):     
    def __init__(self,x,y,color,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.inix,self.iniy=x,y
        self.width = w
        self.heigh = h
        self.ImgObj = pygame.Surface((self.width,self.heigh))
        self.ImgObj.fill(color)
        self.rect = self.ImgObj.get_rect()
        self.rect.x,self.rect.y = x,y
        self.seguir = False
        self.taken = False
        

    def __moviments(self,w_screen,h_screen,player):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= w_screen:
            self.rect.right = w_screen 
        elif self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= h_screen:
            self.rect.bottom =  h_screen
        else:
            self.rect.left = player.rect.centerx
            self.rect.top = player.rect.centery
    def GetPosPiece(self,player,screenW,screenH):
        # superf.blit(self.ImgObj,self.rect)
        if self.seguir:
            self.__moviments(screenW,screenH,player)
    
    def drawing(self,superf):
        superf.blit(self.ImgObj,self.rect)

    
    
    # def Collaide(self,obj1):
    #     for i in obj1.listSubObj:

    


        
