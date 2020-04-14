from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog


class MyApp(QWidget):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)

        self.setup_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setup_ui(self):
        self.vlayout = QVBoxLayout()
        self.btn = QPushButton("按钮")
        self.btn.setObjectName('btn')
        self.vlayout.addWidget(self.btn)
        self.setLayout(self.vlayout)

    @pyqtSlot()
    def on_btn_clicked(self):
        print(1)
        target_dir = QFileDialog.getExistingDirectory(self, caption='选择路径', directory='c:\\')
        print(target_dir)


def main():
    import sys
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
