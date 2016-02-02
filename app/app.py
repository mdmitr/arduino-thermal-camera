import sys
from PyQt5.QtWidgets import QApplication, QDialog

app = QApplication(sys.argv)


from ThermalScanDialog import ThermalScanDialog
ui = ThermalScanDialog()
ui.show()

sys.exit(app.exec_())
