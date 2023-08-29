#PROYECTO
#NIDIA VANESSA CHÁVEZ RENDÓN
#FUNDAMENTOS DE PROGRAMACIÓN
#IT1
#     __//
##  /.__.\
#   \ \/ /
#'__/    \
# \-      )
#  \_____/
#____|_|____
#    " "

#Proyecto Snake: El juego Snake es uno de los juegos de arcade más populares de todos los tiempos. 
#El objetivo principal del jugador es atrapar el máximo número de frutas sin golpear la pared o a sí mismo.

#SE IMPORTAN LAS LIBRERÍAS NECESARIAS.

#Pygame: Se pueden usar objetos, cargar, mostrar imágenes en diferentes formatos, sonidos, etc. 
#Además, al ser un módulo destinado a la programación de videojuegos se puede monitorizar el teclado o joystick
import pygame
#Time: Está pensada para medir tiempos de ejecución de fragmentos pequeños de código. 
import time
#Random: Permite tener un arreglo de elementos, y elegir uno de ellos de forma aleatoria.
import random
 
#Velocidad con la que avanza snake
snake_speed = 8 
 
#TAMAÑO DE LA VENTANA DE JUEGO.

#Se define el ancho y el alto de la ventana en la que se jugará el juego.
window_x = 500
window_y = 500
 
#COLORES DEL JUEGO.

#Se define el color en formato RGB que se utilizará en el juego para mostrar texto.
#Pygame color: Permite tener un arreglo de elementos, y elegir uno de ellos de forma aleatoria.
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
#INICIALIZAR LA LIBRERÍA PYGAME.

#Pygame.init(): Inicializa todos los módulos de pygame importado
pygame.init()
 
#INICIALIZAR LA VENTANA DEL JUEGO.

#Pygame.display: Ofrece control sobre la pantalla del juego.
#Tiene una única superficie de visualización que o bien está contenida en una ventana o se ejecuta a pantalla completa.
pygame.display.set_caption('SNAKE by: NVCR')
game_window = pygame.display.set_mode((window_x, window_y))
 
#FPS (FRAMES POR SEGUNDO) DEL CONTROLADOR.

#Pygame.time.clock(): Se utiliza para crear un objeto de reloj 
#que se puede utilizar para realizar un seguimiento del tiempo.
fps=pygame.time.Clock()
 
#DEFINICIÓN DE LA POSICIÓN DE SNAKE.

#Al establecer la dirección a DERECHA, me aseguro de que, cada vez que el usuario ejecute el juego, 
#Snake se mueva directamente a la pantalla.

snake_position = [100, 50]
 
#Definir los primeros 4 bloques de movimiento del cuerpo de la serpiente.
#Se iniciliza la posición de la fruta al azar en cualquier lugar de la altura y el ancho definidos
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
              
#LUGAR ALEATORIO DE LA FRUTA.

#Al establecer la dirección a DERECHA, me aseguro de que, cada vez que el usuario ejecute el juego, 
#Snake se mueva directamente a la pantalla.
#Random.randrange: Devuelve un elemento seleccionado aleatoriamente del rango especificado
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
#Establecer que la dirección de movimiento predeterminada de snake será hacia la derecha
direction = 'RIGHT'
change_to = direction
 
#PUNTAJE: INICIO/GAME OVER.

#Score: Se utiliza para calcular la precisión de la facción o el recuento de la predicción correcta en Python.
#Matemáticamente representa la suma de verdaderos positivos y verdaderos negativos de todas las predicciones.

#En esta función, en primer lugar estoy creando un objeto de fuente, es decir, el color de la fuente irá aquí.
#Luego uso render para crear una superficie de fondo que cambiará cada vez que se actualice la puntuación.
#Se crea un objeto rectangular para el objeto de superficie de texto (donde se actualizará el texto)
#Después se muestra la puntuación usando blit, el cual toma dos argumentos: screen.blit(background,(x,y))
score = 0
 
#Función puntaje
def show_score(choice, color, font, size):
   
    #FUENTE DEL PUNTAJE.

    #Pygame.font: El módulo de fuentes permite representar fuentes TrueType en objetos Surface.
    score_font = pygame.font.SysFont(font, size)
     
    #Creación de la superficie de visualización
    #Objeto de puntuación
    score_surface = score_font.render('Puntaje : ' + str(score), True, color)
     
    #Creación de un espacio rectangular para el texto
    #Objeto de superficie
    score_rect = score_surface.get_rect()
     
    #Mostrar texto en la vetana de juego
    game_window.blit(score_surface, score_rect)
 
#Función game over

#En la primera línea, estOY creando un objeto de fuente para mostrar puntuaciones.
#Luego se crea una superficie de texto para renderizar puntuaciones.

def game_over():
   
    #Creación de objeto de fuente
    my_font = pygame.font.SysFont('arial', 50)
     
    #Creción de una superficie de texto "Game over"
    #Dibujo
    game_over_surface = my_font.render(
        'Tu puntaje es : ' + str(score), True, red)
     
    #Creación de un objeto rectangular para el texto "Game over"
    #Objeto de superficie para extablecer el texto
    game_over_rect = game_over_surface.get_rect()
     
    #Se establece la posición del texto "Game over"
    #Establezco la posición del texto en el centro de la pantalla de juego.
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    #Se escribirá el texto en la pantalla.
    #Se muestran las puntuaciones usando blit y actualizando la puntuación en base a la superficie usando flip().
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    #TERMINAR EL JUEGO

    #Time.sleep(): Suspende la ejecución durante el número determinado de segundos.
    #Uso sleep(2) para esperar 2 segundos antes de cerrar la ventana usando quit()
    time.sleep(2)
     
    #DESACTIVAR LA LIBRERÍA

    #Pygame.quit(): Cuando queramos detener nuestro juego y luego salir de la ventana, podemos usar el método. 
    #Este método anulará la inicialización de todos los módulos de Pygame
    pygame.quit()
     
    #CERRAR EL PROGRAMA

    #Quit(): Termina el programa en Python como una forma fácil y efectiva de terminar un script de Python 
    #Cuando este comando se ejecuta, genera una excepción SystemExit en el sistema operativo.
    quit()
 
 
#FUNCIÓN PRINCIPAL.

#Establezco los eventos de teclado que serán responsables del movimiento de la snake.
while True:
     
    #EVENTOS DE TECLADO

    #Pygame.event.get(): 
    for event in pygame.event.get():
        #Event.tipe:
        #Event.key:
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
    #Si se presionan dos teclas simultáneamente.
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    #Movimiento de snake.
    if direction == 'UP': #SUBIR
        snake_position[1] -= 10
    if direction == 'DOWN': #BAJAR
        snake_position[1] += 10
    if direction == 'LEFT': #IZQUIERDA
        snake_position[0] -= 10
    if direction == 'RIGHT': #DERECHA
        snake_position[0] += 10
 
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
        #Pygame.draw: 
        pygame.draw.rect(game_window, green,
                        #Pygame.Rect: 
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    #Condiciones para "Game over"
    #Si la serpiente se golpea a sí misma, se llamará a la función game over.
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    #Manejo del cuerpo de la serpiente
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    #Mostrar de forma continua el puntaje obtenido
    #Muestro las puntuaciones utilizando la función show_score creada anteriormente.
    show_score(1, white, 'arial', 20)
 
    #ACTUALIZACIÓN DE LA PANTALLA DE JUEGO.

    #Pygame.display.update():
    pygame.display.update()
 
    #FPS para frecuencia de actualización de la pantalla de juego
    fps.tick(snake_speed)

#FIN DEL CÓDIGO.