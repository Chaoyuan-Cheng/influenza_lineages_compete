'''


'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from geopy.distance import geodesic
import math
from matplotlib.pyplot import MultipleLocator

# import data
f = pd.read_excel(r"C:\Users\40506\OneDrive\OneDrive_SYNC\发表论文\influenza_host_2019\data\plots.xlsx",header=0,sheet_name="fig1_all_with_lineage")


# var
time = f["time"]
lat = f["LAT"]
lon = f["LON"]
id = f["id"]
region = f["region"]
host = f["host"]
GD = f["GD"]
color= f["color"]

# set figure
fig,ax = plt.subplots(2,3,figsize=(9,6))  # 画布大小
fig.tight_layout()

oldest_time = min(time)

# Homo sapiens #################################
ax[0,0].set_title("A")
ax[0,0].set_xlabel("Year",fontsize=12)
ax[0,0].set_ylabel("Genetic distance",fontsize=12)
ax[0,0].set_xlim(int(oldest_time)-1, 2019)   # 设置x轴范围，使legend的点位于之外
ax[0,0].set_ylim(0,0.4)
ax[0,0].grid(alpha=0.3)
for i in range(len(time)):
    if host[i] == "Homo sapiens":
        try:
            x2 = time[i]
            y2 = GD[i]
            if region[i] == "Africa":
                ax[0,0].scatter(x2,y2,c = "peru",alpha = 0.7,marker=".")
            elif region[i] == "Central_Asia":
               ax[0,0].scatter(x2,y2,c = "orange",alpha = 0.7,marker=".")
            elif region[i] == "Europe":
               ax[0,0].scatter(x2,y2,c = "mediumspringgreen",alpha = 0.7,marker=".")
            elif region[i] == "North_America":
               ax[0,0].scatter(x2,y2,c = "blue",alpha = 0.7,marker=".")
            elif region[i] == "Northeast_Asia":
               ax[0,0].scatter(x2,y2,c = "red",alpha = 0.7,marker=".")
            elif region[i] == "Oceania":
               ax[0,0].scatter(x2,y2,c = "darkorchid",alpha = 0.7,marker=".")
            elif region[i] == "South_America":
               ax[0,0].scatter(x2,y2,c = "green",alpha = 0.7,marker=".")
            elif region[i] == "South_Asia":
               ax[0,0].scatter(x2,y2,c = "yellow",alpha = 0.7,marker=".")
            elif region[i] == "Southeast_Asia":
               ax[0,0].scatter(x2,y2,c = "cyan",alpha = 0.7,marker=".")
            elif region[i] == "Western_Asia":
               ax[0,0].scatter(x2,y2,c = "pink",alpha = 0.7,marker=".")

        except:
            pass

# Avian ##################################################
ax[0,1].set_title("B")
ax[0,1].set_xlabel("Year",fontsize=12)
ax[0,1].set_ylabel("Genetic distance",fontsize=12)
ax[0,1].set_xlim(int(oldest_time)-1, 2019)   # 设置x轴范围，使legend的点位于之外
ax[0,1].set_ylim(0,0.4)
ax[0,1].grid(alpha=0.3)
for i in range(len(time)):
    if host[i] == "swine":
        try:

            x2 = time[i]
            y2 = GD[i]

            if region[i] == "Africa":
                ax[0,1].scatter(x2,y2,c = "peru",alpha = 0.7,marker=".")
            elif region[i] == "Central_Asia":
                ax[0,1].scatter(x2,y2,c = "orange",alpha = 0.7,marker=".")
            elif region[i] == "Europe":
                ax[0,1].scatter(x2,y2,c = "mediumspringgreen",alpha = 0.7,marker=".")
            elif region[i] == "North_America":
                ax[0,1].scatter(x2,y2,c = "blue",alpha = 0.7,marker=".")
            elif region[i] == "Northeast_Asia":
                ax[0,1].scatter(x2,y2,c = "red",alpha = 0.7,marker=".")
            elif region[i] == "Oceania":
                ax[0,1].scatter(x2,y2,c = "darkorchid",alpha = 0.7,marker=".")
            elif region[i] == "South_America":
                ax[0,1].scatter(x2,y2,c = "green",alpha = 0.7,marker=".")
            elif region[i] == "South_Asia":
                ax[0,1].scatter(x2,y2,c = "yellow",alpha = 0.7,marker=".")
            elif region[i] == "Southeast_Asia":
                ax[0,1].scatter(x2,y2,c = "cyan",alpha = 0.7,marker=".")
            elif region[i] == "Western_Asia":
                ax[0,1].scatter(x2,y2,c = "pink",alpha = 0.7,marker=".")

        except:
            pass

# swine #################
ax[0,2].set_title("C")
ax[0,2].set_xlabel("Year",fontsize=12)
ax[0,2].set_ylabel("Genetic distance",fontsize=12)
ax[0,2].set_xlim(int(oldest_time)-1, 2019)   # 设置x轴范围，使legend的点位于之外
ax[0,2].set_ylim(0,0.4)
ax[0,2].grid(alpha=0.3)
for i in range(len(time)):
    if host[i] == "Avian":
        try:

            x2 = time[i]
            y2 = GD[i]

            if region[i] == "Africa":
                ax[0,2].scatter(x2,y2,c = "peru",alpha = 0.7,marker=".")
            elif region[i] == "Central_Asia":
                ax[0,2].scatter(x2,y2,c = "orange",alpha = 0.7,marker=".")
            elif region[i] == "Europe":
                ax[0,2].scatter(x2,y2,c = "mediumspringgreen",alpha = 0.7,marker=".")
            elif region[i] == "North_America":
                ax[0,2].scatter(x2,y2,c = "blue",alpha = 0.7,marker=".")
            elif region[i] == "Northeast_Asia":
                ax[0,2].scatter(x2,y2,c = "red",alpha = 0.7,marker=".")
            elif region[i] == "Oceania":
                ax[0,2].scatter(x2,y2,c = "darkorchid",alpha = 0.7,marker=".")
            elif region[i] == "South_America":
                ax[0,2].scatter(x2,y2,c = "green",alpha = 0.7,marker=".")
            elif region[i] == "South_Asia":
                ax[0,2].scatter(x2,y2,c = "yellow",alpha = 0.7,marker=".")
            elif region[i] == "Southeast_Asia":
                ax[0,2].scatter(x2,y2,c = "cyan",alpha = 0.7,marker=".")
            elif region[i] == "Western_Asia":
                ax[0,2].scatter(x2,y2,c = "pink",alpha = 0.7,marker=".")

        except:
            pass

# others ################################################################################################################
# All samples #################################
ax[1,0].set_title("D")
ax[1,0].set_xlabel("Year",fontsize=12)
ax[1,0].set_ylabel("Genetic distance",fontsize=12)
ax[1,0].set_xlim(int(oldest_time)-1, 2019)   # 设置x轴范围，使legend的点位于之外
ax[1,0].set_ylim(0,0.4)
ax[1,0].grid(alpha=0.3)

for i in range(len(time)):
    try:
        x = time[i]
        y = GD[i]
        print(x,y)
        if color[i] == "grey":
            ax[1,0].scatter(x,y,c="%s"%color[i],marker=".",alpha=0.3)
        else:
            ax[1,0].scatter(x,y,c="%s"%color[i],marker=".",alpha=0.7)

    except:
        pass

plt.show()

