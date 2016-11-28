from django.conf.urls import url

from produtos.views import ProdutosList, ProdutoDetail, PrecoMedioUpdate

urlpatterns = [
    # api
    url(r'^$', ProdutosList.as_view(), name="produtos_list"),
    url(r'^update/preco_medio/$', PrecoMedioUpdate.as_view(), name="preco_medio_update"),
    url(r'^(?P<pk>[0-9]+)/$', ProdutoDetail.as_view(), name="produto_detail")
]