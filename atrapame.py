import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
ventana_ancho = 800
ventana_alto = 600

# Colores
blanco = (255, 255, 255)
azul = (0, 0, 255)

# Crear la ventana
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Atrapa el Objeto")

# Personaje
personaje_ancho = 50
personaje_alto = 50
personaje_x = ventana_ancho // 2 - personaje_ancho // 2
personaje_y = ventana_alto - personaje_alto - 10
personaje_velocidad = 5

# Objeto que cae
objeto_ancho = 50
objeto_alto = 50
objeto_x = random.randint(0, ventana_ancho - objeto_ancho)
objeto_y = 0
objeto_velocidad = 5

# Puntuación
puntuacion = 0
fuente = pygame.font.Font(None, 36)

# Función para mostrar la puntuación
def mostrar_puntuacion():
    texto = fuente.render("Puntuación: " + str(puntuacion), True, azul)
    ventana.blit(texto, (10, 10))

# Bucle principal del juego
jugando = True
reloj = pygame.time.Clock()

while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Mover al personaje
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and personaje_x > 0:
        personaje_x -= personaje_velocidad
    if teclas[pygame.K_RIGHT] and personaje_x < ventana_ancho - personaje_ancho:
        personaje_x += personaje_velocidad

    # Mover el objeto que cae
    objeto_y += objeto_velocidad

    # Verificar si el personaje atrapa el objeto
    if personaje_y < objeto_y + objeto_alto and personaje_x < objeto_x < personaje_x + personaje_ancho:
        puntuacion += 1
        objeto_x = random.randint(0, ventana_ancho - objeto_ancho)
        objeto_y = 0

    # Dibujar la pantalla
    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, (personaje_x, personaje_y, personaje_ancho, personaje_alto))
    pygame.draw.rect(ventana, azul, (objeto_x, objeto_y, objeto_ancho, objeto_alto))

    mostrar_puntuacion()
    pygame.display.update()

    # Limitar la velocidad de fotogramas
    reloj.tick(60)

# Cerrar Pygame
pygame.quit()
