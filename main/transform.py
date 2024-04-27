import numpy as np

# 由于python对于以D表示的科学计数法转化浮点数失效，故以此进行转化
def convert_to_float(s):
    if isinstance(s, np.integer):  # 检查是否为整数类型
        s = str(s)  # 转换为字符串
    return float(s.replace('D', 'e'))