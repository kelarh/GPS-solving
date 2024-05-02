import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def draw(file):
    # 读取坐标
    data = pd.read_excel(file)
    print(data.columns)
    # 创建三维坐标
    x = data['positionX']
    y = data['positionY']
    z = data['positionZ']


    # 创建球体的网格点，注意这里更改了变量名以避免冲突
    u_sphere = np.linspace(0, 2 * np.pi, 100)
    v_sphere = np.linspace(0, np.pi, 100)
    x_sphere = 6371000 * np.outer(np.cos(u_sphere), np.sin(v_sphere))
    y_sphere = 6371000 * np.outer(np.sin(u_sphere), np.sin(v_sphere))
    z_sphere = 6371000 * np.outer(np.ones(np.size(u_sphere)), np.cos(v_sphere))




    fig = plt.figure()  
    ax = fig.add_subplot(111, projection='3d')  

    # 绘制散点图
    ax.scatter(x, y, z, c='b', marker='o', alpha=0.6)

    # 绘制球体，使用新的变量名
    ax.plot_surface(x_sphere, y_sphere, z_sphere, color='#4ba1d7', alpha=0.7)



    # 设置坐标轴标签
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    # 设置标题
    ax.set_title('satellite_orbit')
    plt.show()
