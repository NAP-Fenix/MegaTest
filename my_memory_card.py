




from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel,QMessageBox)
from random import shuffle , randint 
 

class Question():
   def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
        
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3
        self.question=question

swip =[] 
swip.append(Question(' Кто снял фильм Аватар?', 'Джеймс Кэмерон', 'Джордж Лукас', 'Питер Джексон', 'Ридли Скотт'))
swip.append(Question(' Год выхода сериала место преступления майами?', '2002', '2003', '2012','2001'))
swip.append(Question(' apple Дата основания?', '1976', '2000', '1986','1977'))  
swip.append(Question(' Год окончания сериала место преступления майами?', ' 2012', '2003', '2015','2013'))
swip.append(Question(' nvidia дата основания?', ' 1993', '1893', '1992','1983'))
swip.append(Question(' какой национальности не сушествует?', ' Смурфы', 'Энцы', 'Чулымцы','Алеуты'))
swip.append(Question(' В аквариуме 10 рыбок 2 утанули 3 уплыли сколько рыбок осталось в аквариуме?', ' 10', '8', '7','5'))



app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

score = '0'
stata = QLabel('Ваша статистика: '+ score )

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Правельный ответ")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)



layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addWidget(stata, alignment = Qt.AlignHCenter)
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    global score
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
    if lb_Result.text() == 'Верно!':
        score = int(score)
        score += 10
        score = str(score)
    else:
        score = int(score)
        score += -10
        score = str(score)
    stata.setText('Ваша статистика: ' + score)
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q:Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 
 
def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Верно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_quetsion():
    window.i+=1
    random_number = randint(0, len(swip)-1)
    q = swip[random_number]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        if window.i<6:
            next_quetsion()
        else:
           aaa= QMessageBox() 
           aaa.setText('тест завершон!')
           aaa.exec()
           print("тест пройден!")

window = QWidget()
window.i = 0
window.setLayout(layout_card)
window.setWindowTitle('TEST Card')
next_quetsion()
btn_OK.clicked.connect(click_OK) 
 
window.show()
app.exec()




#где тут можно поменять разешени
