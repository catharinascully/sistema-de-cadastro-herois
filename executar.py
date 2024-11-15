from cadastro_vingadores import CadastroVingadores

def menu():
    print('\n===== Vingadores =====\n')
    print('1. Cadastrar um vingador')
    print('2. Listar vingadores')
    print('3. Procurar vingador')
    print('4. Sair')

def executar():
    cadastro = CadastroVingadores()

    while True:
        menu()
        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == "1":
            cadastro.cadastrar_vingador()
        elif opcao == "2":
            cadastro.listar_vingadores()
        elif opcao == "3":
            cadastro.procurar_vingador()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()