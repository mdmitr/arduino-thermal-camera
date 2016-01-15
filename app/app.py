import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ThermalScanDialog import ThermalScanDialog

app = QApplication(sys.argv)
ui = ThermalScanDialog()
ui.show()
sys.exit(app.exec_())
