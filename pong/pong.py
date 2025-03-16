import pygame

class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((640, 480))
        

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
            # 1 borrar la pantalla       Rojo, Verde, azul
            pygame.draw.rect(self.pantalla,  (30,     30,     80), ((0, 0), (640, 480)))


            # 2 pintar los objetos en la posicion correspodiente
            rectangulo = pygame.Rect(eje_x/10, eje_y/15, 250, 150)
            pygame.draw.rect(self.pantalla, (150, 150, 150), rectangulo)
            # 3 mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

juego = Pong()
juego.jugar()
