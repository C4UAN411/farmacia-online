from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ProdutoCarrinho')

class ProdutoCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)


# Create your models here.
