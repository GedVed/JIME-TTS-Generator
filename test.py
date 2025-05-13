from PyQt6.QtWidgets import QApplication
from src.custom_tooltip import CustomToolTip

app = QApplication([])
button = CustomToolTip("Test Button")
button.setToolTip("Test tooltip")
button.show()
app.exec()