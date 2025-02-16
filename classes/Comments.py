import pygame
from helpers import screen
from constants import *
class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, i):
        if i == 0:
            font = pygame.font.SysFont(FONT_NAME, COMMENT_TEXT_SIZE)
            text = font.render(self.text, True, BLACK)
            screen.blit(text, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS])
        else:
            font = pygame.font.SysFont(FONT_NAME, COMMENT_TEXT_SIZE)
            text = font.render(self.text, True, BLACK)
            screen.blit(text, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + i * COMMENT_LINE_HEIGHT])