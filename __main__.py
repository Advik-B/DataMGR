import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTableWidget
from qt_material import apply_stylesheet
from PyQt5.uic import loadUi


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Load the UI file
        loadUi("design.ui", self)
        # Apply the stylesheet
        apply_stylesheet(self, theme="dark_cyan.xml")
        self.setWindowTitle("Data Manager")
        # The below line is required to resize the window but the side effect is that the window is not positioned
        # correctly. self.setGeometry(100, 100, 800, 600) Instead of the above line, the below line is used to resize
        # the window correctly without changing up its position.
        self.resize(800, 600)
        # Calling the beforeLoad method
        self.beforeLoad()
        # The below line is used to show the window in the center of the screen. (The centering is done by the window
        # manager automatically.)
        self.show()
    
    def beforeLoad(self):
        # assert 0.1 * 0.2 == 0.02, RED + "Computers suck at math!" + RESET
        pass

def main():
    app = QApplication(sys.argv)
    UI = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
