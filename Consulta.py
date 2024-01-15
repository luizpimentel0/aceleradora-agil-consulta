from json import load, dump, decoder

class Consulta:
    def __init__(self, paciente, dia, hora, especialidade):
        self.paciente = paciente
        self.dia = dia
        self.hora = hora
        self.especialidade = especialidade

    @staticmethod
    def get_consultas():
        try:
            with open('consultas.json', 'r') as f:
                consultas = load(f)
        except FileNotFoundError:
            consultas = []
        except decoder.JSONDecodeError:
            consultas = []

        return [Consulta.unserialize(consulta) for consulta in consultas]

    def adicionar(self, consulta, consultas):
        consultas.append(consulta)
        self.salvar(consultas)

    def salvar(self, consultas):
        with open(f'consultas.json', 'w') as f:
            dump([Consulta.serialize(consulta) for consulta in consultas], f)

    def cancelar(self):
        print('-' * 12, 'Consulta cancelada', '-' * 12)
        print('Paciente:', self.paciente['nome'])
        print('Dia:', self.dia)
        print('Hora:', self.hora)
        print('Especialidade:', self.especialidade)

    def remover(self, consultas, indice):
        del consultas[indice]
        self.cancelar()
        self.salvar(consultas)

    def serialize(self):
        return {
            'paciente': self.paciente,
            'dia': self.dia,
            'hora': self.hora,
            'especialidade': self.especialidade
        }

    def unserialize(consulta):
        return Consulta(consulta['paciente'], consulta['dia'], consulta['hora'], consulta['especialidade'])
