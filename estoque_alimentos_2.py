from datetime import datetime

class EstoqueAlimentos:
    def __init__(self):
        # O estoque agora armazena uma lista de dicionários com quantidade e validade
        self.estoque = {}

    def adicionar_item(self, nome, quantidade, validade):
        validade = datetime.strptime(validade, "%d/%m/%Y")  # Converte a validade para o formato de data
        if nome in self.estoque:
            self.estoque[nome]['quantidade'] += quantidade
            self.estoque[nome]['validade'] = validade  # Atualiza a validade caso seja necessário
        else:
            self.estoque[nome] = {'quantidade': quantidade, 'validade': validade}
        print(f"Adicionado {quantidade} de {nome} com validade até {validade.strftime('%d/%m/%Y')} no estoque.")

    def remover_item(self, nome, quantidade):
        if nome in self.estoque:
            if self.estoque[nome]['quantidade'] >= quantidade:
                self.estoque[nome]['quantidade'] -= quantidade
                print(f"Removido {quantidade} de {nome} do estoque.")
                if self.estoque[nome]['quantidade'] == 0:
                    del self.estoque[nome]
            else:
                print(f"Quantidade de {nome} insuficiente no estoque para remover.")
        else:
            print(f"O item {nome} não está no estoque.")

    def atualizar_item(self, nome, nova_quantidade, nova_validade):
        if nome in self.estoque:
            nova_validade = datetime.strptime(nova_validade, "%d/%m/%Y")
            self.estoque[nome]['quantidade'] = nova_quantidade
            self.estoque[nome]['validade'] = nova_validade
            print(f"Estoque de {nome} atualizado para {nova_quantidade} com validade até {nova_validade.strftime('%d/%m/%Y')}.")
        else:
            print(f"O item {nome} não está no estoque.")

    def listar_estoque(self):
        if self.estoque:
            print("Itens no estoque:")
            for nome, detalhes in self.estoque.items():
                validade_str = detalhes['validade'].strftime('%d/%m/%Y')
                print(f"- {nome}: {detalhes['quantidade']} unidades, validade até {validade_str}")
        else:
            print("O estoque está vazio.")

def menu():
    estoque = EstoqueAlimentos()
    while True:
        print("\nSistema de Controle de Estoque de Alimentos")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Atualizar item")
        print("4. Listar estoque")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do item: ")
            quantidade = int(input("Quantidade: "))
            validade = input("Data de validade (dd/mm/aaaa): ")
            estoque.adicionar_item(nome, quantidade, validade)
        elif opcao == '2':
            nome = input("Nome do item: ")
            quantidade = int(input("Quantidade: "))
            estoque.remover_item(nome, quantidade)
        elif opcao == '3':
            nome = input("Nome do item: ")
            nova_quantidade = int(input("Nova quantidade: "))
            nova_validade = input("Nova data de validade (dd/mm/aaaa): ")
            estoque.atualizar_item(nome, nova_quantidade, nova_validade)
        elif opcao == '4':
            estoque.listar_estoque()
        elif opcao == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
