''' Главное окно '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListView, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 

from memo_edit_layout import *
from memo___card_layout import *


list_questions = QListView()
wdgt_edit = QWidget()
wdgt_edit.setLayout(layout_form)
btn_add = QPushButton('Нове запитання')
btn_delete = QPushButton('Видалити запитання')
btn_start = QPushButton('Почати')
main_col1 = QVBoxLayout()
main_col2 = QVBoxLayout()
main_line2 = QHBoxLayout()
layout_main = QVBoxLayout()