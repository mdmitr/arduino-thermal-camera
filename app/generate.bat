#pyuic5 ui/ThremalScan.ui > ui_ThermalScan.py
call del Ui_*.py
for /f %%f in ('dir /b ui') do (call pyuic5 ui/%%f > Ui_%%f)

call rename Ui_*.ui *.py
