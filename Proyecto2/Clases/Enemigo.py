import pygame
import math
from random import randint
import Proyectil

class Invasor(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        # self.imageProyectil = pygame.image.load('Images/zombicito.png')
        self.imageEnemigo = pygame.Surface((30,30))
        # self.pygame.draw.circle(imageEnemigo,(100,150,255),(15,15),15)
        self.imageEnemigo.fill((100,150,255))
        self.rect = self.imageEnemigo.get_rect()
        self.listaDisparo = []
        self.velocidad = 1
        self.rect.top = posy
        self.rect.left = posx
        self.rangoDisparo = 5
        self.vidaCantidad = 100
        self.vida = True

        # self.derecha = True
        # self.contador = 0
        # self.Maxdescenso = self.rect.top + 40
        self.conquista = False

        self.distancia = 0
        # self.cambio = True
        # self.ale_x,self.ale_y = randint(0,ancho),randint(0,largo)
        
        # self.limiteDerecha = posx + dist
        # self.limiteIzquierda = posx - dist

    def dibujar(self, superficie,Fuente):
        if self.vida == True:
            superficie.blit(self.imageEnemigo,self.rect)
            contador = Fuente.render(str(self.vidaCantidad),0,(255,255,255))
            superficie.blit(contador,(self.rect.x + self.rect.width,self.rect.y+20))
        # pygame.draw.circle(superficie,(255,34,12),(self.ale_x,self.ale_y),2)

    def __get_distancia(self,x,y):
        # print x,y
        return math.sqrt(pow(self.rect.x-x,2) + pow(self.rect.y-y,2))

    def __movimiento(self,posx,posy):
        self.distancia = self.__get_distancia(posx,posy)
        if self.distancia > 0:
            # print self.distancia
            # if self.cambio:
            #     self.ale_x = randint(0,ancho)
            #     self.ale_y = randint(0,largo)
            #     self.cambio = False
            # else:
            direc_x = posx - self.rect.x
            direc_y = posy - self.rect.y
            # print("obj:",posx,posy)
            # print("act:",self.rect.x,self.rect.y)
            if abs(direc_x) > abs(direc_y):
                self.__movimientoHorizontal(direc_x)
            else: 
                self.__movimientoVertical(direc_y)

            # tmp = randint(0,1)
            # if tmp:
            #     self.__movimientoHorizontal()
            # else: 
            #     self.__movimientoVertical()
        else:
            pass
            # print("hallado")
            # while True:
            #     self.ale_x = randint(0,ancho)
            #     self.ale_y = randint(0,largo)
            #     if(self.__get_distancia(self.ale_x,self.ale_y) < self.distancia):
            #         break
            # if self.ale_x == self.rect.x and self.ale_y == self.rect.y :
            #     self.cambio = True

            
        # if self.contador < 3:
        #     self.__movimientoLateral()
        # else:
        #     self.__descenso()
    
    def __movimientoVertical(self,direc_y):
        if direc_y < 0:
            self.rect.top = self.rect.top - self.velocidad
        else:
            self.rect.bottom = self.rect.bottom + self.velocidad
        # if self.Maxdescenso == self.rect.top:
        #     self.contador = 0
        #     self.Maxdescenso = self.rect.top + 40
        # else:
        #     self.rect.top += 1

    def __movimientoHorizontal(self,direc_x):
        if direc_x < 0:
            self.rect.left = self.rect.left - self.velocidad
        else:
            self.rect.right = self.rect.right + self.velocidad

        # if self.derecha == True:
        #     self.rect.left = self.rect.left + self.velocidad
        #     if self.rect.left > 500:
        #         self.derecha = False
        #         self.contador +=1
        # else:
        #     self.rect.left = self.rect.left - self.velocidad
        #     if self.rect.left<0:
        #         self.derecha = True


    def __ataque(self):
        if randint(0,100) < self.rangoDisparo:
            self.__disparo()
    
    def __disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil.Proyectil(x,y,False)
        self.listaDisparo.append(miProyectil)
    
    def actualizarVida(self):
        self.vidaCantidad -= 10
        if self.vidaCantidad <= 0:
            self.vida = False

    def comportamiento(self,obj):
        # self.distancia = self.__get_distancia(obj.rect.x,obj.rect.y)
        if self.conquista == False:
            self.__movimiento(obj.rect.x,obj.rect.y)
            self.__ataque()
 