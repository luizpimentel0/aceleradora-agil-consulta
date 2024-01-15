def validate_nome(nome):
    if nome == '':
        print('-' * 45)
        print('Nome inválido')
        print('Tente novamente')
        return False
    return True

def validate_telefone(telefone, pacientes):
    if telefone == '' or telefone.isnumeric() == False:
        print('-' * 45)
        print('Telefone inválido')
        print('Tente novamente')
        return False
    elif telefone in [paciente.telefone for paciente in pacientes]:
        print('-' * 45)
        print('Telefone já cadastrado')
        return False
    return True

def validate_cadastro_consulta(pacientes):
    if len(pacientes) == 0:
        print('-' * 45)
        print('Nenhum paciente cadastrado')
        print('É preciso cadastrar um paciente antes de cadastrar uma consulta')
        return False
    return True

def validate_paciente_consulta(paciente_selecionado, pacientes):
    if paciente_selecionado < 0 or paciente_selecionado >= len(pacientes) or pacientes[paciente_selecionado] == None:
        print('-' * 45)
        print('Paciente inválido')
        print('Tente novamente')
        return False
    return True

def validate_dia(dia_consulta, dia_atual):
    if dia_consulta.isnumeric() == False or int(dia_consulta) < dia_atual.day or int(dia_consulta) < 1 or int(dia_consulta) > 31:
        print('-' * 45)
        print('-' * 50)
        print('Dia inválido')
        print('Tente novamente')
        return False
    return True

def validate_hora(hora):
    if hora.isnumeric() == False or int(hora) < 0 or int(hora) > 23:
        print('-' * 45)
        print('Hora inválida')
        print('Tente novamente')
        return False
    return True

def validate_consulta(consultas):
    if len(consultas) == 0:
        print('-' * 45)
        print('Nenhuma consulta cadastrada')
        return False
    return True

def validate_consulta_selecionada(consulta_selecionada, consultas):
    if consulta_selecionada < 0 or consulta_selecionada >= len(consultas) or consultas[consulta_selecionada] == None:
        print('-' * 45)
        print('Consulta inválida')
        print('Tente novamente')
        return False
    return True

def validate_horario_dia_consulta(consultas, dia_consulta, hora_consulta, especialidade):
    for consulta in consultas:
        if consulta.dia == dia_consulta and consulta.hora == hora_consulta and consulta.especialidade.lower() == especialidade.lower():
            print('-' * 45)
            print('Já existe uma consulta nesse horário')
            print('Tente novamente')
            return False
    return True

def validate_paciente_consulta_hora(consultas, pacientes, paciente_selecionado, hora, dia):
    for consulta in consultas:
        print(consulta.paciente['nome'], pacientes[paciente_selecionado].nome)
        if consulta.paciente['nome'] == pacientes[paciente_selecionado].nome and consulta.hora == hora and consulta.dia == dia:
            print('-' * 45)
            print('Paciente já possui uma consulta nesse horário')
            print('Tente novamente')
            return False
    return True
