import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,posx,posy, obj):
        pygame.sprite.Sprite.__init__(self)
        self.ImgBullet = pygame.Surface((10,10)).convert()
        self.ImgBullet.fill((255,255,255))
        self.rect = self.ImgBullet.get_rect()
        self.speedShoot = 3
        self.rect.top = posy
        self.rect.left = posx
        self.typeObj = obj

    def trayectory(self):
        if self.typeObj == True:
            self.rect.top = self.rect.top - self.speedShoot
        else:
            self.rect.top = self.rect.top + self.speedShoot

    
    def drawing(self, superf):
        superf.blit(self.ImgBullet,self.rect)
