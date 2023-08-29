#PROYECTO
#NIDIA VANESSA CHÁVEZ RENDÓN
#FUNDAMENTOS DE PROGRAMACIÓN
#IT1


#Se importan las librerías necesarias
import pygame
import time
import random
 
#Velocidad con la que avanza la serpiente
snake_speed = 8 
 
#Tamaño de la ventana del juego
window_x = 750
window_y = 500
 
#Colores del juego
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

main_image=pygame.image.load("snake.png")
pause_image=pygame.image.load("pausa.png")

def start_menu(start,window):
    window.blit(main_image, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            #sys.exit()

        elif event.type==pygame.KEYDOWN:
            if event.key:
                return False

    return True

def pause_game(window):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            #sys.exit()

        if event.ype==pygame.KEYDOWN:
            if event.key==pygame.k_c:
                paused=False

            elif event.key==pygame.k_q:
                pygame.quit()
                #sys.exit()

    window.blit(pause_image, (0, 0))
    pygame.display.update()
 
#Inicializar librería pygame
pygame.init()
 
#Inicializar la ventana del juego
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))
 

#FPS (Frames poor segundo) del controlador 
fps = pygame.time.Clock()
 
#Definición de la posición predeterminada de snake
snake_position = [100, 50]
 
#Definir los primeros 4 bloques de movimiento del cuerpo de la serpiente
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
              
#Lugar aleatorio de la fruta
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
#Establecer que la dirección de movimiento predeterminada de snake será hacia la derecha
direction = 'RIGHT'
change_to = direction
 
#Inicio del puntaje
score = 0
 
#Función puntaje
def show_score(choice, color, font, size):
   
    #Fuente de la puntuación
    score_font = pygame.font.SysFont(font, size)
     
    #Creación de la superficie de visualización
    #Objeto de puntuación
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    #Creación de un espacio rectangular para el texto
    #Objeto de superficie
    score_rect = score_surface.get_rect()
     
    #Mostrar texto en la vetana de juego
    game_window.blit(score_surface, score_rect)
 
#Función game over
def game_over():
   
    #Creación de objeto de fuente
    my_font = pygame.font.SysFont('arial', 50)
    start=True
     
    #Creción de una superficie de texto "Game over"
    #Dibujo
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    #Creación de un objeto rectangular para el texto "Game over"
    #Objeto de superficie para extablecer el texto
    game_over_rect = game_over_surface.get_rect()
     
    #Se establece la posición del texto "Game over"
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    #Se escribirá el texto en la pantalla
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    #Cerrar el juego luego de 2 segundos de mostrar texto "Game over"
    time.sleep(2)
     
    #Desactivar librería
    pygame.quit()
     
    #Cerrar el programa
    quit()
 
 
#Función principal
while True:

    while start:
        start=start_menu(start, #window
        )
     
    #Eventos de teclado para el manejo
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #SUBIR
            if event.key == pygame.K_UP: #BAJAR
                change_to = 'UP'
            if event.key == pygame.K_DOWN: #BAJAR
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT: #IZQUIERDA
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    #Evitar que snake se mueva en dos direcciones distintas 
    #Si se presionan dos teclas simultáneamente
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    #Movimiento de snake
    if direction == 'UP': #SUBIR
        snake_position[1] -= 10
    if direction == 'DOWN': #BAJAR
        snake_position[1] += 10
    if direction == 'LEFT': #IZQUIERDA
        snake_position[0] -= 10
    if direction == 'RIGHT': #DERECHA
        snake_position[0] += 10


    #if event.key==pygame.K_p:
        #pause_game(window)
 
    #Mecanismo de movimiento de snake 
    #Aumento en el puntaje de 10 en 10 cuando snake come la fruta
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    #Condiciones para "Game over"
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    #Manejo del cuerpo de la serpiente
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    #Mostrar de forma continua el puntaje obtenido
    show_score(1, white, 'arial', 20)
 
    #Actualización de la pantalla de juego
    pygame.display.update()
 
    #FPS para frecuencia de actualización de la pantalla de juego
    fps.tick(snake_speed)