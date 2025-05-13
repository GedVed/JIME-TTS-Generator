from PyQt6.QtWidgets import QPushButton, QToolTip
from PyQt6.QtCore import QTimer, QEvent, Qt
from PyQt6.QtGui import QEnterEvent


class CustomToolTip(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tooltip_text = ""
        self.tooltip_delay = 100  
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.show_tooltip)

    def setToolTip(self, text: str) -> None:
            self.tooltip_text = text
            super().setToolTip("") 
        
    def enterEvent(self, event: QEnterEvent) -> None:
            
            super().enterEvent(event)
            if self.tooltip_text:
                self.timer.start(self.tooltip_delay)
        
    def leaveEvent(self, event: QEvent) -> None:
            super().leaveEvent(event)
            self.timer.stop()
            QToolTip.hideText()
        
    def show_tooltip(self) -> None:
            if self.tooltip_text:
                global_pos = self.mapToGlobal(self.rect().center())
                QToolTip.showText(global_pos, self.tooltip_text, self, self.rect(), 5000)
    