from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

class Question():
    def __init__(self,question,r_ans, w_ans1, w_ans2, w_ans3):
        self.question=question
        self.r_ans=r_ans
        self.w_ans1=w_ans1
        self.w_ans2=w_ans2
        self.w_ans3=w_ans3

def show_result():
    box.hide() 
    box1.show()
    ans.setText('Следующий вопрос')

def show_question():
    box1.hide()
    r_box.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    r_box.setExclusive(True)
    ans.setText('Ответить')
    box.show()

def start_test():
    if ans.text()=='Ответить':
        show_result()
    elif ans.text()=='Следующий вопрос':
        show_question()

#1 часть
app = QApplication([])

win = QWidget()
win.setWindowTitle('Memory Card')
win.resize(300,150)
q=QLabel('')
ans1=QRadioButton('')
ans2=QRadioButton('')
ans3=QRadioButton('')
ans4=QRadioButton('')
ans=QPushButton('Ответить')
box=QGroupBox('Варианты ответов')

r_box=QButtonGroup()
r_box.addButton(ans1)
r_box.addButton(ans2)
r_box.addButton(ans3)
r_box.addButton(ans4)

answers = [ans1,ans2,ans3,ans4]

box1=QGroupBox('Результат теста')
good=QLabel('Верно/Неверно')
good1=QLabel('Правильный ответ')
v_line3=QVBoxLayout()

def ask(q2: Question):
    shuffle(answers)
    answers[0].setText(q2.r_ans)
    answers[1].setText(q2.w_ans1)
    answers[2].setText(q2.w_ans2)
    answers[3].setText(q2.w_ans3)
    q.setText(q2.question)
    good1.setText(q2.r_ans)
    show_question()

q_list=list()

q1=Question('Национальный язык Бразилии','Португальский','Испанский','Английский','Итальянский')
q2=Question('Самая высокая гора в мире','Эверест','Арарат','Эльбрус','Фудзияма')
q3=Question('Назовите первые 3 символа числа Пи','3,14','2,45','6,70','8,92')
q4=Question('Кто придумал Теорию относительности?','А. Эйнштейн','Н. Тесла','Л. Толстой','Д. Трамп')
q5=Question('Какая химическая формула воды','H20','NaCl','H3PO4','Ba')
q6=Question('Какая столица Канады','Оттава','Квебек','Кёльн','Амстердам')

q_list.append(q1)
q_list.append(q2)
q_list.append(q3)
q_list.append(q4)
q_list.append(q5)
q_list.append(q6)

def next_q():
    cur_question= randint(0,len(q_list)-1)
    win.total+=1
    ask(q_list[cur_question])

def show_correct(res):
    good.setText(res)
    show_result()    

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        win.score+=1
        
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно') 
    print('Статистика:')
    print('Всего вопросов:',win.total)
    print('Всего правильных ответов:',win.score)
    print('Рейтинг:',win.score/win.total*100)

def check_Ok():
    if ans.text()=='Ответить':
        check_answer()
    elif ans.text()=='Следующий вопрос':
        next_q()

#группа
h_line2=QHBoxLayout()
h_line3=QHBoxLayout()
v_line2=QVBoxLayout()

#остальное
h_line=QHBoxLayout()
h_line4=QHBoxLayout()

v_line=QVBoxLayout()

h_line.addWidget(q,alignment=Qt.AlignCenter)
h_line2.addWidget(ans1,alignment=Qt.AlignHCenter)
h_line2.addWidget(ans3,alignment=Qt.AlignHCenter)
h_line3.addWidget(ans2,alignment=Qt.AlignHCenter)
h_line3.addWidget(ans4,alignment=Qt.AlignHCenter)
h_line4.addStretch(1)
h_line4.addWidget(ans,stretch=3,alignment=Qt.AlignCenter)

v_line2.addLayout(h_line2)
v_line2.addLayout(h_line3)
v_line.addLayout(h_line)
v_line.addWidget(box,alignment=Qt.AlignCenter)

box.setLayout(v_line2)

v_line.addWidget(box1,alignment=Qt.AlignCenter)
box1.setLayout(v_line3)
v_line3.addWidget(good)
v_line3.addWidget(good1,alignment=Qt.AlignVCenter)
box1.hide()

ans.clicked.connect(check_Ok)
win.total=0
win.score=0
next_q()

v_line.addLayout(h_line4)
win.setLayout(v_line)
win.show()
app.exec_()
