class Pessoa:
    def __init__(self, nome, matricula, curso, turma):
        self._nome = nome   # Convenção para indicar campo protegido
        self.__matricula = matricula  # Convenção para indicar campo privado
        self.curso = curso   # Campo público
        self.__turma = turma  # Convenção para indicar campo privado

    def get_nome(self):
        return self._nome
        # Retorna o valor do campo "nome"

    def set_nome(self, novo_nome):
        self._nome = novo_nome
        # Define um novo valor para o campo "nome"

    def get_matricula(self):
        return self.__matricula
        # Retorna o valor do campo "matricula"

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula
        # Define um novo valor para o campo "matricula"

    def get_turma(self):
        return self.__turma
        # Retorna o valor do campo "turma"

    def set_turma(self, nova_turma):
        self.__turma = nova_turma
        # Define um novo valor para o campo "turma"
    def exibir_cadastro(self, sala, serie):
        print(f"Nome: {self._nome}")
        print(f"Matrícula: {self.__matricula}")
        print(f"Curso: {sala}")
        print(f"Turma: {serie}")
        print()

