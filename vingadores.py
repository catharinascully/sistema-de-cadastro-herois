class Vingadores:

    def __init__(self, nomeheroi, nomereal, categoria, poderes, poderprincipal, fraquezas, nforca):
        self.nomeheroi = nomeheroi
        self.nomereal = nomereal
        self.categoria = categoria
        self.poderes = poderes
        self.poderprincipal = poderprincipal
        self.fraquezas = fraquezas
        self.nforca = nforca

    def __str__(self):
        return (f"{'Nome de Herói'.ljust(20)} | {'Nome Real'.ljust(20)} | {'Categoria'.ljust(15)} | "
                f"{'Poderes'.ljust(30)} | {'Poder Principal'.ljust(20)} | {'Fraquezas'.ljust(20)} | "
                f"{'Nível de Força'.ljust(15)}\n"
                f"{self.nomeheroi.ljust(20)} | {self.nomereal.ljust(20)} | {self.categoria.ljust(15)} | "
                f"{self.poderes.ljust(30)} | {self.poderprincipal.ljust(20)} | "
                f"{self.fraquezas.ljust(20)} | {self.nforca.ljust(15)}")
    
    def detalhes_vingador(self):
        print(f'Nome de herói: {self.nomeheroi}')
        print(f'Nome real: {self.nomereal}')
        print(f'Categoria: {self.categoria}')
        print(f'Poderes: {self.poderes}')
        print(f'Poder principal: {self.poderprincipal}')
        print(f'Fraquezas: {self.fraquezas}')
        print(f'Nível de força: {self.nforca}')

    def lista_poderes(self):
        print(f'Os poderes de {self.nomeheroi} são: {self.poderes}')
        
    def lista_fraquezas(self):
        print(f'As fraquezas de {self.nomeheroi} são: {self.fraquezas}')

    def aplicar_tornozeleira(self):
        print(f'Tornozeleira aplicada em {self.nomeheroi}')

    def aplicar_chip_gps(self):
        print(f'Chip GPS aplicado em {self.nomeheroi}')
    
    def convocar_vingador(self):
        print(f'O vingador {self.nomeheroi} foi chamado para a batalha!')

    def prender(self):
        print(f'O(a) {self.nomeheroi} foi preso(a)!')