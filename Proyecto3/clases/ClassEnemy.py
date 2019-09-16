import pygame
import math
from random import randint

class Enemy(pygame.sprite.Sprite):
    # def __init__(self,posx,posy,r,sp):
    def __init__(self,pos=(0,0)):
        pygame.sprite.Sprite.__init__(self)
        # self.ImgEnemy = pygame.Surface((r*2,r*2),pygame.SRCALPHA)
        # pygame.draw.circle(self.ImgEnemy,(255,0,255),(r,r),r)
        self.ImgEnemy = pygame.Surface((10,10)).convert()
        self.ImgEnemy.fill((255,255,255))

        
        # self.rect = self.ImgEnemy.get_rect()
        self.rect = self.ImgEnemy.get_rect(center=pos)
        # self.speed = sp
        self.speed_x = 0
        self.speed_y = 0
        # self.rect.top = posy
        # self.rect.left = posx
        self.lifeCant = 100
        self.state = True

        self.derecha = True
        self.contador = 0
        self.Maxdescenso = self.rect.top + 40
        self.conquest = False


    def drawing(self, superf,font):
        if self.state == True:
            superf.blit(self.ImgEnemy,self.rect)
            counter = font.render(str(self.lifeCant),0,(255,255,255))
            superf.blit(counter,(self.rect.x + 10,self.rect.bottom))
        # pygame.draw.circle(superficie,(255,34,12),(self.ale_x,self.ale_y),2)

    # def __get_distance(self,x,y):
    #     # print x,y
    #     return math.sqrt(pow(self.rect.x-x,2) + pow(self.rect.y-y,2))

    # def __moviments(self):
    #     if self.contador < 3:
    #         self.__movimentsLateral()
    #     else:
    #         self.__descenso()
    
    # def __descenso(self):
    #     if self.Maxdescenso==self.rect.top:
    #         self.contador = 0
    #         self.Maxdescenso = self.rect.top + 40
    #     else:
    #         self.rect.top += 1
    
    
    # def __movimentsLateral(self):
    #     if self.derecha == True:
    #         self.rect.left = self.rect.left + self.speed
    #         if self.rect.left > 1000:
    #             self.derecha = False
    #             self.contador +=1
    #     else:
    #         self.rect.left = self.rect.left - self.speed
    #         if self.rect.left < 0:
    #             self.derecha = True
    def updateLife(self):
        self.lifeCant -= 10
        if self.lifeCant <= 0:
            self.state = False

    def behavior(self,obj):
        self.__moviments()

    def update(self,screen_w, screen_h):
        self.rect.move_ip(self.speed_x, self.speed_y)
        if self.rect.bottom >= screen_h or self.rect.top <= 0:
            self.__changeY()
        elif self.rect.left <= 0 or self.rect.right >= screen_w:
            self.__changeX()
    def __changeY(self):
        self.speed_y *= -1

    def __changeX(self):
        self.speed_x *= -1

    def start(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def stop(self):
        self.speed_x = 0
        self.speed_y = 0


            
    
