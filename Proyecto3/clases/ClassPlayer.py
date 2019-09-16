import pygame
import pygame.gfxdraw
import math
from random import randint
from Others import Circle
import ClassBullet


class Player(pygame.sprite.Sprite):
    def __init__(self,w_screen,h_screen,r):
        pygame.sprite.Sprite.__init__(self)
        # c1 = Circle.__init__(self, width/2,heigh-50,15)
        self.radius = r
        self.ImgPlayer = pygame.Surface((r*2,r*2))
        # self.ImgPlayer = pygame.Surface((r*2,r*2),pygame.SRCALPHA)
        # pygame.draw.circle( self.ImgPlayer,(100,150,255),(r,r),20)
        self.ImgPlayer.fill((100,150,255))
        # pygame.gfxdraw.aacircle(self.ImgPlayer, 15, 15, 14, (0, 255, 0))
        # pygame.gfxdraw.filled_circle(self.ImgPlayer, 15, 15, 14, (0, 255, 0))
        
        self.rect = self.ImgPlayer.get_rect()
        self.rect.centerx = w_screen / 2
        self.rect.centery = h_screen-50
        self.listShoots = []
        self.listPoints = [(self.rect.left,self.rect.top),(self.rect.right,self.rect.top),(self.rect.right,self.rect.bottom),(self.rect.left,self.rect.bottom)]
        self.speedx = 5
        self.speedy = 5
        self.lifeCant = 100
        self.state = True
        # self.listPiece = []

    def drawing(self, superf,font):
        # print self.rect,self.rect.centerx,self.rect.centery
        if self.state == True:
            superf.blit(self.ImgPlayer,self.rect)
            counter = font.render(str(self.lifeCant),0,(255,255,255))
            superf.blit(counter,(self.rect.x + 10,self.rect.bottom))
    
    # def stop(self):
    #     self.speedx = 0
    #     self.speedy = 0

    # def start(self):
    #     self.speedx = 5
    #     self.speedy = 5
    
    def __moviments(self,w_screen,h_screen):
        if self.state:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= w_screen:
                self.rect.right = w_screen 
            elif self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= h_screen:
                self.rect.bottom =  h_screen

    def movimentRight(self,ancho,largo):
        self.rect.right += self.speedx
        self.__moviments(ancho,largo)
    
    def movimentLeft(self,ancho,largo):
        self.rect.left -= self.speedx
        self.__moviments(ancho,largo)
    
    def movimentUp(self,ancho,largo):
        self.rect.top -= self.speedy
        self.__moviments(ancho,largo)
    
    def movimentDown(self,ancho,largo):
        self.rect.bottom += self.speedy
        self.__moviments(ancho,largo)
    
    def shoot(self,x,y):
        myBullet = ClassBullet.Bullet(x,y,True)
        self.listShoots.append(myBullet)
        print len(self.listShoots)
        # print "disparo"

    def updateLife(self):
        self.lifeCant -= 1
        if self.lifeCant <= 0:
            self.state = False
