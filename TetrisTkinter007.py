# https://github.com/BigShuang/Tetris
import tkinter as tk
import time
import random
# ---------------------------------------------------
# GLOBALS VARS  全局常量
s_width = 800  # 游戏窗体总宽度
s_height = 700  # 游戏窗体总高度
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
C = 10
R = 20
block_size = 30
# 方块出现区域的左上原点的x,y坐标
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# 全局变量-----------------------------
# 键盘按键消息
event_key = "NOKEY"
# scores 游戏得分
scores = 0
# grid
# grid = {}

# SHAPE FORMATS
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255),
                (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3


def left_block(event):
    # 向左移动俄罗斯方块
    global event_key
    event_key = "LEFT"


def right_block(event):
    # 向右移动俄罗斯方块
    global event_key
    event_key = "RIGHT"


def down_block(event):
    # 向下移动俄罗斯方块
    global event_key
    event_key = "DOWN"

def rotate_block(event):
    # 旋转移动俄罗斯方块
    global event_key
    event_key = "UP"


def land_block(event):
    # 降落移动俄罗斯方块
    global event_key
    event_key = "SPACE"


def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    # 根据每个方块的旋转方向，其中一个形状
    format = shape.shape[shape.rotation % len(shape.shape)]
    # print(shape.shape)
    # print(format)
    for i, line in enumerate(format):
        # print(line)
        # line 为形状的每一行，row将line.00..转化成列表形式['.', '0', '0', '.', '.']
        row = list(line)
        # print(row)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    # print(positions)    # [(7, 1), (6, 2), (7, 2), (8, 2)]
    # 将位置坐标的x坐标减2，y坐标减4，这样保证初始值在游戏框外，并且在中间
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    # print(positions)    # [(5, -3), (4, -2), (5, -2), (6, -2)]
    return positions


def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(
        10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False

    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    global shapes, shape_colors

    return Piece(5, 0, random.choice(shapes))


def color(value):
    digit = list(map(str, range(10))) + list("ABCDEF")
    if isinstance(value, tuple):
        string = '#'
        for i in value:
            a1 = i // 16
            a2 = i % 16
            string += digit[a1] + digit[a2]
        return string
    elif isinstance(value, str):
        a1 = digit.index(value[1]) * 16 + digit.index(value[2])
        a2 = digit.index(value[3]) * 16 + digit.index(value[4])
        a3 = digit.index(value[5]) * 16 + digit.index(value[6])
        return (a1, a2, a3)


def clear_rows(grid, locked):
    # need to see if row is clear the shift every other row above down one
    global scores
    inc = 0
    ind = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                    scores += inc
                except:
                    continue
    if inc > 0:
        # sound_clear.play()
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)


def draw_next_shape(shape, surface):
    # font = pygame.font.SysFont('comicsans', 30)
    # label = font.render('Next Shape', 1, (255, 255, 255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                canvas.create_rectangle(sx + j*30,  sy + i*30, sx + (j+1)*30, sy + (
                    i+1)*30, fill=color(shape.color), outline="gray", width=1)


def draw_window(win):
    # print("sdfsdf")
    # 绘制空白游戏面板网格
    canvas.delete("all")
    # 画出游戏格子中所有小方块，线宽0表示用颜色填充内部，填充颜色为grid[i][j]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            canvas.create_rectangle(top_left_x + j * block_size, top_left_y + i * block_size, top_left_x + (
                j+1) * block_size, top_left_y + (i+1) * block_size, fill=color(grid[i][j]), outline="gray", width=1)

    # 绘制游戏面板外框
    canvas.create_rectangle(top_left_x, top_left_y, top_left_x +
                            C * block_size, top_left_y+R * block_size, outline="#ff6400", width=5)


# 游戏主循环
def main():
    global grid
    global event_key

    # (x,y):(255,0,0) 记录累积的每个小方格的颜色，格式如：{(5, 16): (0, 255, 255), (5, 17): (0, 255, 255), (5, 18): (0, 255, 255), (5, 19): (0, 255, 255)}
    locked_positions = {}
    # grid 记录每个格子的颜色值(0,0,0),每行10组，共20行
    grid = create_grid(locked_positions)
    # print(grid)
    change_piece = False
    run = True
    current_piece = get_shape()  # 返回一个随机的具体的对象
    # print(current_piece.shape)
    next_piece = get_shape()

    fall_speed = 0.2   # 控制方块下降的速度0.2秒
    fall_time = 0   # 方块下落计时
    last_time = time.perf_counter()

    while run:

        now_time = time.perf_counter()
        fall_time = fall_time+now_time-last_time
        last_time = now_time

        grid = create_grid(locked_positions)

        if fall_time >= fall_speed:    # 当循环时间大于设定的下降速度

            fall_time = 0

            current_piece.y += 1    # 让当前的方块的坐标y+1，就是下降一步
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        # print(event_key)
        if event_key == "LEFT":
            # move shape down

            current_piece.x -= 1
            if not valid_space(current_piece, grid):
                current_piece.x += 1

        if event_key == "RIGHT":

            current_piece.x += 1
            if not valid_space(current_piece, grid):
                current_piece.x -= 1

        if event_key == "UP":
            current_piece.rotation = current_piece.rotation + \
                1 % len(current_piece.shape)
            if not valid_space(current_piece, grid):
                current_piece.rotation = current_piece.rotation - \
                    1 % len(current_piece.shape)

        if event_key == "DOWN":
            current_piece.y += 1
            if not valid_space(current_piece, grid):
                current_piece.y -= 1

        if event_key == "SPACE":
            while valid_space(current_piece, grid):
                current_piece.y += 1
            current_piece.y -= 1

        event_key = "NOKEY"

        # 返回当前方块的各个小块的坐标值，如：[(5, -4), (5, -3), (5, -2), (5, -1)]
        # 初始值：各个小块的y坐标的最小值为-1
        shape_pos = convert_shape_format(current_piece)

        # print(shape_pos)
        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                # print(pos)
                print(p)
                locked_positions[p] = current_piece.color
            print(locked_positions)
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

            # call four times to check for multiple clear rows
            clear_rows(grid, locked_positions)

        # 将所有单元格按照grid[i][j]的颜色值，重新绘制一遍
        draw_window(win)

        # 绘制下一个方块
        draw_next_shape(next_piece, win)

        # 显示游戏得分
        canvas.create_text(400, 60, text='SCORES:'+str(scores),
                           fill='white', font=('Courier', 32))

        win.update()

        # 判断游戏是否结束
        if check_lost(locked_positions):
            run = False


# ===========================================================================
# ===========================================================================
# 建立窗体
win = tk.Tk()
canvas = tk.Canvas(win, width=s_width, height=s_height, background="#000000")
canvas.pack()

# draw_blank_board(canvas)
# win.update()
# canvas.create_text(400, 60, text="SCORES:0",
#                    fill='white', font=('Courier', 32))
win.title("Tetris")


canvas.focus_set()  # 聚焦到canvas画板对象上
canvas.bind("<KeyPress-Left>", left_block)    # 方向左键按下，向左移动方块一步
canvas.bind("<KeyPress-Right>", right_block)    # 方向右键按下，向右移动方块一步
canvas.bind("<KeyPress-Up>", rotate_block)
canvas.bind("<KeyPress-Down>", down_block)
canvas.bind("<KeyPress-space>", land_block)

# 游戏主程序开始
main()  # start game

# 游戏最后一行，保持窗体持续运行中
win.mainloop()
