import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

plt.rcParams['font.sans-serif'] = ['STFangsong']
plt.rcParams['axes.unicode_minus'] = False


f1 = open("test.txt",'r')
f2 = open("test2.txt",'r')
x1 = []
y1 = []
x2 = []
y2 = []
raw_line1 = f1.readlines()
raw_line2 = f2.readlines()
f1.close()
f2.close()
for i in raw_line1:
    arr = i.split(',')
    x1.append(arr[0])
    y1.append(arr[1].replace('\n',''))
for i in raw_line2:
    arr = i.split(',')
    x2.append(arr[0])
    y2.append(arr[1].replace('\n',''))
f,ax = plt.subplots(1,2,sharex='row',sharey=False)

ax[0].plot(x1,y1)
ax[1].plot(x2,y2)


ax[1].xaxis.set_major_locator(MultipleLocator(4))
plt.ylim(45,0)
plt.show()

