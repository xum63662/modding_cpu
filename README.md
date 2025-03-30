這裡是放研究的東西
還沒整理好

這邊可以打進度(也沒什麼進度)

目前暫時把RC充放電用C寫出來了

view.py是可以把test.txt<--RC充電
              test2.txt<--RC放電
劃出圖表

R電阻取值=1k歐姆
C電容取值=47微法拉
V電壓取值=5伏特

----筆記---
RC 充電

^是成指數

e(自然指數) = 2.71828

t = R*C

t = 0:
    Vc(0)(電容電壓) = 0
    VR(0)(電阻電壓) = V
    I(0)(電容充電電流) = V/R
0<t<5t:
    Vc(t) = V*(1-e^-t/(R*C))
    VR(t) = V+e^-t/(R*C)
    I(t)  = (V/R)*(e^-t/(R*C))
t>=5t:
    Vc(5t) = V
    VR(5t) = 0
    I(5t)  = 0

RC放電

t = 0:
    Vc(0) = V
    VR(0) = -V
    I(0)  = -V/R

0<t<5t:
    Vc(t) = V*(e^-t/(R*C))
    VR(t) = -V*(e^-t/(R*C))
    I(t)  = -(V/R)*(e^t/(R*C))

t>=5t:
    Vc(5t) = 0
    VR(5t) = 0
    I(5t)  = 0


RL充電

t = L/R

t = 0:
    VL(0)(電感電壓) = V
    VR(0) = 0
    I(0)  = 0
0<t<5t:
    VL(t) = V*(e^-t/(L/R))
    VR(t) = V*(1-(e^-t/(L/R)))
    I(t)  = (V/R)*(1-(e^-t/(L/R)))
t>=5t:
    VL(5t) = V*(e^-5)
    VR(5t) = V*(1-e^-5)
    I(5t)  = (V/R)*(1-e^-5)

RL放電

t = 0:
    VL(0) = -V
    VR(0) = V
    I(0)  = V/R
0<t<5t:
    VL(t) = -V*(e^-t/(L/R))
    VR(t) = V*(e^-t/(L/R))
    I(t)  = (V/R)*(e^-t/(L/R))
t>=5t:
    VL(5t) = 0
    VR(5t) = 0
    I(5t)  = 0