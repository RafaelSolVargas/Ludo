from Views.PlayerInterface import PlayerInterface
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
ludo = PlayerInterface()
ludo.run()
app.exec()
