from classes.Post import Post
import pygame
from helpers import screen, from_text_to_array, center_text
from constants import *

class TextPost(Post):
    def __init__(self, username, location, description, text, color_text, color_background):
        super().__init__(username, location, description)
        self.text = from_text_to_array(text)
        self.color_text = color_text
        self.color_background = color_background

    def display(self):
        pygame.draw.rect(screen, self.color_background, pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))
        counter = 0
        text_font = pygame.font.SysFont(FONT_NAME, TEXT_POST_FONT_SIZE)
        for text in self.text:
            text_to_display = text_font.render(text, True, self.color_text)
            text_position = center_text(len(self.text), text_to_display, counter)
            counter += 1
            screen.blit(text_to_display, text_position)
        super().display()

