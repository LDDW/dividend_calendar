# Imports
import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("app.ui", None)
window.setWindowTitle('TODO LIST APP')

window.show()
app.exec()