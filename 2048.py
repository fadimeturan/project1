import pygame.display
import pygame

pygame.init()

FPS = 60
WIDTH, HEIGHT = 400, 400
ROWS = 4
COLS = 4
RECT_HEIGTH = HEIGHT // ROWS
RECT_WIGHT = WIDTH // COLS
OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)
FONT = pygame.font.SysFont("comicsans", 60, bold= True)
MOVE_VEL = 20
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIGHT
        self.y = row * RECT_HEIGTH

    def get_color(self):
        pass

    def draw(slef, window):
        pass

    def set_pos(self):
        pass
    
    def move(self, delta):
        pass

def draw_grid(window):

    for row in range(1, ROWS):
        y = row * RECT_HEIGTH
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    for col in range(1, COLS):
        x = col * RECT_WIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)


def draw(window):
    window.fill(BACKGROUND_COLOR)

    draw_grid(window)

    pygame.display.update()


def main(window):

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window)
    pygame.quit()

 
if __name__ == "__main__":
    main(WINDOW)

