def split1(ab):
    # 使用空格分割字符串
    sp = ab.split()

    hours = int(sp[3])
    minutes = int(sp[4])
    
    # 计算总秒数
    result = hours * 3600 + minutes * 60 
    
    return int(result)
