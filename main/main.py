from read import read
from orbit import draw

filename = 'brdc2030.23n'
# 进行文件统一指向，便于批量操作
a = filename
b = f"{filename}.xlsx"
c = f'{filename}.result.xlsx'
d = f'{filename}.classify.result.xlsx'
n = 11

read(a,b,c,d,n)
# 提取后的单颗卫星坐标进行绘图
draw(d)