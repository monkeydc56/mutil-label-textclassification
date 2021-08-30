import pandas as pd
import numpy as np
da = pd.read_excel(r"C:\Users\哈哈\PycharmProjects\datasets\aapd\metrix.csv",index_col=0)#共现矩阵文件的路径
tag = pd.read_csv(r"C:\Users\哈哈\PycharmProjects\datasets\aapd\datacsv.csv")#tag的csv文件路径
list = da.values.tolist()

def newPMI(tag,list):
    l = len(tag)
    for i in range(len(list)):
        conx = list[i][i]
        px = conx/l
        for j in range(len(list)):
            cony = list[j][j]
            py = cony/l
            con = list[i][j]
            pxy = con/l
            #print(con)
            if con != 0:
                pmi = (pxy / (px * py))
                list[i][j] = pmi
            else:
                list[i][j] = 0
    test = pd.DataFrame(data=list)
    test.to_csv(r"C:\Users\哈哈\PycharmProjects\datasets\aapd\newpmicsv1.csv")  # 保存计算好的PMI


c = newPMI(tag,list)


