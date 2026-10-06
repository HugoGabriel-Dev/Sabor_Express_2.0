from avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Restaurante: {self._nome}, Categoria: {self._categoria}, Ativo: {self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"NOME".ljust(20)} | {"CATEGORIA".ljust(20)} | {"AVALIACOES".ljust(20)} | {"ATIVO"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.mostrar_media_avaliacao).ljust(20)} | {restaurante.ativo}')

    
    @property
    def ativo(self):
        return 'ativo'.title() if self._ativo else 'inativo'.title()
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)
    @property
    def mostrar_media_avaliacao(self):
        if not self._avaliacoes:
            return 0
        soma_avaliacoes = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_avaliacoes = len(self._avaliacoes)
        media = round(soma_avaliacoes / quantidade_avaliacoes, 1)
        return media