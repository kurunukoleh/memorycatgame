from PyQt5.QtWidgets import *
import base
import random
from meniu import meniuwind
import redaction

app = QApplication([])

app.setStyleSheet("""
    QWidget {
        background-color: #FFFFDD;
        color : #016A70;
    }
    
    QPushButton {
        background-color: #D2DE32;
        color : #016A70;
        border-radius: 5px ;
        border-color: #D2DE32;
        border-style: hidden;
        border-width: 5px;
        min-height: 20px;
        font-size: 15px;
        font-family: Impact;
        
    }
    
    QGroupBox {
        background-color: #A2C579;
        color : #016A70;
    }
    
    QRadioButton {
        background-color: #A2C579;
        color : #016A70;
    }
    
    QSpinBox#a{
        background-color: #D2DE32;
        color : #016A70;
        border-radius: 5px ;
        border-color: #D2DE32;
        border-style: none;
        border-width: 5px;
        min-height: 20px;
        font-size: 15px;
        font-family: Impact;
    }
    
    QLabel#b{
        background-color: #FFFFDD;
        color : #016A70;
        border-radius: 5px ;
        border-color: #D2DE32;
        border-style: none;
        border-width: 5px;
        min-height: 20px;
        font-size: 15px;
        font-family: Impact;
    }
    
""")


window = QWidget()
window.resize(400 , 300)

mainline = QVBoxLayout()

menubut = QPushButton('меню')
restbtn = QPushButton('Відпочити')
timespn = QSpinBox()
timespn.setObjectName('a')
timlb = QLabel('хвилин')
timlb.setObjectName('b')
redaguvaty = QPushButton('редагувати питаня')

firstline = QHBoxLayout()
firstline.addWidget(menubut)
firstline.addWidget(restbtn)
firstline.addWidget(timespn)
firstline.addWidget(timlb)
mainline.addLayout(firstline)

quetext = QLabel('скільки отчімів у a4 ?')
mainline.addWidget(quetext)

answersgroup = QGroupBox('варіанти відповідей')
answer1 = QRadioButton('1')
answer2 = QRadioButton('2')
answer3 = QRadioButton('3')
answer4 = QRadioButton('4')
answerline = QVBoxLayout()
answerline.addWidget(answer1)
answerline.addWidget(answer2)
answerline.addWidget(answer3)
answerline.addWidget(answer4)
answers = [answer1 , answer2 , answer3 , answer4]
answersgroup.setLayout(answerline)
mainline.addWidget(answersgroup)

result = QLabel('Результат :')
answerline.addWidget(result)
result.hide()

ansbut = QPushButton('відповісти')
nextque = QPushButton('наступне питання')
mainline.addWidget(ansbut)
mainline.addWidget(nextque)
nextque.hide()
mainline.addWidget(redaguvaty)

def shovresult():
    for i in range(4):
        answers[i].hide()
    result.show()
    nextque.show()
    ansbut.hide()
    if answers[0].isChecked():
        result.setText('правильно')
    else:
        result.setText('не правильно')

def showqueshon():
    random.shuffle(answers)
    quetext.setText(base.qeust[base.currentQuest]['питання:'])
    answers[0].setText(base.qeust[base.currentQuest]['правильеа відповідь'])
    answers[1].setText(base.qeust[base.currentQuest]['неправильна1'])
    answers[2].setText(base.qeust[base.currentQuest]['неправильна2'])
    answers[3].setText(base.qeust[base.currentQuest]['неправильна3'])

def showqueshon2():
    random.shuffle(answers)
    base.currentQuest += 1
    quetext.setText(base.qeust[base.currentQuest]['питання:'])
    answers[0].setText(base.qeust[base.currentQuest]['правильеа відповідь'])
    answers[1].setText(base.qeust[base.currentQuest]['неправильна1'])
    answers[2].setText(base.qeust[base.currentQuest]['неправильна2'])
    answers[3].setText(base.qeust[base.currentQuest]['неправильна3'])
    result.hide()
    nextque.hide()
    for i in range(4):
        answers[i].show()
    ansbut.show()

def redactioned():
    window.hide()
    redaction.redwind()
    window.show()

    showqueshon()


showqueshon()
ansbut.clicked.connect(shovresult)
nextque.clicked.connect(showqueshon2)
menubut.clicked.connect(meniuwind)
redaguvaty.clicked.connect(redactioned)

window.setLayout(mainline)
window.show()
app.exec()