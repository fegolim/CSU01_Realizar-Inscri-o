'''class SistemaDeInscricao:
    def __init__(self):
        self.alunos = {}
        self.disciplinas = ['Matematica', 'Historia', 'Fisica', 'Quimica', 'Biologia', 'Ingles', 'Redacao']
        self.horarios = ['07:20', '08:00', '08:40', '09:20', '10:00', '10:40']  
        self.disciplina_horario = dict(zip(self.disciplinas, self.horarios))  
        self.creditos_por_disciplina = 4
        self.max_creditos = 20

    def inscrever(self, nome_aluno, disciplina, horario):
        if nome_aluno not in self.alunos:
            self.alunos[nome_aluno] = {'disciplinas_inscritas': [], 'creditos': self.max_creditos}
        info_aluno = self.alunos[nome_aluno]

        if disciplina not in self.disciplinas:
            print("Disciplina nao encontrada.")
            return

        if disciplina in info_aluno['disciplinas_inscritas']:
            print("Aluno ja inscrito nesta disciplina.")
            return

        if info_aluno['creditos'] < self.creditos_por_disciplina:
            print("Creditos insuficientes.")
            return

        # Verificar se o horário já foi escolhido para outra disciplina
        for disciplina_inscrita, horario_inscrito in info_aluno['disciplinas_inscritas']:
            if horario_inscrito == horario:
                print(f"Horario {horario} já foi escolhido para a disciplina {disciplina_inscrita}.")
                return

        info_aluno['disciplinas_inscritas'].append((disciplina, horario))
        info_aluno['creditos'] -= self.creditos_por_disciplina
        print(f"Aluno {nome_aluno} inscrito na disciplina {disciplina} com sucesso. Horario: {horario}")

    def exibir_disciplinas(self):
        print("Disciplinas disponiveis:")
        for idx, disciplina in enumerate(self.disciplinas, start=1):
            print(f"{idx} - {disciplina}")

    def exibir_horarios(self):
        print("Horarios disponiveis:")
        for idx, horario in enumerate(self.horarios, start=1):
            print(f"{idx} - {horario}")

    def revisar_inscricao(self, nome_aluno):
        if nome_aluno in self.alunos:
            print(f"\nInscricoes do aluno {nome_aluno}:")
            for disciplina, horario in self.alunos[nome_aluno]['disciplinas_inscritas']:
                print(f"{disciplina} ({horario})")  
        else:
            print(f"\nAluno {nome_aluno} nao encontrado.")

    def confirmar_inscricoes(self):
        print("\nConfirmando inscricoes de todos os alunos...")
        for nome_aluno, info_aluno in self.alunos.items():
            print(f"Aluno: {nome_aluno}")
            print("Disciplinas inscritas:")
            for disciplina, horario in info_aluno['disciplinas_inscritas']:
                print(f"{disciplina} ({horario})")  
            print("\n---")

    def sair_do_sistema(self):
        print("Saindo do sistema...")
        exit()

def main():
    sistema = SistemaDeInscricao()
    while True:
        print("\nMenu de opcoes:")
        print("1 - Inscrever aluno")
        print("2 - Revisar inscricao")
        print("3 - Confirmar inscricoes")
        print("4 - Sair do sistema")
        escolha = input("Escolha uma opcao: ").strip()
        if escolha == '1':
            nome_aluno = input("Digite o nome do aluno: ").strip()
            sistema.exibir_disciplinas()
            opcao_disciplina = int(input("Escolha o numero da disciplina: ").strip()) - 1
            if 0 <= opcao_disciplina < len(sistema.disciplinas):
                disciplina = sistema.disciplinas[opcao_disciplina]
                sistema.exibir_horarios()
                opcao_horario = int(input("Escolha o numero do horario: ").strip()) - 1
                if 0 <= opcao_horario < len(sistema.horarios):
                    horario = sistema.horarios[opcao_horario]
                    sistema.inscrever(nome_aluno, disciplina, horario)
                else:
                    print("Numero do horario invalido.")
            else:
                print("Numero da disciplina invalido.")
        elif escolha == '2':
            nome_aluno = input("Digite o nome do aluno: ").strip()
            sistema.revisar_inscricao(nome_aluno)
        elif escolha == '3':
            sistema.confirmar_inscricoes()
        elif escolha == '4':
            sistema.sair_do_sistema()
        else:
            print("Opção invalida.")

if __name__ == "__main__":
    main()'''

import os

class SistemaDeInscricao:
    def __init__(self):
        self.alunos = {}
        self.disciplinas = ['Matematica', 'Historia', 'Fisica', 'Quimica', 'Biologia', 'Ingles', 'Redacao']
        self.horarios = ['07:20', '08:00', '08:40', '09:20', '10:00', '10:40']  
        self.disciplina_horario = dict(zip(self.disciplinas, self.horarios))  
        self.creditos_por_disciplina = 4
        self.max_creditos = 20

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def inscrever(self, nome_aluno, disciplina, horario):
        if nome_aluno not in self.alunos:
            self.alunos[nome_aluno] = {'disciplinas_inscritas': [], 'creditos': self.max_creditos}
        info_aluno = self.alunos[nome_aluno]

        if disciplina not in self.disciplinas:
            print("\nDisciplina nao encontrada.\n")
            return

        if disciplina in info_aluno['disciplinas_inscritas']:
            print("\nAluno ja inscrito nesta disciplina.\n")
            return

        if info_aluno['creditos'] < self.creditos_por_disciplina:
            print("\nCreditos insuficientes.\n")
            return

        # Verificar se o horário já foi escolhido para outra disciplina
        for disciplina_inscrita, horario_inscrito in info_aluno['disciplinas_inscritas']:
            if horario_inscrito == horario:
                print(f"\nHorario {horario} já foi escolhido para a disciplina {disciplina_inscrita}.\n")
                return

        info_aluno['disciplinas_inscritas'].append((disciplina, horario))
        info_aluno['creditos'] -= self.creditos_por_disciplina
        print(f"\nAluno {nome_aluno} inscrito na disciplina {disciplina} com sucesso. Horario: {horario}\n")

    def exibir_disciplinas(self):
        print("\nDisciplinas disponiveis:")
        for idx, disciplina in enumerate(self.disciplinas, start=1):
            print(f"{idx} - {disciplina}")

    def exibir_horarios(self):
        print("\nHorarios disponiveis:")
        for idx, horario in enumerate(self.horarios, start=1):
            print(f"{idx} - {horario}")

    def revisar_inscricao(self, nome_aluno):
        if nome_aluno in self.alunos:
            print(f"\nInscricoes do aluno {nome_aluno}:")
            for disciplina, horario in self.alunos[nome_aluno]['disciplinas_inscritas']:
                print(f"{disciplina} ({horario})")  
        else:
            print(f"\nAluno {nome_aluno} nao encontrado.")

    def confirmar_inscricoes(self):
        print("\nConfirmando inscricoes de todos os alunos...")
        for nome_aluno, info_aluno in self.alunos.items():
            print(f"Aluno: {nome_aluno}")
            print("Disciplinas inscritas:")
            for disciplina, horario in info_aluno['disciplinas_inscritas']:
                print(f"{disciplina} ({horario})")  
            print("\n---")

    def sair_do_sistema(self):
        print("\n...Saindo do sistema...\n")
        exit()

def main():
    sistema = SistemaDeInscricao()
    sistema.limpar_tela()  # Limpa a tela
    while True:
        print("\nMenu de opcoes:")
        print("1 - Inscrever aluno")
        print("2 - Revisar inscricao")
        print("3 - Confirmar inscricoes")
        print("4 - Sair do sistema")
        escolha = input("Escolha uma opcao: ").strip()
        if escolha == '1':
            nome_aluno = input("Digite o nome do aluno: ").strip()
            sistema.exibir_disciplinas()
            opcao_disciplina = int(input("Escolha o numero da disciplina: ").strip()) - 1
            if 0 <= opcao_disciplina < len(sistema.disciplinas):
                disciplina = sistema.disciplinas[opcao_disciplina]
                sistema.exibir_horarios()
                opcao_horario = int(input("Escolha o numero do horario: ").strip()) - 1
                if 0 <= opcao_horario < len(sistema.horarios):
                    horario = sistema.horarios[opcao_horario]
                    sistema.inscrever(nome_aluno, disciplina, horario)
                else:
                    print("Numero do horario invalido.")
            else:
                print("Numero da disciplina invalido.")
        elif escolha == '2':
            nome_aluno = input("Digite o nome do aluno: ").strip()
            sistema.revisar_inscricao(nome_aluno)
        elif escolha == '3':
            sistema.confirmar_inscricoes()
        elif escolha == '4':
            sistema.sair_do_sistema()
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()
