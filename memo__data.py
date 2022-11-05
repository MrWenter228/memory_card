from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
new_quest_templ = 'Нове запитання'
new_answer_templ = 'Нова відповідь'
class Form():
    def __init__(self, question=new_quest_templ, answer=new_answer_templ, wrong_answer1='', wrong_answer2='', wrong_answer3=''):
        self.question = question
        self.answer = answer 
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.is_active = True
        self.attempts = 0
        self.correct = 0
    
    def got_right(self):
        self.attempts += 1
        self.correct += 1 
    def got_wrong(self):
        self.attempts += 1 

class FormView():
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.frm_model = frm_model
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

    def change(self, frm_model):
        self.frm_model = frm_model

class QuestionEdit(FormView):
    ''' використовується коли треба редагувати запитання'''
    def save_question(self):
        ''' зберігає текст питання '''
        self.frm_model.question = self.question.text() #копіює дані з віджета в об'єкт
    def save_answer(self):
        ''' зберігає текст правильної відповіді '''
        self.frm_model.answer = self.answer.text() # копіює дані з віджета в об'єкт
    def save_wrong(self):
        ''' зберігає всі неправильні відповіді '''
        self.frm_model.wrong_answer1 = self.wrong_answer1.text()
        self.frm_model.wrong_answer2 = self.wrong_answer2.text()
        self.frm_model.wrong_answer3 = self.wrong_answer3.text()
    def set_connects(self):
        ''' обробка подій у віджетах, так що зберігає дані '''
        self.question.editingFinished.connect(self.save_question)
        self.answer.editingFinished.connect(self.save_answer)
        self.wrong_answer1.editingFinished.connect(self.save_wrong) 
        self.wrong_answer2.editingFinished.connect(self.save_wrong)
        self.wrong_answer3.editingFinished.connect(self.save_wrong)
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        # перезаписуєм конструктор, щоб не визивати ф-ю set_connects вручну
        super().init(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.set_connects()

class QuestionListModel(QAbstractListModel):
    ''' в данных находится список объектов типа Question, 
    а также список активных вопросов, чтобы показывать его на экране '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_list = []
    def rowCount(self, index):
        ''' число элементов для показа: обязательный метод для модели, с которой будет связан виджет "список"'''
        return len(self.form_list)
    def data(self, index, role):
        ''' обязательный метод для модели: какие данные она дает по запросу от интерфейса'''
        if role == Qt.DisplayRole:
            form = self.form_list[index.row()]
            return form.question
    def insertRows(self, parent=QModelIndex()):
        ''' этот метод вызывается, чтобы вставить в список объектов новые данные;
        генерируется и вставляется один пустой вопрос.'''
        position = len(self.form_list) 
        self.beginInsertRows(parent, position, position) 
        self.form_list.append(Question())
        self.endInsertRows()
        QModelIndex()
        return True 
    def removeRows(self, position, parent=QModelIndex()):
        ''' стандартный метод для удаления строк - после удаления из модели строка автоматически удаляется с экрана'''
        self.beginRemoveRows(parent, position, position) 
        self.form_list.pop(position) 
        self.endRemoveRows() 
        return True 
    def random_question(self):
        ''' Выдаёт случайный вопрос '''
        total = len(self.form_list)
        current = randint(0, total - 1)
        return self.form_list[current]
