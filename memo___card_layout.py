''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 


app = QApplication([])
# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
btn_Menu = QPushButton('Меню') 
# кнопка прибирає вікно і повертає його після закінчення таймера
btn_Sleep = QPushButton('Відпочити')
# введення кількості хвилин
box_Minutes = QSpinBox() 
box_Minutes.setValue(30)
# кнопка відповіді "Ок" / "Наступний"
btn_OK = QPushButton('Відповісти') 
# текст питання
lb_Question = QLabel('')
# Опиши групу перемикачів
RadioGroupBox = QGroupBox("Варіанти відповідей")
#Рамка для групи перемикачів з відповідями
RadioGroup = QButtonGroup()
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4) 
# Опиши панень з результатами
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('') # правильно/не правильно
lb_Correct = QLabel('') # правильна відповідь

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
#Розміщуємо варіанти відповідей в два стовпці всередині групи
layout_ans2.addWidget(rbtn_1) #Дві відповіді в перший стовпець
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) #Дві відповіді у другий стовпець
layout_ans3.addWidget(rbtn_4)
#Тепер перемикачі прив'язані до однієї горизонтальної направляючої лінії
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
RadioGroupBox.setLayout(layout_ans1)

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignRight | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
#Головні напрямляючі лінії
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1) # розрив між кнопками
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин')) # змінна не потрібна
layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)
 
layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) # більша кнопка
layout_line4.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)


# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне питання')
    

def show_question():
    ''' показати панель запитань '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    #Скинути обрану радіо-кнопку
    RadioGroup.setExclusive(False)#Зняти обмеження, щоб скинути вибір 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) #Повернути обмеження