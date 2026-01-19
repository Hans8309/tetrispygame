# test AI agent to code

import math

def inscribed_circle_radius(a, b, c):
    """
    计算三角形内切圆的半径，已知三条边长 a, b, c。
    
    参数:
    a, b, c (float): 三角形的三条边长，必须满足三角不等式。
    
    返回:
    float: 内切圆的半径，如果输入无效则返回 None。
    """
    # 检查是否能构成三角形
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        print("输入的边长不能构成三角形。")
        return None
    
    # 计算半周长
    s = (a + b + c) / 2
    
    # 计算面积（海伦公式）
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    # 计算内切圆半径
    r = area / s
    
    return r

# 示例使用
if __name__ == "__main__":
    # 示例：等边三角形，边长 3
    a, b, c = 3, 3, 3
    r = inscribed_circle_radius(a, b, c)
    if r is not None:
        print(f"等边三角形边长 {a} 的内切圆半径为: {r:.4f}")
    
    # 另一个示例：边长 3, 4, 5
    a, b, c = 3, 4, 5
    r = inscribed_circle_radius(a, b, c)
    if r is not None:
        print(f"边长 {a}, {b}, {c} 的三角形内切圆半径为: {r:.4f}")
