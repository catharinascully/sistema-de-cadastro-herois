from vingadores import Vingadores

class CadastroVingadores:

    def __init__(self):
        self.vingadores = {}

    def cadastrar_vingador(self):
        nomeheroi = input('Nome do Herói: ')
        nomereal = input('Nome Real: ')
        categoria = input('Categoria: ')
        poderes = input('Poderes: ')
        poderprincipal = input('Poder principal: ')
        fraquezas = input('Fraquezas: ')
        nforca = input('Nível de força: ')

        vingador = Vingadores(nomeheroi, nomereal, categoria, poderes, poderprincipal, fraquezas, nforca)

        self.vingadores[nomeheroi] = vingador

        print(f'O vingador foi cadastrado: \n{vingador}')

    def listar_vingadores(self):
        if not self.vingadores:
            print('Não há vingadores cadastrados.')
        else:
            print('Vingadores cadastrados:\n')
            for nomeheroi in self.vingadores:
                print(nomeheroi)

    def procurar_vingador(self):
        nomeheroi = input('Nome do vingador que você deseja procurar: \n')
        vingador = self.vingadores.get(nomeheroi)

        if vingador:
            print('Vingador encontrado:')
            vingador.detalhes_vingador()
        else:
            print(f'{nomeheroi} não encontrado.')