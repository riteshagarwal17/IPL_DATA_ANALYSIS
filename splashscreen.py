from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import main_window
import time


class Form(QDialog):

    def __init__(self):
        super(Form, self).__init__()
        self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')
        self.setGeometry(600,150, 630, 650)
        self.lineedit = QLineEdit("To Proceed,Press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.update_ui)

    def update_ui(self):
        self.browser.append(self.lineedit.text())


    def keyPressEvent(self, QKeyEvent):
        #returnPressed = pyqtSignal
        try:
            self.obj = main_window.Demo()
            self.obj.show()
        except BaseException as ex:
            print(ex)

if __name__ == "__main__":
    import sys, time

    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap('cp.png')

    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    # splash = QSplashScreen(splash_pix)
    # adding progress bar
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)

    # splash.setMask(splash_pix.mask())

    splash.show()
    splash.showMessage("<h1><font color='blue'>Welcome To IPL</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)

    for i in range(1, 11):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()

    # Simulate something that takes time
    time.sleep(2)

    form = Form()
    form.show()
    splash.finish(form)
    sys.exit(app.exec_())