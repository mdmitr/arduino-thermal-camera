import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ThermalScan import Ui_ThermalScanDialog

app = QApplication(sys.argv)
ui = Ui_ThermalScanDialog()
ui.show()
sys.exit(app.exec_())
