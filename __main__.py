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
        self.show()


def main():
    app = QApplication(sys.argv)
    UI = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
