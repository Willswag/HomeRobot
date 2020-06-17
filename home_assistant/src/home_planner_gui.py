#!/usr/bin/env python
"""
create a gui for modifing maps to be used with robots and the navigation stack
menu bar for editing tools
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, qApp, QMenu,
QMessageBox, QGridLayout,QLabel)
from PyQt5.QtGui import QIcon, QPixmap


class gui(QMainWindow):

    def __init__(self):

        super().__init__()
        self.title = 'image'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # grid = QGridLayout()
        #
        # x = 0
        # y = 0
        #
        # self.text = f'x:{x}, y:{y}'
        #
        # self.label = QLabel(self.text,self)
        # grid.addWidget(self.label,0,0,Qt.AlignCenter)
        #
        # self.setMouseTracking(True)
        # self.setLayout(grid)
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('IMG_2625.JPG')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())


        exitAct = QAction(QIcon('exit.png'),'&Exit',self)
        exitAct.setShortcut('ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        editMenu = menubar.addMenu('Edit')
        viewMenu = menubar.addMenu('View')
        helpMenu = menubar.addMenu('Help')

        openMenu = QMenu('Open', self)
        openAct = QAction('open file', self)
        openMenu.addAction(openAct)

        newAct = QAction('New', self)
        newAct.setShortcut('ctrl+N')

        fileMenu.addAction(newAct)
        fileMenu.addMenu(openMenu)
        fileMenu.addAction(exitAct)

        # self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('home')
        self.show()

    def closeEvent(self,event):

        reply = QMessageBox.question(self,'Message',"Are you sure you want to exit without saving? ", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            event.accept()
        elif reply == QMessageBox.Cancel:
            event.ignore()
        else:
            event.ignore()
    #
    # def mouseMoveEvent(self,e):
    #
    #     x = e.x()
    #     y = e.y()
    #
    #     text = f'x:{x}, y:{y}'
    #     self.label.setText(text)

    def showFileDialog(self):

        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self,'open file', home_dir)

        if fname[0]:
            f = open(fname[0],'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

def main():
    app = QApplication(sys.argv)
    ex = gui()
    sys.exit(app.exec_())

if __name__ =='__main__':
        main()
