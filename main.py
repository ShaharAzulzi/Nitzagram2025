import pygame

from buttons import like_button, comment_button, click_post_button, view_more_comments_button
from helpers import screen, mouse_in_button, read_comment_from_user
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes import Comments, Button, ImagePost, TextPost


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))


    noa_kirel = ImagePost.ImagePost("marat", "desert", "Tornado", "Images/noa_kirel.jpg")
    ronaldo = ImagePost.ImagePost("cr7", "portugal", "Ronaldo the GOAT", "Images/ronaldo.jpg")

    text_post = TextPost.TextPost("bot", "Argentina", "Messi the bot", "Messi got the World Cup!",
                                  (235, 152, 232), (28, 19, 28))

    posts = [noa_kirel, ronaldo, text_post]

    current_index = 0
    current_post = posts[current_index]

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button, pos):
                    current_post.add_like()
                    pass
                elif mouse_in_button(comment_button, pos):
                    comment = read_comment_from_user()
                    current_post.add_comment(comment)
                    pass
                elif mouse_in_button(click_post_button, pos):
                    current_index = (current_index + 1) % len(posts)
                    current_post = posts[current_index]
                    current_post.reset_comment_display_index()

                elif mouse_in_button(view_more_comments_button, pos):
                    current_post.view_more_comments()

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        current_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()