class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Restaurante: {self._nome}, Categoria: {self._categoria}, Ativo: {self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"NOME":<20} | {"CATEGORIA":<15} | {"ATIVO":<5}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome:<20} | {restaurante._categoria:<15} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return 'ativo'.title() if self._ativo else 'inativo'.title()
    
    def alternar_estado(self):
        self._ativo = not self._ativo

praca = Restaurante('restaurante A', 'italiana')
praca.alternar_estado()
gourmet = Restaurante('restaurante B', 'chinesa')

Restaurante.listar_restaurantes()


