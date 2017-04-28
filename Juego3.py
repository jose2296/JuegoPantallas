import pygame
import random
import os
import time
from pygame.locals import *



#--------------------------EVENTO BUCLEPRINCIPAL ------------------------------------
def events(fin):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inicio()
            #if event.key == pygame.K_c:
                #fin = True
            if event.key == pygame.K_p:
                paused()
    return fin



#-----------------------Variables de la pantalla ------------------------------------
ANCHO = 600
ALTO  = 400
ANCHOMEDIO = ANCHO/2
ALTOMEDIO = ALTO/2
AREA = ANCHO * ALTO


 
#-------------------------Inicializar Display ------------------------------------

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Titulo ventana")
reloj = pygame.time.Clock()





#-------------------------------COLORES------------------------------------

blanco = (255,255,255)
negro = (0,0,0)
rojo = (150,0,0)
verde = (0,150,0)
azul = (0,0,150)
rojoclaro = (255,0,0)
verdeclaro = (0,255,0)
azulclaro = (0,0,255)
amarillo = (255,255,0)


#--------------------------------FUENTES------------------------------------

muygrande = pygame.font.Font(None, 100)
grande = pygame.font.Font(None, 75)
mediana = pygame.font.Font(None, 50)
pequena = pygame.font.Font(None, 25)

#-----------------------ARRAY DE IMAGENES DE LOS BOTONES--------------------------------
arraydeimagenes = ["imagenes/verde.png","imagenes/verdehover.png","imagenes/azul.png","imagenes/azulhover.png","imagenes/rojo.png","imagenes/rojohover.png","imagenes/volver.png","imagenes/volverhover.png"]


#---------------------------------VARIABLES---------------------------------------------------

lado = 25
botonw = 150
botonh = 50



#-----------------------FUNCIONES DE TEXTO Y BOTONES------------------------------------
def centrartexto(mensaje,color,fuente):
    texto = fuente.render(mensaje, True, color)
    return texto,texto.get_rect()


def imprimirTexto(mensaje,color,fuente,x = 0, y=0):
    textopantalla,textoRect = centrartexto(mensaje,color,fuente)
    textoRect.center = (ANCHO/2)+x,(ALTO/2)+y
    pantalla.blit(textopantalla, textoRect)


def imprimirTextoBoton(mensaje,color,fuente, x,y,ancho,alto):
    textopantalla,textoRect = centrartexto(mensaje,color,fuente)
    textoRect.center = (x+(ancho/2)),(y+(alto/2))
    pantalla.blit(textopantalla, textoRect)

def boton(texto,x,y,color,accion = None):
    posraton = pygame.mouse.get_pos()
    #pygame.draw.rect(pantalla, color, [x,y,botonw,botonh])

    imagen = 6
    
    if accion == "jugar":
        imagen = 0
    elif accion == "controles":
        imagen = 2
    elif accion == "salir":
        imagen = 4
    if accion == "volver":
        imagen == 6
        
    jugar = pygame.image.load(arraydeimagenes[imagen])
    jugarhover = pygame.image.load(arraydeimagenes[imagen+1])

    pantalla.blit(jugar,(x,y))

    if (posraton[0] >= x and posraton[0] <= x+botonw) and (posraton[1] >= y and posraton[1] <= y+botonh):
        if accion == "jugar":
##            pygame.draw.rect(pantalla, verdeclaro, [x,y,botonw,botonh])
            pantalla.blit(jugarhover,(x,y))
            if pygame.mouse.get_pressed() == (1,0,0):
                buclePrincipal()
        elif accion == "controles":
##            pygame.draw.rect(pantalla, azulclaro, [x,y,botonw,botonh])
            pantalla.blit(jugarhover,(x,y))
            if pygame.mouse.get_pressed() == (1,0,0):
                pantallacontroles()
        elif accion == "salir":
##            pygame.draw.rect(pantalla, rojoclaro, [x,y,botonw,botonh])
            pantalla.blit(jugarhover,(x,y))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.quit()
                quit()
        if accion == "volver":
##            pygame.draw.rect(pantalla, azulclaro, [x,y,botonw,botonh])
            pantalla.blit(jugarhover,(x,y))
            if pygame.mouse.get_pressed() == (1,0,0):
                time.sleep(0.21)
                inicio()


##    imprimirTextoBoton(texto,blanco,pequena, x,y,botonw,botonh)

#-----------------------------------------------------------------------------------------------------------------------------



#CLASES
#------------------------------CLASES----------------------------------------------------------------

#-----CLASE JUGADOR---------------------------------------------------------------------

class jugador:
    def __init__(self,velocidad, lado, tiempo,cuanto):
        self.velocidad= velocidad
        self.lado = lado
        self.tiempo = tiempo
        self.cuanto = cuanto


    def setPosicion(self,x,y):
        self.x = x
        self.y = y
        self.xVelocidad = 0
        self.yvelocidad = 0
        

    def keys(self):
        k = pygame.key.get_pressed()


        
        self.xVelocidad = 0
        self.yVelocidad = 0
        
        if k[K_LEFT]:
            self.xVelocidad = -self.velocidad
            self.yVelocidad = 0
        elif k[K_RIGHT]:
            self.xVelocidad = self.velocidad
            self.yVelocidad = 0
        elif k[K_DOWN]:
            self.yVelocidad = self.velocidad
            self.xVelocidad = 0
        elif k[K_UP]:
            self.yVelocidad = -self.velocidad
            self.xVelocidad = 0

        

        

            
    def mover(self):
        self.x += self.xVelocidad
        self.y += self.yVelocidad


    def draw(self):
        #pygame.draw.circle(pantalla, blanco, (self.x,self.y -25), 25, 0)
        pygame.draw.rect(pantalla, blanco, [self.x, self.y, self.lado,self.lado])

    def do(self):
        self.keys()
        self.mover()




#-------------------------FUNCION MENU OPCIONES----------------------------------------
def pantallacontroles():

    controles = True

    while controles:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inicio()
        pantalla.fill(negro)

        
        boton("volver",(ANCHO/2)-(botonw/2), 325 ,azul, accion = "volver")

        imprimirTexto("Controles", blanco,grande,0,-150)
        imprimirTexto("Flechas: Movimiento", blanco,mediana,0,-80)
        imprimirTexto("Espacio: Disparar", blanco,mediana,0,-30)
        imprimirTexto("Escape: volver al inicio", blanco,mediana,0,20)
        imprimirTexto("P: menu de pausa", blanco,mediana,0,70)
        
        pygame.display.update()
        reloj.tick(30)



#-----------------------------FUNCION MENU PRINCIPAL------------------------------------
def inicio():

    inicio = True

    puntero = 0
    
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        

        pantalla.fill(negro)

        imprimirTexto("Titulo del Juego", blanco,muygrande,0,-125)
        boton("Jugar",(ANCHO/2)-(botonw/2), 150, verde, accion = "jugar")
        boton("Controles",(ANCHO/2)-(botonw/2) ,225, azul, accion = "controles")
        boton("Salir",(ANCHO/2)-(botonw/2), 300 ,rojo, accion = "salir")
        
        
        pygame.display.update()
        reloj.tick(30)



#--------------------------MENU DE PAUSA------------------------------------------------
def paused():

    paused = True
    pantalla.fill(verde)
    imprimirTexto("Pausa", blanco,grande,0,-50)
    imprimirTexto("Presiona enter para continuar", blanco,mediana)
    imprimirTexto("Presiona ESC para salir al menu", blanco,mediana,0,50)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
                if event.key == pygame.K_ESCAPE:
                    inicio()

        

        pygame.display.update()
        reloj.tick(15)


    
#--------------------------BUCLEPRINCIPAL---------------------------------------------------
def buclePrincipal():

    tiempo = 0
    cuanto = 100
    #CREAR OBJETO DE JUGADOR:
    p = jugador(lado,lado,tiempo,cuanto)
    p.setPosicion(100,100)
    
    salir = True
    fin = False


    


    while salir:

        #fin del juego
        while fin:
            pantalla.fill(blanco)
            imprimirTexto("Fin juego", rojo,grande,0,-50)
            imprimirTexto("Presoina enter para jugar de nuevo", rojo,mediana)
            imprimirTexto("Presoina ESC para salir al menu", rojo,mediana,0,50)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        buclePrincipal()
                    if event.key == pygame.K_ESCAPE:
                        inicio()


                    
        events(fin)    


        reloj.tick(20)



        if pygame.time.get_ticks()- tiempo > cuanto:
            tiempo = pygame.time.get_ticks()
            p.do()


        p.draw()

        
        pygame.display.update()

        
        pantalla.fill(negro)


    pygame.quit()
    quit()

    
inicio()
buclePrincipal()
