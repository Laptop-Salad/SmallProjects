"""
Bouncing dvd screen saver
"""
import pygame

# Logo class
class Logo:
    def __init__(self, x, y, text, dir):
        self.x = x
        self. y = y
        self.text = text
        self.dir = dir

# Pygame setup
pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)
dvd = font.render('DVD', True, 'blue')
running = True
x = None
y = None
vel = 5
dir = 'br'
logos = [
    Logo(20, screen_height - 20, font.render('DVD', True, 'blue'), 'tr'),
    Logo(screen_width - 20, 150, font.render('DVD', True, 'green'), 'bl'),
    Logo(screen_width - 20, 100, font.render('DVD', True, 'red'), 'tl'),
    Logo(0 + 20, 320, font.render('DVD', True, 'orange'), 'br'),
    Logo(10, 0 + 20, font.render('DVD', True, 'purple'), 'bl'),
]

# Keep track of corners hit
corner_hits = 0
pygame.display.set_caption('Corners Hit: {}'.format(corner_hits))


while running:
    # If the user clicks x to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.time.delay(20)
    
    # Reset the screen
    screen.fill('black')
    
    # For each logo
    for logo in logos:
        # Check logo hit corner
        
        # Top left corner
        if logo.x == 20 and y == 20:
            logo.x += 1
            logo.dir = 'br'
            corner_hits += 1
            pygame.screen.set_caption('Corners Hit: {}'.format(corner_hits))
        # Top right corner
        elif logo.x == 590 and logo.y == 20:
            logo.x -= 1
            logo.dir = 'bl'
            corner_hits += 1
            pygame.screen.set_caption('Corners Hit: {}'.format(corner_hits))
        # Bottom left corner
        elif logo.x == 20 and logo.y == 390:
            logo.x += 1
            logo.dir = 'tr'
            corner_hits += 1 
            pygame.screen.set_caption('Corners Hit: {}'.format(corner_hits))
        # Bottom right corner
        elif logo.x == 590 and logo.y == 390:
            logo.x -= 1
            logo.dir = 'tl'
            corner_hits += 1
            pygame.screen.set_caption('Corners Hit: {}'.format(corner_hits))
        
        """
        If hit an edge
            tl  top   tr
               ______
        left |        | right
             | ______ |
           bl  bottom  br
        """
        if (logo.x + 20) > screen_width or (logo.y + 20) > screen_height or (logo.x - 20) < 0 or (logo.y - 20) < 0:
            # If direction is bottom right
            if logo.dir == 'br':
                # If hit bottom edge
                if (logo.y + 20) > screen_height:
                    logo.dir = 'tr'
                    logo.y = screen_height - 20
                # If hit right edge
                elif (logo.x + 20) > screen_width:
                    logo.dir = 'bl'
                    logo.x = screen_width - 20
            # If direction is top right
            elif logo.dir == 'tr':
                # If hit top edge
                if (logo.y - 20) < 0:
                    logo.dir = 'br'
                    logo.y = 0 + 20
                # If hit right edge
                elif (logo.x + 20) > screen_width:
                    logo.dir = 'tl'
                    logo.x = screen_width - 20
            # If direction is bottom left
            elif logo.dir == 'bl':
                # If hit bottom edge
                if (logo.y + 20) > screen_height:
                    logo.dir = 'tl'
                    logo.y = screen_height - 20
                # If hit left edge
                elif (logo.x - 20) < 0:
                    logo.dir = 'br'
                    logo.x = 0 + 20 
            # If direction is top left
            elif logo.dir == 'tl':
                # If hit top edge 
                if (logo.y - 20) < 0:
                    logo.dir = 'bl'
                    logo.y = 0 + 20
                # If hit left edge
                elif (logo.x - 20) < 0:
                    logo.dir = 'tr'
                    logo.x = 0 + 20
        else:
            # Move text
            # If direction is bottom right
            if logo.dir == 'br':
                logo.x += 2
                logo.y += 1
            # If direction is bottom left
            elif logo.dir == 'bl':
                logo.x -= 2
                logo.y += 1
            # If direction is top right
            elif logo.dir == 'tr':
                logo.x += 2
                logo.y -= 1
            # If direction is top left
            elif logo.dir == 'tl':
                logo.x -= 2
                logo.y -= 1
        
        # Blit text to x and y coords on screen
        screen.blit(logo.text, (logo.x, logo.y))
        
        # Update display
        pygame.display.update()
        
        # fps
        clock.tick(len(logos) * 200)

pygame.quit()
