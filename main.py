# -*- coding:utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from aboutui import Ui_Dialog
from bdapi import get_audio
from mainui import Ui_MainWindow


class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()


class AboutUs(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(AboutUs, self).__init__(parent)
        self.setupUi(self)


class MyAPP(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyAPP, self).__init__(parent)
        self.about_us = AboutUs()
        self.setupUi(self)

    @pyqtSlot()
    def on_action_triggered(self):
        """
        菜单选项点击 对应的槽函数
        :return:
        """
        self.about_us.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.pushButton.setDisabled(True)
        print("开始合成")
        text = self.plainTextEdit.toPlainText()
        per_map = {
            -2: 0,
            -3: 1,
            -4: 3,
            -5: 4
        }
        aue_map = {
            -2: 3,
            -3: 6
        }
        per = per_map[self.buttonGroup.checkedId()]
        aue = aue_map[self.buttonGroup_2.checkedId()]
        spd = self.verticalSlider.value()
        pit = self.verticalSlider_2.value()
        vol = self.verticalSlider_3.value()
        param = {
            'vol': vol,
            'pit': pit,
            'spd': spd,
            'per': per,
            'aue': aue
        }
        print(text)
        print(param)
        try:
            get_audio(text, **param)
        except Exception as e:
            print(e)
        finally:
            print('合成结束')
        self.pushButton.setEnabled(True)


def main():
    import sys
    app = QApplication(sys.argv)
    my_app = MyAPP()
    style_file = './myqss.qss'
    qss_style = CommonHelper.readQss(style_file)
    my_app.setStyleSheet(qss_style)
    my_app.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
