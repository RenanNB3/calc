from Equipe import *
import listas

f = open("alunos_cadastrados.txt", "a", encoding="utf-8")


# Função para cadastrar um aluno
def cadastrar_aluno(numero_matricula, nome, curso, turma):
    # Abrir o arquivo em modo de adição
    with open("alunos_cadastrados.txt", "a") as arquivo:
        # Escrever os dados do aluno no arquivo
        arquivo.write(f"Número Matrícula: {numero_matricula}, Nome: {nome}, Curso: {curso} Turma: {turma}\n")


# Função para exibir os alunos cadastrados
def exibir_alunos_cadastrados():
    # Abrir o arquivo em modo de leitura
    with open("alunos_cadastrados.txt", "r") as arquivo:
        # Ler as linhas do arquivo
        linhas = arquivo.readlines()
        # Imprimir os alunos cadastrados
        for linha in linhas:
            print(linha.rstrip())  # Remover a quebra de linha ao imprimir


# Cadastrar um aluno
def cadastro():
    lista_info1A = []
    lista_info1B = []
    lista_info2M = []
    lista_info2V = []
    lista_info3M = []
    lista_info3V = []

    lista_eletro1A = []
    lista_eletro1B = []
    lista_eletro2M = []
    lista_eletro2V = []
    lista_eletro3M = []
    lista_eletro3V = []

    lista_quim1A = []
    lista_quim1B = []
    lista_quim2M = []
    lista_quim2V = []
    lista_quim3M = []
    lista_quim3V = []

    lista_edif1A = []
    lista_edif1B = []
    lista_edif2M = []
    lista_edif2V = []
    lista_edif3M = []
    lista_edif3V = []
    cursos = {
        "1": {
            "1": lista_info1A,
            "2": lista_info1B,
            "3": lista_info2M,
            "4": lista_info2V,
            "5": lista_info3M,
            "6": lista_info3V
        },
        "2": {
            "1": lista_eletro1A,
            "2": lista_eletro1B,
            "3": lista_eletro2M,
            "4": lista_eletro2V,
            "5": lista_eletro3M,
            "6": lista_eletro3V
        },
        "3": {
            "1": lista_quim1A,
            "2": lista_quim1B,
            "3": lista_quim2M,
            "4": lista_quim2V,
            "5": lista_quim3M,
            "6": lista_quim3V
        },
        "4": {
            "1": lista_edif1A,
            "2": lista_edif1B,
            "3": lista_edif2M,
            "4": lista_edif2V,
            "5": lista_edif3M,
            "6": lista_edif3V
        }
    }

    pessoas = []

    while True:
        nome = input("Digite o nome do discente: ").capitalize()

        matricula = input("Digite a matrícula do discente:\n")
        while not matricula.isdigit() or len(matricula) < 10:
            print("matrícula inválida, digite apenas números acima de 10 algarismos")
            matricula = input("Digite a matrícula do discente: ")

        print("Todas os cursos :\n1 - Informatica\n2 - Eletrotécnica \n3 - Química -\n4 - Edificações")
        curso = input("Digite o número correspondente à turma do discente: ").capitalize()

        print("todas as turmas:\n 1= 1°A\n 2= 1°B\n 3= 2°Mat\n 4= 2°Vesp\n 5= 3°Mat\n 6= 3°Vesp")
        turma = input("Digite a turma do discente: ").capitalize()

        pessoa = Pessoa(nome, matricula, curso, turma)
        pessoas.append(pessoa)
        print("Cadastro realizado com sucesso!\n")

        if curso in cursos and turma in cursos[curso]:
            cursos[curso][turma].append(pessoa._nome)

        # modifica a escolha p/ o nome do curso
        if curso == "1":
            sala = "Informática"
        elif curso == "2":
            sala = "Eletrotécnica"
        elif curso == "3":
            sala = "Química"
        elif curso == "4":
            sala = "Edificações"
        # modifica a escolha p/ o nome do curso
        if turma == "1":
            serie = "1°A"
        elif turma == "2":
            serie = "1°B"
        elif turma == "3":
            serie = "2°M"
        elif turma == "4":
            serie = "2°V"
        elif turma == "5":
            serie = "3°M"
        elif turma == "6":
            serie = "3°V"
        pessoa.exibir_cadastro(sala, serie)
        cadastrar_aluno(matricula, nome, sala, serie)

        repetir = input("Deseja realizar um novo cadastro?\n1- sim\n2- não")
        if repetir == '2':
            break
    print("Cadastros Realizados:\n")
    listas.lista(curso, cursos, turma)








