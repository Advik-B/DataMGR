import sys
from PyQt5.QtWidgets import QWidget, QApplication
from qt_material import apply_stylesheet

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        apply_stylesheet(self, theme="dark_cyan.xml")
        self.setWindowTitle("Data Manager")
        # The below line is required to resize the window but the side effect is that the window is not positioned correctly.
        # self.setGeometry(100, 100, 800, 600)
        # Instead of the above line, the below line is used to resize the window correctly without changing up its position.
        self.resize(800, 600)
        # The below line is used to show the window in the center of the screen. (The centering is done by the window
        # manager automatically.)
        self.show()


def main():
    app = QApplication(sys.argv)
    UI = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
