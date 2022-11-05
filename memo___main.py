from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from memo___app import app
from memo__data import *
from memo_main_layout import *
from memo___card_layout import *
from memo_edit_layout import *
from random import shuffle # будем перемішувати відповіді

######################################              Константы:              #############################################
main_width, main_height=1000, 450 # начальные размеры главного окна
card_width, card_height=600, 500 # начальные размеры окна "карточка"
time_unit = 1000
###

###

######################################          Глобальные переменные:      #############################################
questions_listmodel=QuestionListModel()# список вопросов
radio_list=[rbtn_1,rbtn_2, rbtn_3,rbtn_4]# список виджетов, который надо перемешивать (для случайного размещения ответов)
frm_card = 0 # здесь будет связываться вопрос с формой теста
timer = QTimer()
win_card=QWidget()# окно карточки
win_main=QWidget()# окно редактирования вопросов, основное в программе
######################################             Тестовые данные:         #############################################
def testlist():

    frm = Form('Яблоко','apple','application','pinapple','apply')
    questions_listmodel.form_list.append(frm)
    frm = Form('Дім','house','horse','hurry')
    questions_listmodel.form_list.append(frm)
    frm =Form('Миша', 'mouse', 'mouth', 'muse', 'museum')
    questions_listmodel.form_list.append(frm)
    frm = Form('Число', 'number', 'digit', 'amount', 'summary')
    questions_listmodel.form_list.append(frm)


######################################     Функции для проведения теста:    #############################################

def set_card():
    ''' задаёт, как выглядит окно карточки'''
    win_card.resize(card_width, card_height)
    win_card.move(300, 300)
    win_card.setWindowTitle('Memory Card')
    win_card.setLayout(layout_card)



def set_main():
    ''' задаёт, как выглядит основное окно'''
    win_main.resize(main_width, main_height)
    win_main.move(100, 100)
    win_main.setWindowTitle('Список вопросов')
    win_main.setLayout(layout_main)



def show_random():
    ''' показать случайный вопрос '''
    global frm_card # как бы свойство окна - текущая форма с данными карточки
    # получаем случайные данные, и случайно же распределяем варианты ответов по радиокнопкам:
    frm_card = random_AnswerCheck(questions_listmodel, lb_Question, radio_list, lb_Correct, lb_Result)
    # мы будем запускать функцию, когда окно уже есть. Так что показываем:
    frm_card.show() # загрузить нужные данные в соответствующие виджеты 
    show_question() # показать на форме панель вопросовq

def click_OK():
    ''' проверяет вопрос или загружает новый вопрос '''
    if btn_OK.text() != 'Следующий вопрос':
        frm_card.check()
        show_result()
    else:
        # надпись на кнопке равна 'Следующий', вот и создаем следующий случайный вопрос:
        show_random()

def back_to_menu():
    ''' возврат из теста в окно редактора '''
    win_card.hide()
    win_main.showNormal()

def start_test():
    ''' при начале теста форма связывается со случайным вопросом и показывается'''
    show_random()
    win_card.show()
    win_main.showMinimized()

def edit_question(index):
    '''загружає у форму редагування запитання і відповіді які пишуться '''
    #  index - це обєкт класу QModelIndex >>>>>>>>> 
    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()
def add_form():
    ''' добавляє нове запитанн і дає можливість його змінити '''
    questions_listmodel.insertRows() # Нове запитання появляється в даних і автоматичо у списку
    last = questions_listmodel.rowCount(0) - 1   # нове запитання останнє в списку. шукаєм позицію. 
                                                # В rowCount передаєм 0, щоб ф-я працювала
    index = questions_listmodel.index(last) # получаєм обєкт класу QModelIndex, останній елемент даних
    list_questions.setCurrentIndex(index) #активне запитання
    edit_question(index)    # загружаєм для редагування
    txt_Question.setFocus(Qt.TabFocusReason) # редагуєм питання
def del_form():
    ''' видаляє запитання '''
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())
###
######################################      Установка нужных соединений:    #############################################
def connects():
    list_questions.setModel(questions_listmodel) # связать список на экране со списком вопросов
    btn_start.clicked.connect(start_test) # нажатие кнопки "начать тест" 
    btn_OK.clicked.connect(click_OK) # нажатие кнопки "OK" на форме теста
    btn_Menu.clicked.connect(back_to_menu) # нажатие кнопки "Меню" для возврата из формы теста в редактор вопросов
    timer.timeout.connect(show_card) # показываем форму теста по истечении таймера
    btn_Sleep.clicked.connect(sleep_card) # нажатие кнопки "спать" у карточки-тест
######################################            Запуск программы:         #############################################
# Основной алгоритм иногда оформляют в функцию, которая запускается, только если код выполняется из этого файла,
# а не при подключении как модуль. Детям это совершенно не нужно.
testlist()
set_card()
set_main()
connects()
win_main.show()
app.exec_()