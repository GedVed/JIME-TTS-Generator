from PyQt6.QtWidgets import QFileDialog, QMainWindow, QPushButton



def check_file_dialog(window: QMainWindow):
        if(window.ui.radioButton_CoquiAI.isChecked()):
            window.ui.pushButton_UserVoice.setEnabled(True)
        else:
            window.ui.pushButton_UserVoice.setEnabled(False)

def open_file_dialog(window: QMainWindow):
        file_path, _ = QFileDialog.getOpenFileName(
            window, "Select Audio file", "", "Audio Files (*.wav)")
        if file_path:
            window.ui.textEdit_Results.append(f"Selected file: {file_path}")          