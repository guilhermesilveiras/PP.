class Livro:

    nome = None
    qtdPaginas = None
    autor = None
    preco = None

    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self. qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco

    def get_preco(self):
        return self.preco

    def set_preco(self, novoPreco):
        self.preco = novoPreco

l1 = Livro("Harry Potter", "300", "J.K. Rowling", 79)


print(l1.nome, " — ", l1.autor, " — Valor: R$ ", l1.get_preco())