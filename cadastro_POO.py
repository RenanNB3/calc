from equipes import *

# Função que irá abrir nossso arquivo
f = open("alunos_cadastrados.txt", "a")


# Função para cadastrar um aluno
def cadastrar_aluno(numero_matricula, nome, curso, turma):
    # Abrir o arquivo em modo de adição
    with open("alunos_cadastrados.txt", "a", encoding="utf-8") as arquivo:
        # Escrever os dados do aluno no arquivo
        arquivo.write(f"Numero Matricula: {numero_matricula}, Nome: {nome}, Curso: {curso} Turma: {turma}\n")


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
        nome = input("Digite o nome do discente (ou 'f' para finalizar o cadastro): ").capitalize()
        if nome == 'F':
            break

        matricula = input("Digite a matrícula do discente: ")
        while not matricula.isdigit() or len(matricula) < 13 or len(matricula) > 15:
            tamanho = len(matricula)
            print("matrícula inválida, foi digitado apenas", tamanho)
            matricula = input("Digite a matrícula do discente: ")

        print("Todas os cursos :\n1 - Informatica\n2 - Eletrotécnica \n3 - Química -\n4 - Edificações")
        curso = input("Digite o número correspondente à turma do discente: ").capitalize()

        print("todas as turmas:\n 1 = 1°A\n 2 = 1°B\n 3 = 2°Mat\n 4 = 2°Vesp\n 5 = 3°Mat\n 6 = 3°Vesp")
        turma = input("Digite a turma do discente: ").capitalize()

        pessoa = Pessoa(nome, matricula, turma)
        pessoas.append(pessoa)
        print("Cadastro realizado com sucesso!\n")

        if curso in cursos and turma in cursos[curso]:
            cursos[curso][turma].append(pessoa.nome)
        print("Cadastros Realizados:\n")
        # Cursos
        if curso == "1":
            sala = "Informática"
        elif curso == "2":
            sala = "Eletrotécnica"
        elif curso == "3":
            sala = "Química"
        elif curso == "4":
            sala = "Edificações"
        # turmas
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
        cadastrar_aluno(matricula, nome, sala, serie)

    # Info
    print("Lista de Informática M\n")
    for i in lista_info1A:
        print("Alunos do 1º Informática A\n", i)

    for i in lista_info1B:
        print("Alunos do 1º Informática B\n", i)

    for i in lista_info2M:
        print("Alunos do 2º Informática M\n", i)

    for i in lista_info2V:
        print("Alunos do 2º Informática V\n", i)

    for i in lista_info3M:
        print("Alunos do 3º Informática M\n", i)

    for i in lista_info3V:
        print("Alunos do 3º Informática V\n", i)
    # Eletro
    print("Lista de Eletro\n")
    for i in lista_eletro1A:
        print("Alunos do 1º Eletrotécnica A\n", i)

    for i in lista_eletro1B:
        print("Alunos do 1º Eletrotécnica B\n", i)

    for i in lista_eletro2M:
        print("Alunos do 2º Eletrotécnica M\n", i)

    for i in lista_eletro2V:
        print("Alunos do 2º Eletrotécnica V\n", i)

    for i in lista_eletro3M:
        print("Alunos do 3º Eletrotécnica M\n", i)

    for i in lista_eletro3V:
        print("Alunos do 3º Eletrotécnica V\n", i)

    # Quim
    print("Lista de Quimica\n")
    for i in lista_quim1A:
        print("Alunos do 1º Química A\n", i)

    for i in lista_quim1B:
        print("Alunos do 1º Química B\n", i)

    for i in lista_quim2M:
        print("Alunos do 2º Química M\n", i)

    for i in lista_quim2V:
        print("Alunos do 2º Química V\n", i)

    for i in lista_quim3M:
        print("Alunos do 3º Química M\n", i)

    for i in lista_quim3V:
        print("Alunos do 3º Química V\n", i)

    # Edif
    print("Lista de Edificações\n")
    for i in lista_edif1A:
        print("Alunos do 1º Edificações A\n", i)

    for i in lista_edif1B:
        print("Alunos do 1º Edificações B\n", i)

    for i in lista_edif2M:
        print("Alunos do 2º Edificações M\n", i)

    for i in lista_edif2V:
        print("Alunos do 2º Edificações V\n", i)

    for i in lista_edif3M:
        print("Alunos do 3º Edificações M\n", i)

    for i in lista_edif3V:
        print("Alunos do 3º Edificações V\n", i)


cadastro()

# Exibir os alunos cadastrados
print("Alunos cadastrados:")
exibir_alunos_cadastrados()

