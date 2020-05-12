import sqlite3
import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)
        self.pushButton.clicked.connect(self.open_launch_form)

    def run(self):
        con = sqlite3.connect("db/blogs.sqlite")
        cur = con.cursor()
        if self.linelog.text() and self.linepass.text():
            sql = "SELECT id FROM users WHERE hashed_password = ? AND email = ?"
            arr = (self.linepass.text(), self.linelog.text(),)
            print(cur.execute(sql, arr).fetchall())
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
        uic.loadUi('test2.ui', self)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
