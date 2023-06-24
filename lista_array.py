from estrutura_elementar import estrutura_elementar


class ArrayList(estrutura_elementar):
    def __init__(self):
        self.list = []

    def esta_vazio(self) -> bool:
        tamanho = len(self.list)
        if tamanho == 0:
            return True
        else:
            return False

    def inserir(self, item):
        self.list.append(item)

    def remove(self, item): 
        self.list.remove(item)

    def tamanho(self) -> int:
        tamanho = len(self.list)
        return tamanho

    def limpa(self):
        self.list.clear()

    def procura(self, item) -> bool:
        return item in self.list

    def indice_de(self, item):
        try:
            indice = self.list.index(item)
            return indice
        except ValueError:
            return -1

    def recupera_indice(self, index):
        try:
            item = self.list[index]
            return item
        except IndexError:
            return None
