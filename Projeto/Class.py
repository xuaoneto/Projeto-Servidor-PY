class Relogio:

    def __init__ (self, marca, modelo, cor, preco, descricao, estoque):
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._preco = preco
        self._descricao = descricao
        self._estoque = estoque
    
    def __str__(self):
        return f'\n Marca:{self._marca}\n Modelo:{self._modelo}\n Cor:{self._cor}\n Preço:R$ {self._preco},00\n Descrição:{self._descricao}\n Unidades em estoque:{self._estoque}\n ----------\n '

