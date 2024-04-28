import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw(file):
    # 读取坐标
    data = pd.read_excel(file)
    print(data.columns)
    # 创建三维坐标
    x = data['positionX']
    y = data['positionY']
    z = data['positionZ']

    fig = plt.figure()  
    ax = fig.add_subplot(111, projection='3d')  

    # 绘制散点图
    ax.scatter(x, y, z, c='b', marker='o', alpha=0.6)

    # 设置坐标轴标签
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    # 设置标题
    ax.set_title('satellite_orbit')
    plt.show()
