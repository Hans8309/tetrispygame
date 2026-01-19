import pyautogui as pg
import time

# 获取屏幕尺寸
# 元组类型的返回值
screen_width, screen_height = pg.size()
# 获取屏幕宽高
print("屏幕宽度:", screen_width)
print("屏幕高度:", screen_height)
#移动鼠标到指定位置
#duration是指所用时间，默认是0.25  浮点型  单位是秒
pg.moveTo(100, 100, duration=1)
#移动鼠标到相对位置
pg.move(100, -100, duration=1)