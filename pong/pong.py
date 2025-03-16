import pygame
#############################################################################
# configuracion pantalla

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
#colores          rojo  verde    azul
COLOR_DE_FONDO = (40,     60,     100)

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

#############################################################################

class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        

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
            # 3 mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

juego = Pong()
juego.jugar()
