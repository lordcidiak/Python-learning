#es importante instalar estas dos librerias pygame y numpy

#autor juan pablo sanchez 
import pygame
import numpy as np

pygame.init()
#ancho y alto de la pantalla
width, height = 1000, 1000
#creacion de la pantalla
screen = pygame.display.set_mode((height, width))
#color de la pantalla gris oscuro
bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 25, 25

dimCW = width  / nxC
dimCH = height / nyC

gameState = np.zeros((nxC, nyC))


#bucle de ejecucion

while True:

    for y in range(0, nxC):
        for x in range(0, nyC):

            n_neigh = gameState[(x-1)   % nxC, (y-1)   % nyC] + \
                      gameState[(x)     % nxC, (y - 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x - 1) % nxC, (y)     % nyC] + \
                      gameState[(x + 1) % nxC, (y)     % nyC] + \
                      gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                      gameState[(x)     % nxC, (y + 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y + 1) % nyC] + \


                if gameState[x ,y ] == 0 and n_neigh == 3:
                    gameState[x, y] = 1

                elif gameState [x, y] == 1 and (n_neigh < 2 or n_neigh > 3);
                    gameState[x, y] = 0
 \
                #se crea el poligono de cada celda a dibujar
            poly = [((x) * dimCW,   y * dimCH),
                        ((x+1) * dimCW, y * dimCH),
                        ((x+1) * dimCW, (y+1) * dimCH),
                        ((x) * dimCW,(y+1) * dimCH)]


            pygame.draw.polygon(screen, (128,128,128), poly, 1)
    pygame.display.flip()

