import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

colors = [WHITE, RED, GREEN, BLUE]

BLOCKCOUNT = 20
ROWCOUNT = 4
SIZE_WIDTH = 800
SIZE_HEIGHT = 600
BLOCK_WIDTH = SIZE_WIDTH // BLOCKCOUNT - 2
BLOCK_HEIGHT = 15


class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.image = pygame.Surface([BLOCK_WIDTH, BLOCK_HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((RED))
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.x = 0
        self.rect.y = self.screenheight - self.height

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width

def main():
    pygame.init()
    screen = pygame.display.set_mode([SIZE_WIDTH, SIZE_HEIGHT])
    pygame.display.set_caption('Arcanoid 1.0')
    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    blocks = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()

    player = Player()
    allsprites.add(player)

    top = 80
    for row in range(ROWCOUNT):
        for column in range(0, BLOCKCOUNT):
            block = Block(colors[row % len(colors)], column * (BLOCK_WIDTH + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        top += BLOCK_HEIGHT + 2

    clock = pygame.time.Clock()

    exit_program = False

    # Main program loop
    while not exit_program:

        # Limit to 30 fps
        clock.tick(30)

        # Clear the screen
        screen.fill(BLACK)

        # Process the events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program = True

        player.update()

        allsprites.draw(screen)
        # Flip the screen and show what we've drawn
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()