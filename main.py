from PyQt5 import QtWidgets,QtGui
import sys,re
from decimal import Decimal
import numpy as np

C = 0
C_a = ''
R = 0
R_a = ''
L = 0
L_a = ''
V = 0
V_a = ''

def check():
    buf = ""
    buf2 = ""
    R = input1.text()
    C = input2.text()
    L = input3.text()
    V = input4.text()
    R_a = box1.currentText()
    C_a = box2.currentText()
    L_a = box3.currentText()
    V_a = box4.currentText()
    p = Decimal(10)**Decimal('-12')
    n = Decimal(10)**Decimal('-9')
    u = Decimal(10)**Decimal('-6')
    m = Decimal(10)**Decimal('-3')
    match R_a:
        case "mΩ":
            buf = buf + R + "mΩ" + "  "
            buf2 = buf2 + format(Decimal(R)*m,'.3f') + ","
        case "Ω":
            buf = buf + R + "Ω" + "  "
            buf2 = buf2 + R + ","
        case "kΩ":
            buf = buf + R + "kΩ" + "  "   
            buf2 = buf2 + str(int(R)*pow(10,3)) + ","
        case "MΩ":
            buf = buf + R + "MΩ" + "  "
            buf2 = buf2 + str(int(R)*pow(10,6)) + ","
    match C_a:
        case "pF":
            buf = buf + C + "pF" + "  "
            buf2 = buf2 + format(Decimal(C)*p, '.12f') + ","
        case "nF":
            buf = buf + C + "nF" + "  "
            buf2 = buf2 + format(Decimal(C)*n, '.9f') + ","
        case "μF":
            buf = buf + C + "μF" + "  "
            buf2 = buf2 + format(Decimal(C)*u, '.6f') + ","
        case "mF":
            buf = buf + C + "mF" + "  "
            buf2 = buf2 + format(Decimal(C)*m, '.3f') + ","
        case "F":
            buf = buf + C + "F" + "  "
            buf2 = buf2 + C + ","
    match L_a:
        case "nH":
            buf = buf + L + "nH" + "  "
            buf2 = buf2 + format(Decimal(L)*n, '.9f') + ","
        case "μH":
            buf = buf + L + "μH" + "  "
            buf2 = buf2 + format(Decimal(L)*u, '.6f') + ","
        case "mH":
            buf = buf + L + "mH" + "  "
            buf2 = buf2 + format(Decimal(L)*m, '.3f') + ","
        case "H":
            buf = buf + L + "H" + "  "
            buf2 = buf2 + L + ","
    match V_a:
        case "mV":
            buf = buf + V + "mV" 
            buf2 = buf2 + format(Decimal(V)*m, '.3f')
        case "V":
            buf = buf + V + "V" 
            buf2 = buf2 + V
        case "kV":
            buf = buf + V + "kV" 
            buf2 = buf2 + str(float(V)*pow(10,3))

    mbox = QtWidgets.QMessageBox(From)
    mbox.setText("確認以下規格:\n"+buf)
    mbox.addButton("確定",0)
    mbox.setDefaultButton(mbox.addButton("取消",1))
    ret = mbox.exec()
    if ret == 0:
        print(buf2)
        file = open("setting.cfg",'w',encoding='utf-8')
        file.write(buf2)
        file.flush()
        file.close()

def all_number(s):
    return bool(re.match(r'^\d+$',s))

def check2():
    R = input1.text()
    C = input2.text()
    L = input3.text()
    V = input4.text()
    if all_number(R) and all_number(C) and all_number(L) and all_number(V):
        button1.setDisabled(False)
    else:
        button1.setDisabled(True)

width = 600
height = 400

app = QtWidgets.QApplication(sys.argv)

From = QtWidgets.QWidget()
From.setWindowTitle("Test")
From.setFixedSize(width,height)

#字
Label_font = QtGui.QFont()
Label_font.setPointSize(15)

Label1 = QtWidgets.QLabel(From)
Label2 = QtWidgets.QLabel(From)
Label3 = QtWidgets.QLabel(From)
Label4 = QtWidgets.QLabel(From)

Label1.setGeometry(55,int(height/2)-50,100,50)
Label1.setFont(Label_font)
Label1.setText("電阻(R)")


Label2.setGeometry(185,int(height/2)-50,100,50)
Label2.setFont(Label_font)
Label2.setText("電容(C)")

Label3.setGeometry(345,int(height/2)-50,100,50)
Label3.setFont(Label_font)
Label3.setText("電感(L)")

Label4.setGeometry(465,int(height/2)-50,100,50)
Label4.setFont(Label_font)
Label4.setText("電壓(V)")


#輸入欄
input1 = QtWidgets.QLineEdit(From)
input1.setGeometry(35,int(height/2),100,20)

input2 = QtWidgets.QLineEdit(From)
input2.setGeometry(170,int(height/2),100,20)

input3 = QtWidgets.QLineEdit(From)
input3.setGeometry(330,int(height/2),100,20)

input4 = QtWidgets.QLineEdit(From)
input4.setGeometry(450,int(height/2),100,20)

input1.textChanged.connect(check2)
input2.textChanged.connect(check2)
input3.textChanged.connect(check2)
input4.textChanged.connect(check2)

output1 = QtWidgets.QLineEdit(From)
output1.setGeometry(int(width/2)-90,100,200,20)
output1.setReadOnly(True)


#下拉欄
box1 = QtWidgets.QComboBox(From)
box2 = QtWidgets.QComboBox(From)
box3 = QtWidgets.QComboBox(From)
box4 = QtWidgets.QComboBox(From)

box1.addItems(["mΩ","Ω","kΩ","MΩ"])
box2.addItems(["pF","nF","μF","mF","F"])
box3.addItems(["nH","μH","mH","H"])
box4.addItems(["mV","V","kV"])


box1.setGeometry(35,int(height/2)+35,100,20)
box2.setGeometry(170,int(height/2)+35,100,20)
box3.setGeometry(330,int(height/2)+35,100,20)
box4.setGeometry(450,int(height/2)+35,100,20)


#按鈕

button1 = QtWidgets.QPushButton(From)
button1.setGeometry(int(width/2)-100,int(height/2)+100,200,40)
button1.setText("模擬")
button1.setDisabled(True)
button1.setStyleSheet('''
    QPushButton{
        font-size:20px;
        color: #f00;
        background: #ff0;
        border: 2px solid #000;
    }
    QPushButton:hover {
        color: #ff0;
        background: #f00;
    }
    QPushButton:disabled{
        color:  #a9a9a9;
        background: #dcdcdc;       
    }
''')

button1.clicked.connect(check)
From.show()
sys.exit(app.exec_())

