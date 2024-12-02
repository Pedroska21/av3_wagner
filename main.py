import getpass
from servicos.usuario_servicos import inserir_usuario, login
from telas.admin_tela import admin_tela

while(True):
   print("1 - Cadastrar Usuario 2 - Login")
   opc = input("Digite a opcao desejada: ")

   if opc == "1":
       email = input("Digite o email: ")
       password = input("Digite a senha: ")
       inserir_usuario(email, password)
   elif opc == "2":
       email = input("Digite o email: ")
       password = getpass.getpass("Digite a senha: ")
       usuario_autenticado = login(email, password)
       if usuario_autenticado:
            admin_tela(usuario_autenticado)
       else:
            print("Usuario ou senha invalidos!")