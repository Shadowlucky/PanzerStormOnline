import sqlite3
import sys
from game import main

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Login_window.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        global nickname
        con = sqlite3.connect("db/blogs.sqlite")
        cur = con.cursor()
        if self.linelog.text() and self.linepass.text():
            sql = "SELECT name FROM users WHERE hashed_password = ? AND email = ?"
            arr = (self.linepass.text(), self.linelog.text(),)
            nickname = cur.execute(sql, arr).fetchall()[0][0]
            if cur.execute(sql, arr).fetchall() != '[]':
                self.open_launch_form()
        else:
            print(12)
        cur.close()
        con.close()

    def open_launch_form(self):
        self.launch_form = Launch()
        self.launch_form.show()
        self.central_form = MyWidget()
        self.central_form.hide()


class Launch(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ip_window.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if self.lineEdit.text():
            main(self.lineEdit.text(), nickname)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
