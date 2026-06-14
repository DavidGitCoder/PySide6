#only needed to access command line arguments
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication,QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")
        button=QPushButton("Press Me!")
        self.setCentralWidget(button)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for you app.
# If you know yo won't use command line arguments QApplication([]) works too.
app=QApplication(sys.argv)

# Create a Qt widget, which will be our window
window=QMainWindow()
window.show() # IMPORTANT!!!! Windows are hidden by default

# Start the event loop
app.exec()

# Your application won't reach here until you exit and the event loop has stopped



