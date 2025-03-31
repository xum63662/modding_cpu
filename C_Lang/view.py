import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['STFangsong']
plt.rcParams['axes.unicode_minus'] = False


plt.ion()

RC_up_point = 0
RC_down_point = 0
RC_ax_up_point = None
RC_ax_down_point = None
RC_ax_line_up = None
RC_ax_line_down = None

f1 = open("test.txt",'r')
f2 = open("test2.txt",'r')
x1 = []
y1 = []
x2 = []
y2 = []

fig1,ax1 = plt.subplots()
fig2,ax2 = plt.subplots()

raw_line1 = f1.readlines()
raw_line2 = f2.readlines()
f1.close()
f2.close()
for i in raw_line1:
    arr = i.split(',')
    x1.append(float(arr[0]))
    temp = float(arr[1].replace('\n',''))
    y1.append(temp)
    if(len(y1)>2):
        if(y1[len(y1)-2] == temp and RC_up_point == 0):
            RC_ax_up_point, = ax1.plot([x1[len(x1)-2]],[temp],'go',label="充電最高點")
            RC_ax_line_up, = ax1.plot([x1[len(x1)-2],x1[len(x1)-2]],[0,temp],'k--',lw=1)
            RC_up_point+=1        
for i in raw_line2:
    arr = i.split(',')
    x2.append(float(arr[0]))
    temp = float(arr[1].replace('\n',''))
    y2.append(temp)
    if(len(y2)>2):
        if(y2[len(y2)-2] == temp and RC_down_point == 0):
            RC_ax_down_point, = ax2.plot([x2[len(x2)-2]],[temp],'bo',label="放電最低點")
            RC_ax_line_down, = ax2.plot([x2[len(x2)-2],x2[len(x2)-2]],[-0.3,temp],'k--',lw=1)
            RC_down_point+=1


graph1, = ax1.plot(x1,y1,color='red',label="RC充電線")
graph2, = ax2.plot(x2,y2,color='black',label="RC放電線")
ax1.set_title('RC充電')
ax2.set_title('RC放電')
ax1.legend(loc="lower right")
ax2.legend(loc="upper right")
graph1.set_ydata(y1)
graph2.set_ydata(y2)
ax1.set_yticks(np.linspace(0,y1[len(y1)-1],10))
ax1.set_xticks(np.linspace(0,x1[len(x1)-1],15))
ax2.set_yticks(np.linspace(0,y2[0],10))
ax2.set_xticks(np.linspace(0,x2[len(x2)-1],15))
ax1.set_ylim(0,y1[len(y1)-1]+0.3)
ax2.set_ylim(-0.3,y1[len(y1)-1]+0.3)
plt.draw()
plt.pause(2)


while(1):
    RC_up_point = 0
    RC_down_point = 0
    f1 = open("test.txt",'r')
    f2 = open("test2.txt",'r')
    x1.clear()
    y1.clear()
    x2.clear()
    y2.clear()
    raw_line1 = f1.readlines()
    raw_line2 = f2.readlines()
    f1.close()
    f2.close()
    for i in raw_line1:
        arr = i.split(',')
        x1.append(float(arr[0]))
        temp = float(arr[1].replace('\n',''))
        y1.append(temp)
        if(len(y1)>2):
            if(y1[len(y1)-2] == temp and RC_up_point == 0):
                RC_ax_up_point.set_xdata([x1[len(x1)-2]])
                RC_ax_up_point.set_ydata([temp])
                RC_ax_line_up.set_xdata([x1[len(x1)-2],x1[len(x1)-2]])
                RC_ax_line_up.set_ydata([0,temp])
                RC_up_point+=1        
    for i in raw_line2:
        arr = i.split(',')
        x2.append(float(arr[0]))
        temp = float(arr[1].replace('\n',''))
        y2.append(temp)
        if(len(y2)>2):
            if(y2[len(y2)-2] == temp and RC_down_point == 0):
                RC_ax_down_point.set_xdata([x2[len(x2)-2]])
                RC_ax_down_point.set_ydata([temp])
                RC_ax_line_down.set_xdata([x2[len(x2)-2],x2[len(x2)-2]])
                RC_ax_line_down.set_ydata([-0.3,temp])
                RC_down_point+=1

    graph1.set_ydata(y1)
    graph2.set_ydata(y2)
    ax1.set_yticks(np.linspace(0,y1[len(y1)-1],10))
    ax1.set_xticks(np.linspace(0,x1[len(x1)-1],15))
    ax2.set_yticks(np.linspace(0,y2[0],10))
    ax2.set_xticks(np.linspace(0,x2[len(x2)-1],15))
    ax1.set_ylim(0,y1[len(y1)-1]+0.3)
    ax2.set_ylim(-0.3,y1[len(y1)-1]+0.3)
    plt.draw()
    plt.pause(2)
    if not plt.fignum_exists(fig1.number) :
        os._exit(1)
    elif not plt.fignum_exists(fig2.number):
        os._exit(1)
