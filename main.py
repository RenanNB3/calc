from Equipe import *
import cadastro
print("Quem deseja acessar?")
quem = int(input("1 - Aluno que ir� cadastrar\n2 - Professores"))
if quem == 1:
    cadastro.cadastro()

elif quem == 2:
    print("\nAlunos cadastrados: ")
    cadastro.exibir_alunos_cadastrados()
else:
   print("Voc� n�o tem acesso!")

