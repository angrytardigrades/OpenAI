from PyQt6.QtWidgets import QApplication, QMainWindow,QTextEdit,QLineEdit,QPushButton
import sys
from PyQt6.QtCore import Qt
from backend import Chatbot
import threading

class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot() 

        self.setMinimumSize(700,500)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(5,5, 590,420)
        self.chat_area.setReadOnly(True)


        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(5,430, 490,40)


        self.button = QPushButton("send",self)
        self.button.setGeometry(495,430, 100,40)
        self.button.clicked.connect (self.send_message)

        self.show()
        
    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#00008B'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response,args=(user_input,))
        thread.start()
    

    def get_bot_response(self,user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#FF0000'>Bot: {response}</P>")



app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())