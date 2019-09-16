import pygame
import Proyectil

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self,ancho,largo):
        pygame.sprite.Sprite.__init__(self)
        # self.ImageNave = pygame.image.load('Images/paltita.png')
        self.ImageNave = pygame.Surface((50,50)).convert()
        # rect1 = pygame.Rect(pos_x,pos_y,20,50)
        self.ImageNave.fill((45,255,60))
        self.rect = self.ImageNave.get_rect()
        # self.pos_x = self.rect.x
        # self.pos_y = self.rect.y
        self.rect.centerx = ancho / 2
        self.rect.centery = largo - 50
        self.listaDisparo = []
        self.vida = True
        self.vidaCantidad = 100
        self.velocidad = 10

    def movimientoDerecha(self,ancho,largo):
        self.rect.right += self.velocidad
        self.__movimiento(ancho,largo)
    
    def movimientoIzquierda(self,ancho,largo):
        self.rect.left -= self.velocidad
        self.__movimiento(ancho,largo)
    
    def movimientoArriba(self,ancho,largo):
        self.rect.top -= self.velocidad
        self.__movimiento(ancho,largo)
    
    def movimientoAbajo(self,ancho,largo):
        self.rect.bottom += self.velocidad
        self.__movimiento(ancho,largo)

    def __movimiento(self,ancho,largo):
        if self.vida:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= ancho:
                self.rect.right = 900  
            elif self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= largo:
                self.rect.bottom = 800  

    def disparar(self,x,y):
        miProyectil = Proyectil.Proyectil(x,y,True)
        self.listaDisparo.append(miProyectil)
        # print "disparo"

    def dibujar(self, superficie,Fuente):
        superficie.blit(self.ImageNave, self.rect)
        contador = Fuente.render(str(self.vidaCantidad),0,(255,255,255))
        superficie.blit(contador,(self.rect.x + self.rect.width,self.rect.y+20))
