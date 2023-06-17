# https://github.com/BigShuang/Tetris
import tkinter as tk

# ---------------------------------------------------
# GLOBALS VARS
s_width = 800  # 游戏窗体总宽度
s_height = 700  # 游戏窗体总高度
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 30

# 方块出现区域的左上原点的x,y坐标
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height-3


cell_size = 30
C = 10
R = 20
height = R * cell_size
width = C * cell_size

FPS = 500  # 刷新页面的毫秒间隔


# 绘制单个方块
def draw_cell_by_cr(canvas, c, r, color="#000000"):
    """
    :param canvas: 画板，用于绘制一个方块的Canvas对象
    :param c: 方块所在列
    :param r: 方块所在行
    :param color: 方块颜色，默认为#000000，黑色
    :return:
    """
    x0 = c * cell_size+top_left_x
    y0 = r * cell_size+top_left_y
    x1 = x0 + cell_size
    y1 = y0 + cell_size
    canvas.create_rectangle(x0, y0, x1, y1, fill=color,
                            outline="gray", width=1)


# 绘制游戏网格空白面板
def draw_blank_board(canvas):

    # 绘制空白游戏面板网格
    for ri in range(R):
        for ci in range(C):
            draw_cell_by_cr(canvas, ci, ri, "#225511")
    # 绘制游戏空白面板外框
    canvas.create_rectangle(top_left_x, top_left_y, top_left_x +
                            width, top_left_y+height, outline="#ff6400", width=5)


# 建立窗体
win = tk.Tk()
canvas = tk.Canvas(win, width=s_width, height=s_height, background="#000000")
canvas.pack()

draw_blank_board(canvas)

canvas.create_text(400, 60, text="SCORES:0",
                   fill='white', font=('Courier', 32))
win.title("Tetris")



def left_block(event):
    """
    向左移动俄罗斯方块
    """
    print("left")


def right_block(event):
    """
    向右移动俄罗斯方块
    """
    print("right")


def down_block(event):
    """
    向下移动俄罗斯方块
    """
    print("down")


def rotate_block(event):
    """
    旋转移动俄罗斯方块
    """
    print("rotate")


def land_block(event):
    """
    降落移动俄罗斯方块
    """
    print("land")

# 游戏主循环


def game_loop():
    print("running...")
    win.update()
    win.after(FPS, game_loop)


canvas.focus_set()  # 聚焦到canvas画板对象上
canvas.bind("<KeyPress-Left>", left_block)
canvas.bind("<KeyPress-Right>", right_block)
canvas.bind("<KeyPress-Up>", rotate_block)
canvas.bind("<KeyPress-Down>", down_block)
canvas.bind("<KeyPress-space>", land_block)


win.update()
win.after(FPS, game_loop)  # 在FPS 毫秒后调用 game_loop方法


win.mainloop()
