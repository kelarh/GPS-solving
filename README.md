# 功能介绍
基于python对GPS卫星广播星历，进行卫星位置及运动参数解算

## 首先使用NASA提供的GPS卫星广播星历，[点击这里](https://urs.earthdata.nasa.gov/)获取，并进行解读


以如下片段广播星历为例
![](7bb222a2f8996ac77bd67f1907df44b.png)
从第九行开始，为每颗卫星参数信息
(1,1)代表了卫星的PRN号，后(4*8)的参数意义：
![](4b6b18000944f0b1553206169a84f0e.png)

之后参数命名以上为参考(仅使用IDOT前21个参数)
## 实现方法
确保Python环境已经激活，然后运行以下命令来安装：

```bash
pip install pandas numpy matplotlib
```
运行[main.py](main\main.py)，生成卫星参数表格及解算数据：![](588901c82a92248df838642a87c11d5.png)![](94fd25eedfdfd76d6bfaf5564f2494b.png)

# 获取卫星坐标图
运行[orbit.py](main\orbit.py)，生成卫星坐标图：![](Figure.png)