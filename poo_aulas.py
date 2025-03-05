from avaliacao import Avaliacao


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurante(cls):
        print(f'{'Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'
    
    def altenar_estado(self):
        self._ativo = not self._ativo

    def receber_avalicao(self, cliente, nota):
        if nota >=0 and nota <=5:
            avalicao = Avaliacao(cliente, nota)
            self._avaliacao.append(avalicao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        soma_das_notas = sum(avalicao._nota for avalicao in self._avaliacao)
        quantidade_nota = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_nota, 1)
        return media


