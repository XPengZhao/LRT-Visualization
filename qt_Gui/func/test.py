import os
import json
import time
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
def loaddata():
    selfdata = {}
    datas = []
    files = os.listdir("../data/data1")  # 获得文件夹中所有文件的名称列表
    for file in files:
        path = "../data/data1/" + file
        with open(path) as f:
            load_dict = json.load(f)
            try:
                tag = selfdata[load_dict['tagid']]
            except:
                print(2)
                tag = []
            mid = list()
            try:
                timeArray = time.strptime(load_dict["Time"][0:19], "%Y-%m-%d %H:%M:%S")
                timeStamp = int(time.mktime(timeArray)+int(load_dict["Time"][20:24]))
            except:
                print(path)
                print(load_dict["Time"][20:23])
                break
            mid.append(timeStamp)
            mid.append(load_dict["Time"])
            mid.append(load_dict["tagid"])
            mid.append(load_dict["phase"])
            mid.append(load_dict["rss"])
            if "spectrum" in load_dict:
                mid.append(load_dict["spectrum"])
            else:
                mid.append(0)
            mid.append(load_dict["pos"])
            tag.append(mid)
            selfdata[load_dict['tagid']] = tag

    print(4)
    for tag in selfdata.keys():
        selfdata[tag] = pd.DataFrame(selfdata[tag], columns=["TimeStamp","Time", "tagid", "phase", "rss", "spectrum", "pos"])
        selfdata[tag].sort_values("TimeStamp", inplace=True)
    print(selfdata[1]["spectrum"])
    sp_data = pd.DataFrame(selfdata[1]["spectrum"])
    del datas, files
    return sp_data


if __name__ == '__main__':
    pre_data = loaddata()
    plt.figure()
    axes = plt.subplot(111)
    sns.set()
    sns.heatmap(pre_data, ax=axes, fmt=".3f", center=0.5, vmax=1, vmin=0, cmap="gray", annot=False)
    plt.show()
