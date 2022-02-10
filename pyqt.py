from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100,100,200,300)
    window.setWindowTitle("Graphical User Interface")
    layout = QVBoxLayout()
    label = QLabel("Press the Button")
    textbox =QTextEdit()
    button = QPushButton("Button")
    button.clicked.connect(lambda : on_clicked(textbox.toPlainText()))
    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)
  
    window.setLayout(layout)

  

    

    window.show()
    app.exec_()

def on_clicked(msg):
    #print("The button was clicked")
    message = QMessageBox()
    message.setText(msg)
    message.exec_()
  

if __name__ == "__main__":
    main()



      # label= QLabel(window)
  # label.setText("This is a text")
  # label.setFont(QFont("Arial",16))
  # label.move(50,100)