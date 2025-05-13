
from PyQt6.QtWidgets import QMainWindow
from ui.main_window import Ui_MainWindow
from src.ui_control import check_file_dialog, open_file_dialog

class TTS_Generator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_LanguageChoice.addItems(["English", "Polish"])
        self.ui.radioButton_CoquiAI.setChecked(True)

        self.ui.radioButton_CoquiAI.toggled.connect(lambda: check_file_dialog(self))

        self.ui.pushButton_UserVoice.clicked.connect(lambda: open_file_dialog(self))
        