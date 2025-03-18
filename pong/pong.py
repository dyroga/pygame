import pygame
#############################################################################
# configuracion pantalla

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
#colores          rojo  verde    azul
COLOR_DE_FONDO = (50,     50,     50)

#configuraciones jugadores
# jugador 1
ALTO_JUGADOR1 = 120
ANCHO_JUGADOR1 = 15
MARGEN_JUGADOR = 20
COLOR_JUGADOR1 = (150,  150,    150)
MARGEN = (ALTO_PANTALLA - ALTO_JUGADOR1)/2

# jugador 2
ALTO_JUGADOR2 = ALTO_JUGADOR1
ANCHO_JUGADOR2 = ANCHO_JUGADOR1
MARGEN_JUGADOR2 = ANCHO_PANTALLA - MARGEN_JUGADOR - ANCHO_JUGADOR2
COLOR_JUGADOR2 = COLOR_JUGADOR1

# pelota (rectangulo)
ALTO_PELOTA = 8
ANCHO_PELOTA = ALTO_PELOTA
Y_PELOTA = (ALTO_PANTALLA/2) - (ALTO_PELOTA/2)
X_PELOTA = (ANCHO_PANTALLA - ANCHO_PELOTA) /2
COLOR_PELOTA = (200, 200, 200)

#############################################################################
class Pintable:
    def __init__(self, x, y, ancho, alto):
        self.pos_x = x
        self.pos_y = y
        self.ancho = ancho
        self.alto =  alto

    def pintar (self, pantalla):
        obj = pygame.Rect(self.pos_x, self.pos_y, self.ancho, self.alto)
        pygame.draw.rect(pantalla, COLOR_JUGADOR1, obj)


class Pelota(Pintable):
    def __init__(self):
        super().__init__(X_PELOTA, Y_PELOTA, ANCHO_PELOTA, ALTO_PELOTA)

    
class Jugador(Pintable):
    def __init__(self, x):
         
         Y = (ALTO_PANTALLA - ALTO_JUGADOR1) / 2
         super().__init__(x, Y, ANCHO_JUGADOR1, ALTO_JUGADOR1)

        
class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        self.pelota = Pelota()
        self.jugador1 = Jugador(MARGEN_JUGADOR)
        self.jugador2 = Jugador(MARGEN_JUGADOR2)


    def jugar(self):

        salir = False
        eje_x = 0
        eje_y = 0
        # bucle pincipal (main loop)
        while not salir:
            eje_x += 1
            eje_y += 1
            # capturar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("has pulsado el boton de cerrar la ventana")
                    salir = True
                if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                    print("has soltado la tecla escape")
                    salir = True

            # renderizar mis objetos
            # 1 borrar la pantalla  
            #               dimenciones de la pantalla     
            pygame.draw.rect(self.pantalla,
                             COLOR_DE_FONDO,
                             # posicion 
                             ((0, 0), (ANCHO_PANTALLA, ALTO_PANTALLA)))


            # 2 pintar los objetos en la posicion correspodiente
            # pinto los jugadores
            self.jugador1.pintar(self.pantalla)
            self.jugador2.pintar(self.pantalla)

            # pintamos la red
            self.pinto_red()

            #pintamos la pelota en el centro de la pantalla
            self.pelota.pintar(self.pantalla)

            # 3 mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

    def pinto_red(self):
        """pinta l red en la pantalla"""
        # esta centrada horizontalmente
        X_RED = ANCHO_PANTALLA / 2 - 1
        # es un conjunto de lineas discontinuas
        LINEA = 20
        VACIO = 15
        ANCHO_RED = 5
        # ocupa todo el alto de la pantalla
        for pos_y in range(0, ALTO_PANTALLA, LINEA+VACIO):
            pygame.draw.line(self.pantalla, COLOR_JUGADOR1, (X_RED, pos_y), (X_RED, pos_y + LINEA), ANCHO_RED)
            """(
                self.pantalla,
                COLOR_JUGADOR1,
                (X_RED, pos_y),

            )""" 

juego = Pong()
juego.jugar()
