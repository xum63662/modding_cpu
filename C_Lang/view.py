import matplotlib.pyplot as plt
from matplotlib.backend_bases import FigureCanvasBase
from PyQt5.QtWidgets import QApplication,QDesktopWidget
import numpy as np
import os,sys,math
from decimal import Decimal,ROUND_CEILING

app = QApplication(sys.argv)

def on_clse(event):
    print("已關閉視窗")
    sys.exit(app.exec_())




screen = QDesktopWidget().screenGeometry()

screen_width = screen.width()
screen_height = screen.height()

window_width = screen_width // 2
window_height = screen_height // 2

偏移 = 20

plt.rcParams['font.sans-serif'] = ['STFangsong']
plt.rcParams['axes.unicode_minus'] = False


plt.ion()
plt.switch_backend("Qt5Agg")

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
L1,L2 = 1,1

fig1,ax1 = plt.subplots()
ax1.set_title("RC充電")
fig2,ax2 = plt.subplots()
ax2.set_title("RC放電")

manager1 = fig1.canvas.manager
manager1.window.setGeometry(0, 0+偏移, window_width-2, window_height-偏移)
manager2 = fig2.canvas.manager
manager2.window.setGeometry(screen_width - window_width, 0+偏移, window_width, window_height-偏移)

canvas1 = fig1.canvas
canvas1.mpl_connect("close_event",on_clse)
canvas2 = fig2.canvas
canvas2.mpl_connect("close_event",on_clse)

raw_line1 = f1.readlines()
raw_line2 = f2.readlines()
f1.close()
f2.close()


temp_char = raw_line1[len(raw_line1)-1].split(',')
temp_float = Decimal(temp_char[0])
if Decimal('1000') >= temp_float or temp_float > Decimal('1'):
    L1 = Decimal('1') ** Decimal('-3')
    ax1.set_xlabel("Time(s)/1000")
if Decimal('1') >= temp_float or temp_float > Decimal('0.001'):
    L1 = Decimal('10') ** Decimal('0')
    ax1.set_xlabel("Time(s)")
if Decimal('0.001') >= temp_float or temp_float > Decimal('0.000001'):
    L1 = Decimal('10') ** Decimal('3')
    ax1.set_xlabel("Time(ms)")
if Decimal('0.000001') >= temp_float or temp_float > Decimal('0.000000001'):
    L1 = Decimal('10') ** Decimal('6')
    ax1.set_xlabel("Time(μs)")

temp_char = raw_line2[0].split(',')
temp_float = Decimal(temp_char[0])
if Decimal('1000') >= temp_float or temp_float > Decimal('1'):
    L2 = Decimal('1') ** Decimal('-3')
    ax2.set_xlabel("Time(s)/1000")
if Decimal('1') >= temp_float or temp_float > Decimal('0.001'):
    L2 = Decimal('10') ** Decimal('0')
    ax2.set_xlabel("Time(s)")
if Decimal('0.001') >= temp_float or temp_float > Decimal('0.000001'):
    L2 = Decimal('10') ** Decimal('3')
    ax2.set_xlabel("Time(ms)")
if Decimal('0.000001') >= temp_float or temp_float > Decimal('0.000000001'):
    L2 = Decimal('10') ** Decimal('6')
    ax2.set_xlabel("Time(μs)")

for i in raw_line1:
    arr = i.split(',')
    x1.append(float(Decimal(arr[0]) * L1))
    temp = float(arr[1].replace('\n',''))
    y1.append(temp)
    if(len(y1)>2):
        if(y1[len(y1)-2] == temp and RC_up_point == 0):
            RC_ax_up_point, = ax1.plot([x1[len(x1)-2]],[temp],'go',label="充電最高點")
            RC_ax_line_up, = ax1.plot([x1[len(x1)-2],x1[len(x1)-2]],[0,temp],'k--',lw=1)
            RC_up_point+=1        
for i in raw_line2:
    arr = i.split(',')
    x2.append(float(Decimal(arr[0]) * L2))
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
ax1.set_yticks(np.linspace(0,math.ceil(y1[len(y1)-1]),math.ceil(y1[len(y1)-1])+1))
ax1.set_xticks(np.linspace(0,int(Decimal(x1[len(x1)-1]).quantize(Decimal('1'),rounding=ROUND_CEILING)),15))
ax2.set_yticks(np.linspace(0,math.ceil(y2[0]),math.ceil(y1[len(y1)-1])+1))
ax2.set_xticks(np.linspace(0,int(Decimal(x2[len(x2)-1]).quantize(Decimal('1'), rounding=ROUND_CEILING)),15))
ax1.set_ylim(0,y1[len(y1)-1]+0.3)
ax2.set_ylim(-0.3,y1[len(y1)-1]+0.3)
ax1.set_xlim(0,int(Decimal(x1[len(x1)-1]).quantize(Decimal('1'),rounding=ROUND_CEILING)))
ax2.set_xlim(0,int(Decimal(x2[len(x2)-1]).quantize(Decimal('1'), rounding=ROUND_CEILING)))
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
    temp_char = raw_line1[len(raw_line1)-1].split(',')
    temp_float = Decimal(temp_char[0])
    if Decimal('1000') >= temp_float or temp_float > Decimal('1'):
        L1 = Decimal('1') ** Decimal('-3')
        ax1.set_xlabel("Time(s)/1000")
    if Decimal('1') >= temp_float or temp_float > Decimal('0.001'):
        L1 = Decimal('10') ** Decimal('0')
        ax1.set_xlabel("Time(s)")
    if Decimal('0.001') >= temp_float or temp_float > Decimal('0.000001'):
        L1 = Decimal('10') ** Decimal('3')
        ax1.set_xlabel("Time(ms)")
    if Decimal('0.000001') >= temp_float or temp_float > Decimal('0.000000001'):
        L1 = Decimal('10') ** Decimal('6')
        ax1.set_xlabel("Time(μs)")

    temp_char = raw_line2[0].split(',')
    temp_float = Decimal(temp_char[0])
    if Decimal('1000') >= temp_float or temp_float > Decimal('1'):
        L2 = Decimal('1') ** Decimal('-3')
        ax2.set_xlabel("Time(s)/1000")
    if Decimal('1') >= temp_float or temp_float > Decimal('0.001'):
        L2 = Decimal('10') ** Decimal('0')
        ax2.set_xlabel("Time(s)")
    if Decimal('0.001') >= temp_float or temp_float > Decimal('0.000001'):
        L2 = Decimal('10') ** Decimal('3')
        ax2.set_xlabel("Time(ms)")
    if Decimal('0.000001') >= temp_float or temp_float > Decimal('0.000000001'):
        L2 = Decimal('10') ** Decimal('6')
        ax2.set_xlabel("Time(μs)")


    for i in raw_line1:
        arr = i.split(',')
        x1.append(float(Decimal(arr[0]) * L1))
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
        x2.append(float(Decimal(arr[0]) * L2))
        temp = float(arr[1].replace('\n',''))
        y2.append(temp)
        if(len(y2)>2):
            if(y2[len(y2)-2] == temp and RC_down_point == 0):
                RC_ax_down_point.set_xdata([x2[len(x2)-2]])
                RC_ax_down_point.set_ydata([temp])
                RC_ax_line_down.set_xdata([x2[len(x2)-2],x2[len(x2)-2]])
                RC_ax_line_down.set_ydata([-0.3,temp])
                RC_down_point+=1

    print(int(Decimal(x1[len(x1)-1]).quantize(Decimal('1'),rounding=ROUND_CEILING)))
    graph1.set_ydata(y1)
    graph2.set_ydata(y2)
    ax1.set_yticks(np.linspace(0,math.ceil(y1[len(y1)-1]),math.ceil(y1[len(y1)-1])+1))
    ax1.set_xticks(np.linspace(0,int(Decimal(x1[len(x1)-1]).quantize(Decimal('1'),rounding=ROUND_CEILING)),15))
    ax2.set_yticks(np.linspace(0,math.ceil(y2[0]),math.ceil(y1[len(y1)-1])+1))
    ax2.set_xticks(np.linspace(0,int(Decimal(x2[len(x2)-1]).quantize(Decimal('1'), rounding=ROUND_CEILING)),15))
    ax1.set_ylim(0,y1[len(y1)-1]+0.3)
    ax2.set_ylim(-0.3,y1[len(y1)-1]+0.3)
    ax1.set_xlim(0,int(Decimal(x1[len(x1)-1]).quantize(Decimal('1'),rounding=ROUND_CEILING)))
    ax2.set_xlim(0,int(Decimal(x2[len(x2)-1]).quantize(Decimal('1'), rounding=ROUND_CEILING)))
    plt.draw()
    plt.pause(2)