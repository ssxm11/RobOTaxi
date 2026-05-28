import pygame
import os
from code.taxi import Taxi

pygame.init()

screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("RobOTaxi")
dt = 0
TAM = 50

taxi_img = pygame.image.load(os.path.join('img', 'car.png')).convert_alpha()
taxi_img = pygame.transform.scale(taxi_img, (50, 50))

pasajero_img = pygame.image.load(os.path.join('img', 'pasajero.png')).convert_alpha()
pasajero_img = pygame.transform.scale(pasajero_img, (50, 50))

destino_img = pygame.image.load(os.path.join('img', 'ubicacion.png')).convert_alpha()
destino_img = pygame.transform.scale(destino_img, (50, 50))

# Inicializar el taxi desde la clase
taxi = Taxi("tests/Prueba1.txt")
matriz = taxi.matriz

print(f"Matriz cargada: {len(matriz)} filas")
print(f"Posición inicial del taxi: ({taxi.x}, {taxi.y})")
print(f"Pasajeros totales en la ciudad: {taxi.pasajeros_totales}")

running = True

OFFSET_X = 100
OFFSET_Y = 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    # Dibujar la matriz
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
                screen.blit(pasajero_img, (pos_x, pos_y))

            elif valor == 5:
                # Destino
                pygame.draw.rect(screen, (200, 200, 200), rect)
                screen.blit(destino_img, (pos_x, pos_y))
            
            elif valor == 2:
                # Taxi inicial
                pygame.draw.rect(screen, (200, 200, 200), rect)
                screen.blit(taxi_img, (pos_x, pos_y))

    # Dibujar el taxi en su posición actual
    taxi_pos_x = taxi.x * TAM + OFFSET_X
    taxi_pos_y = taxi.y * TAM + OFFSET_Y
    screen.blit(taxi_img, (taxi_pos_x, taxi_pos_y))

    # Movimiento del taxi con teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        taxi.up()
    if keys[pygame.K_s]:
        taxi.down()
    if keys[pygame.K_a]:
        taxi.left()
    if keys[pygame.K_d]:
        taxi.right()
    
    # Recoger pasajero con espacio
    if keys[pygame.K_SPACE]:
        if taxi.recoger_pasajero():
            print(f"Pasajero recogido! Total: {taxi.pasajeros_recogido}/{taxi.pasajeros_totales}")

    # Mostrar información del taxi
    font = pygame.font.Font(None, 24)
    texto_posicion = font.render(f"Pos: ({taxi.x}, {taxi.y})", True, (255, 255, 255))
    texto_pasajeros = font.render(f"Pasajeros: {taxi.pasajeros_recogido}/{taxi.pasajeros_totales}", True, (255, 255, 255))
    screen.blit(texto_posicion, (10, 10))
    screen.blit(texto_pasajeros, (10, 40))

    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
