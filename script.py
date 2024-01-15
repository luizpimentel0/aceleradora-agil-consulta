from datetime import datetime
from Paciente import Paciente
from Consulta import Consulta
from helper_functions import *

pacientes = Paciente.get_pacientes()
consultas = Consulta.get_consultas()

print('-' * 15, 'Seja bem-vindo', '-' * 15)
print('O que deseja fazer ?')
while True:
    print('-' * 20, 'Menu', '-' * 20)
    print('1. Cadastrar um paciente')
    print('2. Marcar uma consulta')
    print('3. Cancelar uma consulta')
    print('4. Sair')

    opcao = input().strip()

    if opcao == '1':
        nome = input('Digite o nome do paciente: ').strip()
        if not validate_nome(nome):
            continue

        telefone = input('Digite o telefone do paciente: ').strip()
        if not validate_telefone(telefone, pacientes):
            continue

        paciente = Paciente(nome, telefone)
        paciente.adicionar(paciente, pacientes)

    elif opcao == '2':
        if not validate_cadastro_consulta(pacientes):
            continue

        print('Selecione o paciente:')
        data_atual = datetime.now()

        for i, paciente in enumerate(pacientes):
            print(f'{i + 1} . {paciente.nome}')

        paciente_selecionado = int(input('Selecione um paciente: ')) - 1

        if not validate_paciente_consulta(paciente_selecionado, pacientes):
            continue

        dia = input('Digite o dia da consulta [SOMENTE NÚMEROS]: ').strip()
        if not validate_dia(dia, data_atual):
            continue

        hora = input('Digite a hora da consulta [SOMENTE NÚMEROS]: ').strip()
        if not validate_hora(hora):
            continue

        especialidade = input('Digite a especialidade da consulta: ').strip()

        if not validate_horario_dia_consulta(consultas, dia, hora, especialidade):
            continue

        if not validate_paciente_consulta_hora(consultas, pacientes, paciente_selecionado, hora, dia):
            continue

        consulta = Consulta(pacientes[paciente_selecionado], dia, hora, especialidade)
        consulta.paciente = Paciente.serialize(consulta.paciente)
        consulta.adicionar(consulta, consultas)
        print('-' * 12, 'Consulta cadastrada', '-' * 12)
       
    elif opcao == '3':
        if not validate_consulta(consultas):
            continue

        print('Selecione a consulta:')
        for i, consulta in enumerate(consultas):
            print(f'{i + 1} . {consulta.paciente["nome"]}')

        consulta_selecionada = int(input('Selecione uma consulta: ')) - 1
        if not validate_consulta_selecionada(consulta_selecionada, consultas):
            continue
        consulta.remover(consultas, consulta_selecionada)

    elif opcao == '4':
        print('-' * 50)
        print('-' * 8, 'Obrigado por utilizar o sistema', '-' * 8)
        print('-' * 20, 'Até logo', '-' * 20)
        break;