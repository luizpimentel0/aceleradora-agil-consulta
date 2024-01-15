from json import load, dump, decoder

class Paciente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    @staticmethod
    def get_pacientes():
        try:
            with open('pacientes.json', 'r') as f:
                pacientes = load(f)
        except FileNotFoundError:
            pacientes = []
        except decoder.JSONDecodeError:
            pacientes = []

        return [Paciente.unserialize(paciente) for paciente in pacientes]

    def adicionar(self, paciente, pacientes):
        pacientes.append(paciente)
        self.salvar(pacientes)

    def salvar(self, pacientes):
        with open(f'pacientes.json', 'w') as f:
            dump([paciente.serialize() for paciente in pacientes], f)

        print('-' * 12, 'Paciente cadastrado', '-' * 12)

    def serialize(self):
        return {
            'nome': self.nome,
            'telefone': self.telefone
        }

    @staticmethod
    def unserialize(paciente):
        return Paciente(paciente['nome'], paciente['telefone'])
