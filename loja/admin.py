from django.contrib import admin
from .models import Categoria, Produto, Carrinho, ProdutoCarrinho

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Carrinho)
admin.site.register(ProdutoCarrinho)


# Register your models here.
