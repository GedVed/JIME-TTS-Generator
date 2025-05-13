from PyQt6.QtWidgets import QApplication
import sys
from src.tts_generator import TTS_Generator


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TTS_Generator()
    window.show()
    sys.exit(app.exec())




