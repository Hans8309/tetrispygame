# https://github.com/BigShuang/Tetris
import tkinter as tk

# ---------------------------------------------------
# GLOBALS VARS
s_width = 800 # 游戏窗体总宽度
s_height = 700 # 游戏窗体总高度
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 30

# 方块出现区域的左上原点的x,y坐标
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


cell_size = 30
C = 10
R = 20
height = R * cell_size
width = C * cell_size



# 绘制单个方块
def draw_cell_by_cr(canvas, c, r, color="#CCCCCC"):
    """
    :param canvas: 画板，用于绘制一个方块的Canvas对象
    :param c: 方块所在列
    :param r: 方块所在行
    :param color: 方块颜色，默认为#CCCCCC，轻灰色
    :return:
    """
    x0 = c * cell_size+top_left_x
    y0 = r * cell_size+top_left_y
    x1 = x0 + cell_size
    y1 = y0 + cell_size 
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="white", width=1)


# 绘制空白面板
def draw_blank_board(canvas):
    for ri in range(R):
        for ci in range(C):
            draw_cell_by_cr(canvas, ci, ri)




win = tk.Tk()
canvas = tk.Canvas(win, width=s_width, height=s_height, background="#005500")
canvas.pack()

draw_blank_board(canvas)

win.mainloop()

# win = pygame.display.set_mode((s_width, s_height))
# pygame.display.set_caption('Tetris')

# main_menu()  # start game

