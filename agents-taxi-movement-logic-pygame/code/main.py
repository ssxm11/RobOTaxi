import pygame
import os

pygame.init()

screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("RobOTaxi")
dt = 0
TAM = 50
matriz = []
taxi = pygame.image.load(os.path.join('img', 'car.png')).convert_alpha()
taxi = pygame.transform.scale(taxi, (50, 50))

pasajero = pygame.image.load(os.path.join('img', 'pasajero.png')).convert_alpha()
pasajero = pygame.transform.scale(pasajero, (50, 50))

destino = pygame.image.load(os.path.join('img', 'ubicacion.png')).convert_alpha()
destino = pygame.transform.scale(destino, (50, 50))

with open("tests/Prueba1.txt", "r") as archivo:
    for linea in archivo:
        fila = linea.strip().split()
        fila = [int(x) for x in fila]
        matriz.append(fila)

    print(matriz)
running = True

taxi_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))


    OFFSET_X = 100
    OFFSET_Y = 50

    for y in range(len(matriz)):
        for x in range(len(matriz[y])):

            valor = matriz[y][x]
            pos_x = x * TAM + OFFSET_X
            pos_y = y * TAM + OFFSET_Y

            rect = pygame.Rect(pos_x, pos_y, TAM, TAM)
            
            if valor == 1: 
                # Muro - gris oscuro
                pygame.draw.rect(screen, (100, 100, 100), rect)

            elif valor == 0:
                # Camino libre - gris claro
                pygame.draw.rect(screen, (200, 200, 200), rect)
                        
            elif valor == 3:
                # Ubicación especial - rojo
                pygame.draw.rect(screen, (255, 100, 100), rect)

            elif valor == 4:
                # Pasajero
                pygame.draw.rect(screen, (200, 200, 200), rect)
                screen.blit(pasajero, (pos_x, pos_y))

            elif valor == 5:
                # Destino
                pygame.draw.rect(screen, (200, 200, 200), rect)
                screen.blit(destino, (pos_x, pos_y))
            
            elif valor == 2:
                # Taxi - pintar en coordenadas correctas
                pygame.draw.rect(screen, (200, 200, 200), rect)
                screen.blit(taxi, (pos_x, pos_y))

    pygame.display.update()
    dt = clock.tick(60) / 1000
pygame.quit()
