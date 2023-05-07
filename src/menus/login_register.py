import pygame
from PyQt5 import uic, QtWidgets
import menus.menu1
from menus.user import User

pygame.display.set_mode((1,1))

app = QtWidgets.QApplication([])

login_screen = uic.loadUi("assets/login_screen.ui")
register_screen = uic.loadUi("assets/register_screen.ui")

user = User("assets/database.db")

def run_login(): 
    login_screen.pushButton.clicked.connect(login)
    login_screen.pushButton_2.clicked.connect(open_register_screen)
    register_screen.pushButton.clicked.connect(register)
    
    

    login_screen.show()
    app.exec()
    app.quit()
    

def login():
    login_screen.label_3.setText("")
    username = login_screen.lineEdit.text()
    password = login_screen.lineEdit_2.text()
    
    if username == "" or password == "":
        login_screen.label_3.setText("Preencha todos os campos!")
        return
    elif user.login(username, password):
        login_screen.label_3.setText("Login realizado com sucesso!")
        login_screen.close()
        menus.menu1.run_menu1()
    else:
        login_screen.label_3.setText("Usuário ou senha incorretos!")

def open_register_screen():
    login_screen.close()
    register_screen.show()

def register():
    register_screen.label_5.setText("")
    register_screen.label_6.setText("")
    register_screen.label_7.setText("")
    register_screen.label_8.setText("")
    
    username = register_screen.lineEdit.text()
    email = register_screen.lineEdit_2.text()
    password = register_screen.lineEdit_3.text()
    password2 = register_screen.lineEdit_4.text()
    
    result = user.register(username, email, password, password2)
    
    if result == "Usuário cadastrado com sucesso!":
        register_screen.close()
        login_screen.show()
        login_screen.label_3.setText(result)
    else:
        error_labels = {
            "o Username já está sendo usado!": register_screen.label_6,
            "Este email já está sendo usado, tente outro!": register_screen.label_7,
            "Preencha todos os campos!": register_screen.label_5,
            "As senhas não coincidem!": register_screen.label_8,
        }
        error_label = error_labels[result]
        if error_label:
            error_label.setText(result)
            
        