import numpy as np
from transform import convert_to_float as cf

def calculate(df,i):
    # 常量和星历数据准备
    radv = 72921151467e-5
    GM = 3.986005e14
    F = -4.442807633e-10
    PRN = df['PRN'].iloc[i]
    toc = cf(df['toc'].iloc[i])
    a2 = cf(df['a2'].iloc[i])
    a1 = cf(df['a1'].iloc[i])
    a0 = cf(df['a0'].iloc[i])
    AODE = cf(df['AODE'].iloc[i])
    sqrtA = cf(df['sqrtA'].iloc[i])
    TOE = cf(df['TOE'].iloc[i])
    deltan = cf(df['deltan'].iloc[i])
    M0 = cf(df['M0'].iloc[i])
    e = cf(df['e'].iloc[i])
    i0 = cf(df['i0'].iloc[i])
    IDOT = cf(df['IDOT'].iloc[i])
    omega = cf(df['omega'].iloc[i])
    Cuc = cf(df['Cuc'].iloc[i])
    Cus = cf(df['Cus'].iloc[i])
    Crc = cf(df['Crc'].iloc[i])
    Crs = cf(df['Crs'].iloc[i])
    Cic = cf(df['Cic'].iloc[i])
    Cis = cf(df['Cis'].iloc[i])
    OMEGA = cf(df['OMEGA'].iloc[i])
    OMEGA_DOT = cf(df['OMEGA_DOT'].iloc[i])
    
    # 以toc时间作为t_ref的参考值
    t_ref = toc

    # 计算卫星位置
    delt = t_ref - toc
    sat_Clk_error = a2*delt**2 + a1*delt + a0 - AODE
    
    tk = t_ref - TOE
    
    # 计算平近点角
    a = sqrtA**2
    n = np.sqrt(GM/(a**3)) + deltan
    M = M0 + n*tk
    M = np.mod(M, 2*np.pi)
    
    # 计算偏近点角
    E0 = M
    while 1:
        E = M + e * np.sin(E0)
        delt_E = E - E0
        delt_E = np.mod(delt_E, 2*np.pi)
        if np.abs(delt_E) < 1e-12:
            break
        else:
            E0 = E
    E = np.mod(E, 2*np.pi)
    
    # 计算真近点角和升交点角距
    nu = np.arctan2(np.sqrt(1 - e**2) * np.sin(E), (np.cos(E) - e))
    phi = nu + omega
    phi = np.mod(phi, 2 * np.pi)
    
    # 计算摄动修正后的升交点角距、轨道半径、轨道倾角
    delt_u = Cuc * np.cos(2 * phi) + Cus * np.sin(2 * phi)
    delt_r = Crc * np.cos(2 * phi) + Crs * np.sin(2 * phi)
    delt_i = Cic * np.cos(2 * phi) + Cis * np.sin(2 * phi)
    u = phi + delt_u
    r = a * (1 - e * np.cos(E)) + delt_r
    i_1 = i0 + IDOT * tk + delt_i
    
    # 计算升交点赤经
    OMEGA = OMEGA + (OMEGA_DOT - radv) * tk - radv * TOE
    OMEGA = np.mod(OMEGA, 2 * np.pi)
    
    # 卫星坐标WGS-84
    positionX = np.cos(u) * r * np.cos(OMEGA) - np.sin(u) * r * np.cos(i_1) * np.sin(OMEGA)
    positionY = np.cos(u) * r * np.sin(OMEGA) + np.sin(u) * r * np.cos(i_1) * np.cos(OMEGA)
    positionZ = np.sin(u) * r * np.sin(i_1)

    # 计算卫星速度
    E_dot = n / (1 - e * np.cos(E))
    Vk_dot = (np.sqrt(1 - e**2) * E_dot) / (1 - e * np.cos(E))

    Uk_dot = 2 * Vk_dot * (Cus * np.cos(2 * phi) - Cuc * np.sin(2 * phi))
    Rk_dot = 2 * Vk_dot * (Crs * np.cos(2 * phi) - Crc * np.sin(2 * phi))
    Ik_dot = 2 * Vk_dot * (Cis * np.cos(2 * phi) - Cic * np.sin(2 * phi))

    U_dot = Vk_dot + Uk_dot
    R_dot = a * e * E_dot * np.sin(E) + Rk_dot
    I_dot = IDOT + Ik_dot

    OMEGA_DOT = OMEGA_DOT - radv

    x = R_dot * np.cos(u) - r * U_dot * np.sin(u)
    y = R_dot * np.sin(u) + r * U_dot * np.cos(u)

    Vx = -positionY * OMEGA_DOT - (y * np.cos(i_1) - positionZ * I_dot) * np.sin(OMEGA) + x * np.cos(OMEGA)
    Vy = positionX * OMEGA_DOT + (y * np.cos(i_1) - positionZ * I_dot) * np.cos(OMEGA) + x * np.sin(OMEGA)
    Vz = y * np.sin(i_1) + positionZ * I_dot * np.cos(i_1)

    # 计算卫星钟偏
    delt = t_ref - toc
    dtr = F * e * np.sqrt(a) * np.sin(E)
    sat_Clk_error = a2 * delt**2 + a1 * delt + a0  + dtr- AODE

    # 返回结果
    return [PRN, positionX , positionY, positionZ, Vx, Vy, Vz, sat_Clk_error]