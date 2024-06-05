from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []


    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    @classmethod
    def listar_restaurante(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} |{"Avaliacao".ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

    def __str__(self):
        return f"{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {self.ativo}"
    
    
    
    @property
    def ativo(self):
       return "Ativo" if self._ativo else "Desativado"
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if  0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return "-"
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        media_notas = round(soma_notas / len(self._avaliacoes), 1)
        return media_notas
