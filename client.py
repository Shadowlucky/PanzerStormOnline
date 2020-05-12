import sys
from client_base import Network
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from style_2 import Ui_Form
from style import Ui_Form_2
from PyQt5.QtCore import Qt
import threading


class Nick(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Ник')
        self.button.clicked.connect(self.next_window)

    def next_window(self):
        name = self.name.text()
        if not name:
            pass
        else:
            self.chat = Chat(self, name)
            self.chat.show()
            self.setVisible(False)
            p = threading.Thread(target=thread, args=[self.chat])
            p.start()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.next_window()


class Chat(QWidget, Ui_Form_2):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Чат')
        self.show()
        self.n = Network()
        self.n.send(args[1])

    def run(self, msg):
        self.recv_block.append(msg)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            text = self.send_block.text()
            if not text:
                pass
            else:
                self.n.send(text)
            self.send_block.clear()


def thread(data):
    while True:
        try:
            msg = data.n.recv()
            if not msg:
                pass
            else:
                data.run(msg)
        except:
            pass


app = QApplication(sys.argv)
ex = Nick()
ex.show()
sys.exit(app.exec_())
