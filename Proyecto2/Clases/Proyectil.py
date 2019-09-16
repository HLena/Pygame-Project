import pygame

class Proyectil(pygame.sprite.Sprite):
    def __init__(self,posx,posy, personaje):
        pygame.sprite.Sprite.__init__(self)
        self.imageProyectil = pygame.Surface((10,10)).convert()
        self.imageProyectil.fill((255,255,255))
        self.rect = self.imageProyectil.get_rect()
        self.velocidadDisparo = 3
        self.rect.top = posy
        self.rect.left = posx
        self.disparoPersonaje = personaje

    def trayectoria(self):
        if self.disparoPersonaje == True:
            self.rect.top = self.rect.top - self.velocidadDisparo
        else:
            self.rect.top = self.rect.top + self.velocidadDisparo

    
    def dibujar(self, superficie):
        superficie.blit(self.imageProyectil,self.rect)
