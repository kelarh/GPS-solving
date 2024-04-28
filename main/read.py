import pandas as pd
from calculate import calculate as cl  
from split import split1

def read(a,b,c,d,n):
    with open(a,'r') as file:
        # 跳过前8行读取后面数据
        lines=file.readlines()[8:None]
    data=[]
    row=[]

    for line in lines:
        # 每行前三个字符为一个数据
        tit=line[0:3].strip()

        # 如果数据不是空，则添加进row
        if tit and not tit.isspace():
            row.append(tit)
            
        # 再令每19个字符作为一个数据
        for i in range(3,len(line),19):
            tit=line[i:i+19].strip()
            if tit and not tit.isspace():
                row.append(tit)
        # 储存够33列重新开始一行
        if len(row)==33:
            data.append(row)
            row=[]
    # 创建表头，代表各参数
    key =  ["PRN", "toc", "a0", "a1", "a2", "AODE", "Crs", "deltan", "M0", "Cuc", "e", "Cus", "sqrtA", "TOE", "Cic", "OMEGA", "Cis", "i0", "Crc", "omega", "OMEGA_DOT", "IDOT", "无效1", "无效2", "无效3", "无效4", "无效5", "TGD", "无效7", "无效8", "无效9", "无效10", "无效11"]
    df = pd.DataFrame(data,columns=key)
    df['toc'] = df['toc'].apply(split1)

    # 修改toc为周内秒形式
    
    # 输出为excel表格
    df.to_excel(b,index=False)
    print(df)

    # 创建一个储存return的列表
    row2 = []
    data2 =[]

    # 计算N文件中所有卫星位置
    for i in range(len(df["PRN"])):
        # 确保cl函数返回7个结果
        results = cl(df, i)

        data2.append(results)

    # 创建一个结果表格的表头
    key2 = ["PRN","positionX", "positionY", "positionZ", "Vx", "Vy", "Vz", "sat_Clk_error"]
    # 创建一个存储表格
    result = pd.DataFrame(data2,columns=key2)

    classify_result = result[result["PRN"].astype(int) == n]
    #输出为excel表格
    result.to_excel(c,index=False)
    classify_result.to_excel(d,index=False)
    print(result)