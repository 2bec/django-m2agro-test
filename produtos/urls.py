from django.conf.urls import url

from produtos.views import ProdutosList, ProdutoDetail

urlpatterns = [
    # api
    url(r'^$', ProdutosList.as_view(), name="produtos_list"),
    url(r'^(?P<pk>[0-9]+)/$', ProdutoDetail.as_view(), name="produto_detail")
]