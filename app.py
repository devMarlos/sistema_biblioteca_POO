from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade = Biblioteca('Biblioteca da Cidade')
biblioteca_shopping = Biblioteca('Biblioteca do Shopping')

biblioteca_cidade.alterna_estado()

livro1 = Livro('1984', 'George Orwell', 30.0, '084-3245')
revista1 = Revista('National Geographic', 'John Doe', 15.0, 'Quinta')
livro2 = Livro('Brave New World', 'Aldous Huxley', 25.0, "084-3245777")

livro1.aplicar_desconto()
revista1.aplicar_desconto()

biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(revista1)
biblioteca_cidade.adicionar_item(livro2)

biblioteca_cidade.receber_avaliacao('Marlos', 10.0)

def main():
    Biblioteca.listar_biblioteca()
    biblioteca_cidade.exibir_itens()

if __name__ == "__main__":
    main()