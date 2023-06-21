import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Туристическое агенство')
        self.setGeometry(0, 0, 300, 100)

        self.tours = QLabel('Туры:')
        self.tours_towns = QLabel('Город вылета:')
        self.tours_towns_text = QLineEdit()
        self.tours_countries = QLabel('Страна:')
        self.tours_countries_text = QLineEdit()
        self.tours_date = QLabel('Дата начала:')
        self.tours_date_text = QLineEdit()
        self.tours_nigths = QLabel('Ночей:')
        self.tours_nigths_text = QLineEdit()
        self.tours_btn = QPushButton('Подтвердить')
        self.tours_btn.clicked.connect(self.get_result)

        self.tours_layout = QHBoxLayout()
        self.tours_layout_town = QVBoxLayout()
        self.tours_layout_countries = QVBoxLayout()
        self.tours_layout_date = QVBoxLayout()
        self.tours_layout_nights = QVBoxLayout()
        self.tours_layout_town.addWidget(self.tours_towns)
        self.tours_layout_town.addWidget(self.tours_towns_text)
        self.tours_layout.addLayout(self.tours_layout_town)
        self.tours_layout_countries.addWidget(self.tours_countries)
        self.tours_layout_countries.addWidget(self.tours_countries_text)
        self.tours_layout.addLayout(self.tours_layout_countries)
        self.tours_layout_date.addWidget(self.tours_date)
        self.tours_layout_date.addWidget(self.tours_date_text)
        self.tours_layout.addLayout(self.tours_layout_date)
        self.tours_layout_nights.addWidget(self.tours_nigths)
        self.tours_layout_nights.addWidget(self.tours_nigths_text)
        self.tours_layout.addLayout(self.tours_layout_nights)
        self.tours_layout.addWidget(self.tours_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.tours)
        layout.addLayout(self.tours_layout)

        self.setLayout(layout)
        self.show()

    def get_result(self):
        QMessageBox.information(
                                self, 'Введенные данные', f'Город: {self.tours_towns_text.text()}\n'
                                f'Страна: {self.tours_countries_text.text()}\n'
                                f'Дата: {self.tours_date_text.text()}\n'
                                f'Количество ночей: {self.tours_nigths_text.text()}'
                                )



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
