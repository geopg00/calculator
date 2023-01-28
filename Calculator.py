from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                QLabel, QHBoxLayout, QVBoxLayout)


style = """
    QWidget {
        background-color: rgb(15, 15, 15)
    }
    QLabel {
        color: black;
        font: bold 20px;
        background-color: rgb(190, 200, 175);
        border: 1px solid black;
        text-align: right;
    } 
    QPushButton {
        color: white;
        background-color: rgb(35, 35, 35);
        border: 1px solid rgb(0, 0, 0);
        padding: 5px;
        border-radius: 3px;
    }
    QPushButton:hover{
        background-color: rgb(20, 20, 20);
    }
    QPushButton#ravno:hover{
        background-color: rgb(20, 180, 20);
    }
    .QPushButton[level = "znak"] {
        background-color: rgb(20, 20, 20)
    }
    .QPushButton[level = "znak"]:hover {
        background-color: rgb(35, 35, 35)
    }

    
    """

#створення вікна
app = QApplication([])
window = QWidget()
window.resize(450, 400)
window.setWindowTitle("Калькулятор")
window.setStyleSheet(style)

#створення віджетів
lb_text = QLabel("")
lb_text.setAlignment(Qt.AlignCenter)
#lb_text.setStyleSheet("color: red")

btn_0 = QPushButton("0")
btn_1 = QPushButton("1")
btn_2 = QPushButton("2")
btn_3 = QPushButton("3")
btn_4 = QPushButton("4")
btn_5 = QPushButton("5")
btn_6 = QPushButton("6")
btn_7 = QPushButton("7")
btn_8 = QPushButton("8")
btn_9 = QPushButton("9")

btn_point = QPushButton(".")

btn_plus = QPushButton("+")
btn_minus = QPushButton("-")
btn_divide = QPushButton("/")
btn_multiply = QPushButton("x")

btn_root = QPushButton("√")
btn_degree = QPushButton("^")
btn_backspase = QPushButton("◄")
btn_AC = QPushButton("AC")
btn_AC.setObjectName("AC")
btn_result = QPushButton("=")
btn_result.setObjectName("ravno")

btn_plus.setProperty("level", "znak")
btn_minus.setProperty("level", "znak")
btn_divide.setProperty("level", "znak")
btn_multiply.setProperty("level", "znak")
btn_root.setProperty("level", "znak")
btn_degree.setProperty("level", "znak")
btn_backspase.setProperty("level", "znak")

#розташування віджетів
hline1 = QHBoxLayout()
hline1.addWidget(lb_text)

hline2 = QHBoxLayout()
hline2.addWidget(btn_AC)
hline2.addWidget(btn_backspase)
hline2.addWidget(btn_root)
hline2.addWidget(btn_multiply)

hline3 = QHBoxLayout()
hline3.addWidget(btn_9)
hline3.addWidget(btn_8)
hline3.addWidget(btn_7)
hline3.addWidget(btn_divide)

hline4 = QHBoxLayout()
hline4.addWidget(btn_6)
hline4.addWidget(btn_5)
hline4.addWidget(btn_4)
hline4.addWidget(btn_plus)

hline5 = QHBoxLayout()
hline5.addWidget(btn_3)
hline5.addWidget(btn_2)
hline5.addWidget(btn_1)
hline5.addWidget(btn_minus)

hline6 = QHBoxLayout()
hline6.addWidget(btn_point)
hline6.addWidget(btn_0)
hline6.addWidget(btn_degree)
hline6.addWidget(btn_result)

vline = QVBoxLayout()
vline.addLayout(hline1)
vline.addLayout(hline2)
vline.addLayout(hline3)
vline.addLayout(hline4)
vline.addLayout(hline5)
vline.addLayout(hline6)

window.setLayout(vline)

#обробка натискання на кнопки
def click_0():
    lb_text.setText(lb_text.text() + "0")

def click_1():
    lb_text.setText(lb_text.text() + "1")

def click_2():
    lb_text.setText(lb_text.text() + "2")

def click_3():
    lb_text.setText(lb_text.text() + "3")

def click_4():
    lb_text.setText(lb_text.text() + "4")

def click_5():
    lb_text.setText(lb_text.text() + "5")

def click_6():
    lb_text.setText(lb_text.text() + "6")

def click_7():
    lb_text.setText(lb_text.text() + "7")

def click_8():
    lb_text.setText(lb_text.text() + "8")

def click_9():
    lb_text.setText(lb_text.text() + "9")

def click_point():
    lb_text.setText(lb_text.text() + ".")


def click_plus():
    lb_text.setText(lb_text.text() + " + ")
def click_degree():
    lb_text.setText(lb_text.text() + " ^ ")
def click_root():
    lb_text.setText(lb_text.text() + " √ ")
def click_AC():
    lb_text.setText("")
def click_minus():
    lb_text.setText(lb_text.text() + " - ")
def click_backspase():
    lb_text.setText(lb_text.text()[0 : -1])
def click_divide():
    lb_text.setText(lb_text.text() + " / ")
def click_result():
    try:
        res = lb_text.text().split()
        for i in range(len(res)):
            try:
                res[i] = float(res[i])
            except:
                pass
        while "√" in res or "^" in res:
            i = 0
            for el in res:
                if el == "√":
                    res[i + 1] = res[i + 1] ** 0.5 
                    res.pop(i)
                if el == "^":
                    res[i - 1] = res[i - 1] ** res[i + 1]
                    res.pop(i + 1)
                    res.pop(i)
                i += 1
        while "x" in res or "/" in res:
            i = 0
            for el in res:
                if el == "x":
                    res[i - 1] *= res[i + 1]
                    res.pop(i + 1)
                    res.pop(i)
                if el == "/":
                    res[i - 1] *= res[i + 1]
                    res.pop(i + 1)
                    res.pop(i)
                i += 1
        while "+" in res or "-" in res:
            i = 0
            for el in res:
                if el == "-":
                    res[i - 1] -= res[i + 1]
                    res.pop(i + 1)
                    res.pop(i)
                if el == "+":
                    res[i - 1] += res[i + 1]
                    res.pop(i + 1)
                    res.pop(i)
                i += 1
        lb_text.setText(str(res[0]))
    except:
        lb_text("error")

def click_multiply():
    lb_text.setText(lb_text.text() + " x ")

btn_0.clicked.connect(click_0)
btn_1.clicked.connect(click_1)
btn_2.clicked.connect(click_2)
btn_3.clicked.connect(click_3)
btn_4.clicked.connect(click_4)
btn_5.clicked.connect(click_5)
btn_6.clicked.connect(click_6)
btn_7.clicked.connect(click_7)
btn_8.clicked.connect(click_8)
btn_9.clicked.connect(click_9)
btn_point.clicked.connect(click_point)

btn_plus.clicked.connect(click_plus)
btn_degree.clicked.connect(click_degree)
btn_root.clicked.connect(click_root)
btn_AC.clicked.connect(click_AC)
btn_minus.clicked.connect(click_minus)
btn_backspase.clicked.connect(click_backspase)
btn_divide.clicked.connect(click_divide)
btn_result.clicked.connect(click_result)
btn_multiply.clicked.connect(click_multiply)



#Запуск додатку
window.show()
app.exec_()