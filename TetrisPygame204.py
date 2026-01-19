import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# 定义屏幕大小
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# 定义游戏区域大小
PLAY_WIDTH = 10  # 10 列
PLAY_HEIGHT = 20  # 20 行

# 初始化屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("俄罗斯方块")

# 加载音效
pygame.mixer.init()
background_music = pygame.mixer.Sound("background.mp3")  # 背景音乐
move_sound = pygame.mixer.Sound("move.wav")  # 移动音效
rotate_sound = pygame.mixer.Sound("rotate.wav")  # 旋转音效
clear_sound = pygame.mixer.Sound("clear.wav")  # 消除行音效
drop_sound = pygame.mixer.Sound("drop.wav")  # 直接降到底音效
game_over_sound = pygame.mixer.Sound("game_over.wav")  # 游戏结束音效

# 播放背景音乐（循环播放）
background_music.play(-1)

# 定义方块形状
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
]

# 定义方块颜色
SHAPE_COLORS = [CYAN, MAGENTA, YELLOW, GREEN, RED, BLUE, ORANGE]

# 创建游戏区域
def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(PLAY_WIDTH)] for _ in range(PLAY_HEIGHT)]
    for y in range(PLAY_HEIGHT):
        for x in range(PLAY_WIDTH):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

# 绘制游戏区域
def draw_grid(surface, grid):
    for y in range(PLAY_HEIGHT):
        for x in range(PLAY_WIDTH):
            pygame.draw.rect(surface, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    for y in range(PLAY_HEIGHT):
        pygame.draw.line(surface, WHITE, (0, y * BLOCK_SIZE), (SCREEN_WIDTH, y * BLOCK_SIZE))
    for x in range(PLAY_WIDTH):
        pygame.draw.line(surface, WHITE, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, SCREEN_HEIGHT))

# 创建方块
def create_shape():
    shape = random.choice(SHAPES)
    color = random.choice(SHAPE_COLORS)
    return {'shape': shape, 'color': color, 'x': PLAY_WIDTH // 2 - len(shape[0]) // 2, 'y': 0}

# 绘制方块
def draw_shape(surface, shape):
    for y, row in enumerate(shape['shape']):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(surface, shape['color'], ((shape['x'] + x) * BLOCK_SIZE, (shape['y'] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

# 检查碰撞
def check_collision(shape, grid):
    for y, row in enumerate(shape['shape']):
        for x, cell in enumerate(row):
            if cell:
                if shape['y'] + y >= PLAY_HEIGHT or shape['x'] + x < 0 or shape['x'] + x >= PLAY_WIDTH or grid[shape['y'] + y][shape['x'] + x] != BLACK:
                    return True
    return False

# 锁定方块
def lock_shape(shape, grid, locked_positions):
    for y, row in enumerate(shape['shape']):
        for x, cell in enumerate(row):
            if cell:
                locked_positions[(shape['x'] + x, shape['y'] + y)] = shape['color']
    return locked_positions

# 清除满行
def clear_rows(grid, locked_positions):
    cleared_rows = 0
    for y in range(PLAY_HEIGHT - 1, -1, -1):
        if BLACK not in grid[y]:
            cleared_rows += 1
            del_row = y
            for x in range(PLAY_WIDTH):
                try:
                    del locked_positions[(x, del_row)]
                except:
                    continue
    if cleared_rows > 0:
        for key in sorted(list(locked_positions), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < del_row:
                new_key = (x, y + cleared_rows)
                locked_positions[new_key] = locked_positions.pop(key)
        clear_sound.play()  # 播放消除行音效
    return cleared_rows

# 直接降到底
def drop_shape(shape, grid):
    while not check_collision(shape, grid):
        shape['y'] += 1
    shape['y'] -= 1
    drop_sound.play()  # 播放降到底音效

# 显示游戏结束提示
def show_game_over():
    font = pygame.font.SysFont('comicsans', 50)
    text = font.render('Game Over!', True, RED)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    font = pygame.font.SysFont('comicsans', 30)
    restart_text = font.render('Press R to Restart', True, WHITE)
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.update()

# 重置游戏
def reset_game():
    locked_positions = {}
    grid = create_grid(locked_positions)
    current_shape = create_shape()
    next_shape = create_shape()
    fall_speed = 0.3
    return locked_positions, grid, current_shape, next_shape, fall_speed

# 主游戏循环
def main():
    locked_positions, grid, current_shape, next_shape, fall_speed = reset_game()
    clock = pygame.time.Clock()
    fall_time = 0
    running = True
    game_over = False

    while running:
        if not game_over:
            grid = create_grid(locked_positions)
            fall_time += clock.get_rawtime()
            clock.tick()

            if fall_time / 1000 >= fall_speed:
                fall_time = 0
                current_shape['y'] += 1
                if check_collision(current_shape, grid):
                    current_shape['y'] -= 1
                    locked_positions = lock_shape(current_shape, grid, locked_positions)
                    current_shape = next_shape
                    next_shape = create_shape()
                    if check_collision(current_shape, grid):
                        game_over = True
                        game_over_sound.play()  # 播放游戏结束音效

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_shape['x'] -= 1
                        if check_collision(current_shape, grid):
                            current_shape['x'] += 1
                        else:
                            move_sound.play()  # 播放移动音效
                    if event.key == pygame.K_RIGHT:
                        current_shape['x'] += 1
                        if check_collision(current_shape, grid):
                            current_shape['x'] -= 1
                        else:
                            move_sound.play()  # 播放移动音效
                    if event.key == pygame.K_DOWN:
                        current_shape['y'] += 1
                        if check_collision(current_shape, grid):
                            current_shape['y'] -= 1
                    if event.key == pygame.K_UP:
                        rotated_shape = list(zip(*current_shape['shape'][::-1]))
                        old_shape = current_shape['shape']
                        current_shape['shape'] = rotated_shape
                        if check_collision(current_shape, grid):
                            current_shape['shape'] = old_shape
                        else:
                            rotate_sound.play()  # 播放旋转音效
                    if event.key == pygame.K_SPACE:  # 按空格键直接降到底
                        drop_shape(current_shape, grid)
                        locked_positions = lock_shape(current_shape, grid, locked_positions)
                        current_shape = next_shape
                        next_shape = create_shape()
                        if check_collision(current_shape, grid):
                            game_over = True
                            game_over_sound.play()  # 播放游戏结束音效

            draw_grid(screen, grid)
            draw_shape(screen, current_shape)
            pygame.display.update()

            if clear_rows(grid, locked_positions):
                fall_speed *= 0.9
        else:
            show_game_over()  # 显示游戏结束提示
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # 按 R 键重新开始
                        locked_positions, grid, current_shape, next_shape, fall_speed = reset_game()
                        game_over = False

    pygame.quit()

if __name__ == '__main__':
    main()