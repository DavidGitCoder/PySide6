from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My App")

layout = QVBoxLayout()

label = QLabel("Nothing clicked yet")
button = QPushButton("Click me")

def on_click():
    label.setText("Button clicked!")

button.clicked.connect(on_click)

layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec())