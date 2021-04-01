# INSTRUCCIONES: Presiona la tecla 'P' para poner pausa,
#                en pausa, presionar 'P' de nuevo para continuar
#                y presionar 'Q' para salir del juego.
#                Presionar 'R' durante el juego para reiniciar.
#                Controles: WASD y flechas (ARRIBA, ABAJO, IZQ, DER)

import pygame, random

def moverSerpiente(direccion, serpiente):
    global vel
    nuevaCabezaX = serpiente[0][0]
    nuevaCabezaY = serpiente[0][1]
    serpiente.pop()

    if direccion == 'ARRIBA':
        nuevaCabezaY -= vel
    elif direccion == 'ABAJO':
        nuevaCabezaY += vel
    elif direccion == 'DERECHA':
        nuevaCabezaX += vel
    elif direccion == 'IZQUIERDA':
        nuevaCabezaX -= vel

    serpiente.insert(0, (nuevaCabezaX, nuevaCabezaY))

def dibujar(surface, serpiente, serpiente2, anchoPixel):
    surface.fill((35, 35, 35))      # Not quite black
    for pixel in serpiente:
        pygame.draw.rect(surface, (255,0,0), (pixel[0],pixel[1],anchoPixel,anchoPixel))
    for pixel2 in serpiente2:
        pygame.draw.rect(surface, (0,0,255), (pixel2[0],pixel2[1],anchoPixel,anchoPixel))
    pygame.display.update()

def exitGame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # Límites de la ventana de 500 x 500 para la colisión serpiente-borde
    if serpiente[0][0] >= 500 or serpiente[0][0] <= -25 or serpiente[0][1] >= 500 or serpiente[0][1] <= -25:
        pygame.quit()
        quit()
    if serpiente2[0][0] >= 500 or serpiente2[0][0] <= -25 or serpiente2[0][1] >= 500 or serpiente2[0][1] <= -25:
        pygame.quit()
        quit()
    # Colisiones serpiente-serpiente
    if serpiente[0] in serpiente[2:]:
        pygame.quit()
        quit()
    if serpiente2[0] in serpiente2[2:]:
        pygame.quit()
        quit()
    # Colisiones serpiente1 con serpiente2
    if serpiente[0] in serpiente2[:]:
        pygame.quit()
        quit()
    if serpiente2[0] in serpiente[:]:
        pygame.quit()
        quit()

def dibujarComida(surface, comidaX, comidaY, anchoPixel): 
    pygame.draw.rect(surface, (0,255,0), (comidaX,comidaY,anchoPixel,anchoPixel))
    pygame.display.update()

def comer():
    global comidaX, comidaY
    # Detectar colisión serpiente-comida y cambiar posición de comida
    # Snake 1
    if serpiente[0][0] == comidaX and serpiente[0][1] == comidaY:
        serpiente.insert(0,(comidaX, comidaY))
        '''La pantalla es de 500x500 y el ancho de los pixeles es 25,
           por lo que la comida debe aparecer en una posición que sea múltiplo de 25.
           El rango aleatorio 1-18 se eligió para que la comida no apareza pegada
           a los bordes de la pantalla o fuera de esta.'''
        comidaX = random.randint(1,18) * 25
        comidaY = random.randint(1,18) * 25
        while (comidaX,comidaY) in serpiente:
            comidaX = random.randint(1,18) * 25
            comidaY = random.randint(1,18) * 25    
    # Snake 2
    if serpiente2[0][0] == comidaX and serpiente2[0][1] == comidaY:
        serpiente2.insert(0, (comidaX, comidaY))
        comidaX = random.randint(1,18) * 25
        comidaY = random.randint(1,18) * 25
        while (comidaX,comidaY) in serpiente2:
            comidaX = random.randint(1,18) * 25
            comidaY = random.randint(1,18) * 25

def pause():
	paused = True
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					paused = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()

def score(surface):
    global serpiente
    score = len(serpiente) - 1
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'Score: {score}', True, (255,255,255))
    surface.blit(img, (10, 10))
    pygame.display.update()

# Snake 1
cabezaX = 400
cabezaY = 50
direccion = 'IZQUIERDA'
serpiente = [(cabezaX, cabezaY)]

# Snake 2
cabeza2X = 50
cabeza2Y = 50
direccion2 = 'DERECHA'
serpiente2 = [(cabeza2X, cabeza2Y)]

# Game Parameters
screenSize = 500
anchoPixel = 25
vel = 25
clock = pygame.time.Clock()

# Generate food in random place
comidaX = random.randint(1,18) * 25
comidaY = random.randint(1,18) * 25

def main():
    global serpiente, cabezaX, cabezaY, direccion
    global serpiente2, cabeza2X, cabeza2Y, direccion2
    global screenSize, anchoPixel, vel, comidaX, comidaY
    pygame.init()
    win = pygame.display.set_mode((screenSize, screenSize))
    pygame.display.set_caption('Snake Game')

    while True:
        pygame.time.delay(100)
        exitGame()
        keys = pygame.key.get_pressed()
        # Snake 1 controls
        if keys[pygame.K_RIGHT] and direccion != 'IZQUIERDA':
            direccion = 'DERECHA'
        elif keys[pygame.K_LEFT]and direccion != 'DERECHA':
            direccion = 'IZQUIERDA'
        elif keys[pygame.K_UP]and direccion != 'ABAJO':
            direccion = 'ARRIBA'
        elif keys[pygame.K_DOWN] and direccion != 'ARRIBA':
            direccion = 'ABAJO'
        # Snake 2 controls
        if keys[pygame.K_d] and direccion2 != 'IZQUIERDA':
            direccion2 = 'DERECHA'
        elif keys[pygame.K_a] and direccion2 != 'DERECHA':
            direccion2 = 'IZQUIERDA'
        elif keys[pygame.K_w] and direccion2 != 'ABAJO':
            direccion2 = 'ARRIBA'
        elif keys[pygame.K_s] and direccion2 != 'ARRIBA':
            direccion2 = 'ABAJO'
        # Pause and reset
        if keys[pygame.K_p]:		# Presionar 'p' para pausar.
            pause()
        elif keys[pygame.K_r]:      # Presionar 'r' para reiniciar.
            # Snake 1
            cabezaX = 400
            cabezaY = 50
            direccion = 'IZQUIERDA'
            # Snake 2
            cabeza2X = 50
            cabeza2Y = 50
            direccion2 = 'DERECHA'

            comidaX = random.randint(1,18) * 25
            comidaY = random.randint(1,18) * 25
            serpiente = [(cabezaX,cabezaY)]
            serpiente2 = [(cabeza2X, cabeza2Y)]

        moverSerpiente(direccion, serpiente)
        moverSerpiente(direccion2, serpiente2)
        dibujar(win, serpiente, serpiente2, anchoPixel)
        comer()
        dibujarComida(win, comidaX, comidaY, anchoPixel)
        score(win)

        clock.tick(60)

main()