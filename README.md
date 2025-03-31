# RC RL CPU 專題

這裡是放研究的東西
還沒整理好

這邊可以打進度(也沒什麼進度)

目前暫時把RC充放電用C寫出來了

 ### 寫C:

- [x] RC充電
- [x] RC放電
- [ ] RL充電
- [ ] RL放電

CPU:
目前沒有東西


view.py是可以把C產出來的兩個
    
    test.txt<--RC充電
    test2.txt<--RC放電

劃出圖表

目前可以顯示RC充電線,最高點
以及RC放電線，最低點

## 取值

| R  | C  | V  | L |
|:--:|:--:|:--:|:--:|
| 1kΩ | 47μ| 5V | 30mH|


* * *
筆記
===
### e(自然指數) = 2.71828

RC 充電
---



| Vc | VR | I | t |
|:--:|:--:|:--:|:--:|
|電容電壓|電阻電壓|電流|時間常數

$$t=RC$$

### **t = 0:**
$$Vc(0) = 0$$
$$VR(0) = V$$
$$I(0) = \frac{V}{R}$$
### **0<t<5t:**
$$Vc(t) = V\times(1-e^\frac{-t}{RC})$$
$$VR(t) = V\times e^\frac{-t}{RC}$$
$$I(t) = \frac{V}{R}\times e^\frac{-t}{RC}$$
### **t>=5t:**
$$Vc(5t) = V$$
$$VR(5t) = 0$$
$$I(5t)  = 0$$
    

## RC放電

### **t = 0:**
$$Vc(0) = V$$
$$VR(0) = -V$$
$$I(0)  = -\frac{V}{R}$$
    

### **0<t<5t:**
$$Vc(t) = V\times e^{\frac{-t}{RC}}$$
$$VR(t) = -V\times e^{\frac{-t}{RC}}$$
$$I(t) = -\frac{V}{R}\times e^{\frac{-t}{RC}}$$

### **t>=5t:**
$$Vc(5t) = 0$$
$$VR(5t) = 0$$
$$I(5t)  = 0$$
## RL充電



| VL | VR | I | t |
|:--:|:--:|:--:|:--:|
| 電感電壓 |電阻電壓|電流|時間常數|

$$t = \frac{L}{R}$$

### **t = 0:**
$$VL(0) = V$$
$$VR(0) = 0$$
$$I(0) = 0$$
### **0<t<5t:**
$$VL(t) = V\times e^{\frac{-t}{L/R}}$$
$$VR(t) = V\times(1-e^{\frac{-t}{L/R}})$$
$$I(t) = \frac{V}{R}\times(1-e^{\frac{-t}{L/R}})$$
### **t>=5t:**
$$VL(5t) = V \times e^{-5} \approx 0$$
$$VR(5t) = V \times (1-e^{-5}) \approx V$$
$$I(5t) = \frac{V}{R}\times(1-e^{-5})$$
## RL放電

### **t = 0:**
$$VL(0) = -V$$
$$VR(0) = V$$
$$I(0)  = \frac{V}{R}$$

### **0<t<5t:**
$$VL(t) = -V\times e^\frac{-t}{ L/R}$$ 
$$VR(t) = V\times e^\frac{-t}{ L/R}$$ 
$$I(t)  = \frac{V}{R}\times e^\frac{-t}{ L/R}$$
    
### **t>=5t:**
$$VL(5t) = 0$$
$$VR(5t) = 0$$
$$ I(5t) = 0 $$

