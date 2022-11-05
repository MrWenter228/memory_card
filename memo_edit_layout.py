''' Вікно для редагування  запитання'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)

from memo___app import app 

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Запитання:', txt_Question)
layout_form.addRow('Правильна:', txt_Answer)
layout_form.addRow('Неправильно:', txt_Wrong1)
layout_form.addRow('Неправильно:', txt_Wrong2)
layout_form.addRow('Неправильно:', txt_Wrong3)