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

class Pelota:
    def __init__(self):
        pass

    def pintar (self, pantalla):
        pelota = pygame.Rect(X_PELOTA, Y_PELOTA, ANCHO_PELOTA, ALTO_PELOTA)
        pygame.draw.rect(pantalla, COLOR_PELOTA, pelota)
    


class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        self.pelota = Pelota()
        

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

            # renderizar mis objetos
            # 1 borrar la pantalla  
            #               dimenciones de la pantalla     
            pygame.draw.rect(self.pantalla,
                             COLOR_DE_FONDO,
                             # posicion 
                             ((0, 0), (ANCHO_PANTALLA, ALTO_PANTALLA)))


            # 2 pintar los objetos en la posicion correspodiente
            # pinto el jugador 1 a la izaquierda
            jugador1 = pygame.Rect(MARGEN_JUGADOR, MARGEN, ANCHO_JUGADOR1, ALTO_JUGADOR1)
            pygame.draw.rect(self.pantalla, COLOR_JUGADOR1, jugador1)

            # pinto el jugador 2 a la derecha
            jugador2 = pygame.Rect(MARGEN_JUGADOR2, MARGEN, ANCHO_JUGADOR2, ALTO_JUGADOR2)
            pygame.draw.rect(self.pantalla, COLOR_JUGADOR2, jugador2)

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
