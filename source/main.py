import sys
from Views.MainMenu import MainMenu
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
ludo = MainMenu()
ludo.run()
app.exec()
