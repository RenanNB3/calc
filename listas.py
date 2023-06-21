def lista(curso, cursos, turma):
  for curso in cursos:
    if curso == "1":
      sala = "Informática"
    elif curso == "2":
      sala = "Eletrotécnica"
    elif curso == "3":
      sala = "Química"
    elif curso == "4":
      sala = "Edificações"
    print("Curso: ",sala)
    for turma in cursos[curso]:
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
      print("Turma: ",serie)
      for aluno in cursos[curso][turma]:
        print("\033[31m",aluno,"\033[0;0m")


