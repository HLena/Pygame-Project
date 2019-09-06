import pygame, sys
from pygame.locals import *
from random import randint


def colision_rect(obj1, obj2):
    if (obj1.x < obj2.x + obj2.width and 
        obj1.x + obj1.width > obj2.x and
        obj1.y < obj2.y + obj2.height and
        obj1.height + obj1.y > obj2.y):
        print("Hay colision!!!")
    else:
        print("No hay colision!!!")

# def colision_circule(obj1, obj2):
#     center_x = obj1.width/2
#     center_y = obj2.height/2
#     radio = 


#-------------------Plano en pygame--------------
#     |-------------------------------> X
#     |
#     |
#     |
#     |
#     |
#   Y |
#-------------------------------------------------
pygame.init()
window = pygame.display.set_mode((800,600))  #Creando la ventana 
pygame.display.set_caption("mi primer juego en pygame")

# formas de definir colores
color = (155,140,50)
color1 = pygame.Color(255,38,59)
#----------Dibujando figuras--------------------------
# #dibujamos una linea(canva, punto1, punto2, gruesor)
# pygame.draw.line(window,color1,(60,80),(200,60),10) 
# #dibujamos un circulo (canva,color,punto central, radio)
# pygame.draw.circle(window,(70,100,150),(150,200),20) #dibujamos una linea
# #dibujamos un rectangulo (canva, color, (punto izq sup, ancho,largo))
# pygame.draw.rect(window,color,(300,300,20,50))
# #dibujmos un poligonos(canva, (puntos))
# pygame.draw.polygon(window,(45,245,139),((600,200),(100,400),(200,50)))


#---------------------Cargando imagenes-------------------------------
# image1  = pygame.image.load('Images/paltita.png')
# image2  = pygame.image.load('Images/zombicito.png')
# image3  = pygame.image.load('Images/girasolito.png')
# metodo blit(imagen a mostrar, posicion(x,y))
pos_x = randint(0,800)
pos_y = randint(0,600)

speed = 10
dark = (0,0,0)
limit = True

# creamos un objeto rectangulo
rect1 = pygame.Rect(pos_x,pos_y,20,50)
rect2 = pygame.Rect(pos_x + 30,pos_y + 30,30,60)
#creamos un objeto circulo
# circle1 = pygame.Circle(pos_x,pos_y,10,5)
# print rect2.x, rect2.y, rect2.width, rect2.height


#----------- incluyendo texto-------------
text = pygame.font.Font(None,30)
my_text = text.render("hola",0,(0,0,0),(255,255,255))
while True:
    window.fill(dark)
    # window.blit(image1,(pos_x,pos_y))
    pygame.draw.rect(window,(145,25,68),rect1)
    # circule1 = pygame.draw.circle(window,color,(pos_x,pos_x),10,3)
    # pygame.draw.circle(window,color,circle1)
    # rect1.left , rect1.top = pygame.mouse.get_pos()
    # window.blit(image2,(randint(0,800),randint(0,600)))
    # window.blit(image3,(randint(0,800),randint(0,600)))
    # window.fill(color) # fill() llena nuestra ventana

    #detectando colisiones
    if rect1.colliderect(rect2):
        print("colisiona")
    else:
        pygame.draw.rect(window,(45,255,68),rect2)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key  == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_LEFT:
                pos_x -= speed
                rect1.x = pos_x
            elif event.key == pygame.K_RIGHT:
                pos_x += speed
                rect1.x = pos_x
            elif event.key == pygame.K_UP:
                pos_y -= speed
                rect1.y = pos_y
            elif event.key == pygame.K_DOWN:
                pos_y += speed
                rect1.y = pos_y
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         print("tecla <- libre")
        #     elif event.key == pygame.K_RIGHT:
        #         print("tecla -> libre")
    window.blit(my_text,(10,10))
    # colision_rect(rect1,rect2)
    # limites de la ventana
    # if limit:
    #     if pos_x < 750:
    #         pos_x += speed
    #         rect2.left = pos_x
    #     else:
    #         limit = False
    # else: 
    #     if pos_x > 1:
    #         pos_x -= speed
    #         rect2.left = pos_x
    #     else: 
    #         limit = True

    # obetener posicion del mouse
    # pos_x,pos_y = pygame.mouse.get_pos()

    pygame.display.update()