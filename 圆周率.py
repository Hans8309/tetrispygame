# # 该代码使用 Madhava-Leibniz 公式来计算圆周率，该公式如下：

# # π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
# # 该公式将圆周率表示为一个无穷级数，可以通过对该级数进行有限项求和来计算圆周率的近似值。


# def pi(n):
#   """
#   使用 Madhava-Leibniz 公式计算圆周率

#   Args:
#     n: 迭代次数

#   Returns:
#     圆周率的近似值
#   """
#   pi = 0
#   for k in range(n):
#     pi += 1 / pow(16, k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
#   return pi

# # 计算 1000 次迭代的圆周率
# pi_value = pi(10)

# # 打印结果
# print(f"圆周率的近似值：{pi_value}")


import math
import time

def calculate_pi(n):
    pi = 0
    for k in range(n):
        pi += 4 * (-1)**k / (2 * k + 1)
    return pi

n = 10000000  # 迭代次数
start_time = time.time()
result = calculate_pi(n)
end_time = time.time()
elapsed = end_time - start_time
print(result)
# # 计算 1000000 次迭代的圆周率
pi_value = calculate_pi(1000000)
# # 打印结果
print(f"圆周率的近似值：{pi_value}")
print(f"运算时间：{elapsed} 秒")
# # 导入数学库以获取更精确的圆周率值
print(f"数学库中的圆周率值：{math.pi}")   



 

