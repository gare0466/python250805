import pygame
import random
#pip install pygame
# 게임 설정
WINDOW_WIDTH, WINDOW_HEIGHT = 300, 600
BLOCK_SIZE = 30
BOARD_WIDTH, BOARD_HEIGHT = WINDOW_WIDTH // BLOCK_SIZE, WINDOW_HEIGHT // BLOCK_SIZE

# 테트로미노 도형 정의
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]
COLORS = [
    (0, 255, 255), (255, 255, 0), (128, 0, 128),
    (0, 0, 255), (255, 165, 0), (0, 255, 0), (255, 0, 0)
]

def rotate(shape):
    return [ [ shape[y][x] for y in range(len(shape)) ] for x in range(len(shape[0])-1, -1, -1) ]

class Tetromino:
    def __init__(self):
        self.type = random.randint(0, len(SHAPES)-1)
        self.shape = SHAPES[self.type]
        self.color = COLORS[self.type]
        self.x = BOARD_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = rotate(self.shape)

class Board:
    def __init__(self):
        self.grid = [[(0,0,0) for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

    def valid(self, tetromino, dx=0, dy=0):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    nx, ny = tetromino.x + x + dx, tetromino.y + y + dy
                    if nx < 0 or nx >= BOARD_WIDTH or ny >= BOARD_HEIGHT:
                        return False
                    if ny >= 0 and self.grid[ny][nx] != (0,0,0):
                        return False
        return True

    def place(self, tetromino):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    nx, ny = tetromino.x + x, tetromino.y + y
                    if ny >= 0:
                        self.grid[ny][nx] = tetromino.color

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(c == (0,0,0) for c in row)]
        lines_cleared = BOARD_HEIGHT - len(new_grid)
        for _ in range(lines_cleared):
            new_grid.insert(0, [(0,0,0)] * BOARD_WIDTH)
        self.grid = new_grid
        return lines_cleared

def draw_board(screen, board, tetromino):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            color = board.grid[y][x]
            pygame.draw.rect(screen, color, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
            pygame.draw.rect(screen, (50,50,50), (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                nx, ny = tetromino.x + x, tetromino.y + y
                if ny >= 0:
                    pygame.draw.rect(screen, tetromino.color, (nx*BLOCK_SIZE, ny*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
                    pygame.draw.rect(screen, (255,255,255), (nx*BLOCK_SIZE, ny*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    board = Board()
    tetromino = Tetromino()
    fall_time = 0
    fall_speed = 500
    running = True

    while running:
        dt = clock.tick(60)
        fall_time += dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if board.valid(tetromino, dx=-1):
                        tetromino.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if board.valid(tetromino, dx=1):
                        tetromino.x += 1
                elif event.key == pygame.K_DOWN:
                    if board.valid(tetromino, dy=1):
                        tetromino.y += 1
                elif event.key == pygame.K_UP:
                    old_shape = tetromino.shape
                    tetromino.rotate()
                    if not board.valid(tetromino):
                        tetromino.shape = old_shape

        if fall_time > fall_speed:
            if board.valid(tetromino, dy=1):
                tetromino.y += 1
            else:
                board.place(tetromino)
                board.clear_lines()
                tetromino = Tetromino()
                if not board.valid(tetromino):
                    running = False
            fall_time = 0

        screen.fill((0,0,0))
        draw_board(screen, board, tetromino)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

