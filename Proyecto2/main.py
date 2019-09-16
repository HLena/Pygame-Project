import pygame, sys
from pygame.locals import *
from random import randint
import math
from Clases import Nave, Proyectil,Enemigo


ancho = 1000
largo = 800
listaEnemigo = []


def colisionMultple(obj1,balas):
    for b in balas:
        if colisionRect(obj1,b):
            obj1.actualizarVida()
            balas.remove(b)
            # if enemigo.vida == False:
            #     listaEnemigo.remove(enemigo)


def colisionRect(obj1, obj2):
    if (obj1.rect.left < obj2.rect.left + obj2.rect.width and 
        obj1.rect.left + obj1.rect.width > obj2.rect.left and
        obj1.rect.top < obj2.rect.top + obj2.rect.height and
        obj1.rect.height + obj1.rect.top > obj2.rect.top):
        return True
    else:
        False

def colisionCircle(obj1, obj2):
    d = math.sqrt(abs(obj1.x - obj2.x)**2 + abs(obj1.y - obj2.y)**2)
    if obj1.r + obj2.r > d:
        return True
    else :
        return False

def detenerTodo():
    for ene in listaEnemigo:
        for disparo in ene.listaDisparo:
            ene.listaDisparo.remove(disparo)
        ene.conquista = True

def CargarEnemigos(num):
    for i in range(num):
        tmpx , tmpy = randint(0,200), randint(0,1000)
        enemigo = Enemigo.Invasor(tmpx,tmpy)
        listaEnemigo.append(enemigo)



def SpaceInvader():
    pygame.init()
    screen = pygame.display.set_mode((1000,800))
    pygame.display.set_caption("Juego Espacial")

    jugador = Nave.NaveEspacial(ancho,largo)
    # enemigo = Invasor(100,100)
    CargarEnemigos(1)#parametro indica el numero de enemigos
    # proyec = Proyectil(ancho/2,largo-50)
    enJuego = True
    clock = pygame.time.Clock()
    fps = 60
    pygame.key.set_repeat(1,1000/fps)

    #------definiendo colores---------------
    red = (255,0,0)
    #-------definiendo Figures--------------
    # smallrect = pygame.Surface((100,30)).fill(red)
    smallrect = pygame.Surface((100,30))
    bigrect = pygame.Surface((200,30))
    
    smallrect.fill(red)
    bigrect.fill(red)
    #-----------------texto-----------------
    Fuente = pygame.font.SysFont("Arial",20)
    texto = Fuente.render("Fin del Juego",0,(120,100,40))

    # pygame.display.flip()
    while True:
        clock.tick(fps)
        # jugador.movimiento()
        # proyec.trayectoria()
        # reloj.tick(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if enJuego == True:
                if event.type == pygame.KEYDOWN:
                    if event.key  == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_LEFT:
                        jugador.movimientoIzquierda(ancho,largo)
                    elif event.key == K_RIGHT:
                        jugador.movimientoDerecha(ancho,largo)
                    elif event.key == K_UP:
                        jugador.movimientoArriba(ancho,largo)
                    elif event.key == K_DOWN:
                        jugador.movimientoAbajo(ancho,largo)
                    elif event.key == K_SPACE:
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)

        #--------------creando obstaculos---------------
        screen.fill((0,0,0))
        screen.blit(smallrect,(0,200))
        screen.blit(smallrect,(400,400))
        screen.blit(bigrect,(ancho-bigrect.get_width(),200))
        screen.blit(smallrect,(ancho-smallrect.get_width(),500))
        screen.blit(bigrect,(0,500))
        # screen.blit(bigrect,(500,500))
        # print ancho - bigrect.get_width()
        # screen.fill(smallrect)
        # enemigo.comportamiento(jugador)
        jugador.dibujar(screen,Fuente)
        # enemigo.dibujar(screen,Fuente)
        # enemigo.distancia = enemigo.get_distancia(jugador)
        # proyec.dibuajar(screen)
        if len(jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujar(screen)
                x.trayectoria()
                if x.rect.top < 0:
                    jugador.listaDisparo.remove(x)
        
        if len(listaEnemigo)>0:
            for enemigo in listaEnemigo:
                enemigo.comportamiento(jugador)
                enemigo.dibujar(screen,Fuente)
                # if colisionRect(enemigo,jugador):
                    # enemigo.actualizarVida()
                colisionMultple(enemigo,jugador.listaDisparo)
                if enemigo.vida == False:
                    listaEnemigo.remove(enemigo)

                if len(enemigo.listaDisparo) > 0:
                    for x in enemigo.listaDisparo:
                        x.dibujar(screen)
                        x.trayectoria()
                        if x.rect.top > 800:
                            enemigo.listaDisparo.remove(x)
        
        if enJuego == False:
            screen.blit(texto,(300,300))

        pygame.display.update()

SpaceInvader()