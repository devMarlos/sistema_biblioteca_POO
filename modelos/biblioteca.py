from modelos.avaliacao import Avaliacao
from modelos.itens.item_biblioteca import ItemBiblioteca

class Biblioteca:
    bibliotecas = []
    
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self.avaliacao = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)
        
    def __str__(self):
        return self.nome
    
    # Método para listar toda as bibliotecas criadas, média de avaliações e o status 
    @classmethod
    def listar_biblioteca(cls):
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Nota média'.ljust(25)} | {'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {str(biblioteca.media_avaliacao).ljust(25)} |{biblioteca.ativo}")
    
    # Método para alterar o status da biblioteca
    def alterna_estado(self):
        self._ativo = not self._ativo
    
    # Método para fazer a validação se a biblioteca está ativada  
    @property
    def ativo(self):
        return "Ativada" if self._ativo else "Desativada"
    
    # Método que recebe a avaliação herdando atributos da classe "avaliacao.py"
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self.avaliacao.append(avaliacao)
    
    # Método que calcula a média das avaliações
    @property
    def media_avaliacao(self):
        if not self.avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self.avaliacao)
        media = round(soma / len(self.avaliacao), 1)
        return media
    
    # Método que adiciona um item na biblioteca instanciada, herdando da classe ItemBiblioteca
    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)
    
    # Método que exibe uma lista com todos os itens adicionados na lista de itens
    def exibir_itens(self):
        print(f'Itens da biblioteca {self.nome}\n')
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, 'isbn'):
                msg_livro = f'{i}. (Livro) -> Título: {item._titulo.ljust(25)} | Autor: {item._autor.ljust(25)} | Preço: {str(item._preco).ljust(25)} | ISBN: {item.isbn}'
                print(msg_livro)
            else:
                msg_revista = f'{i}. (Revista) -> Título: {item._titulo.ljust(23)} | Autor: {item._autor.ljust(25)} | Preço: {str(item._preco).ljust(25)} | Edição: {item.edicao}'
                print(msg_revista)