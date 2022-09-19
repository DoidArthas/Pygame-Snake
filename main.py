from pygame import font
from pygame import event
from pygame import display
from time import sleep
from pygame import time
import game

import apple as ap
import snake as sn

# Cria o jogo como um objeto, inicializando o pygame e recuperando os valores do overlay (values.properties).
gm = game.game()

# Cria a maçã a ser coletada no jogo, precisa do tamanho da tela que vem do objeto do jogo.
apple = ap.apple(gm.screenWidthRatio, gm.screenHeightRatio)

# Cria o objeto do jogador.
snake = sn.snake()

# Aqui é onde o jogo acontece
while not gm.game_over:
    # Controla a velocidade do jogo.
    sleep(gm.sleepTimeMS)

    # Controla os eventos.
    gm.event_handler(event.get())

    # Verifica e trata as colisões.
    apple.collision(gm, snake)

    # Check if snake collided with something
    gm.game_over = snake.collision_verifier(gm.screen)

    if gm.game_over:
        break

    for i in range(len(snake.position) - 1, 0, -1):
        snake.position[i] = (snake.position[i - 1][0], snake.position[i - 1][1])

    # Move o jogador.
    gm.move(snake)

    gm.screen.fill((0, 0, 0))
    gm.screen.blit(apple.surface, apple.position)

    gm.draw_lines()

    score_font = gm.font.render('Score: %s' % (gm.score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (gm.screen.get_width() - 120, 10)
    gm.screen.blit(score_font, score_rect)

    for pos in snake.position:
        gm.screen.blit(snake.surface, pos)

    display.update()

while True:
    game_over_font = font.Font(gm.font_family, 45)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    gm.screen.blit(game_over_screen, game_over_rect)
    display.update()
    time.wait(500)
    while True:
        gm.event_handler(event.get())
