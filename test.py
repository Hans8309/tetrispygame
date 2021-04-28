# https://www.bilibili.com/video/BV13k4y1r7JE?from=search&seid=9751224032757141306
# https://youtu.be/zfvxp7PgQ6c?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB
# Full Code: https://pastebin.com/embed_js/yaWTeF6y

import pygame


pygame.init()


win = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Tetris')

win.fill((122, 180, 100))

pygame.draw.line(win, (255, 0, 0), (0, 0), (200, 200), 8)


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
