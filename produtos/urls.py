from django.conf.urls import url
from django.views.generic import TemplateView

from produtos.views import ProdutosList, ProdutoDetail

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="produtos/home.html")),
    # api
    url(r'^api/v1/$', ProdutosList.as_view(), name="produtos_list"),
    url(r'^api/v1/(?P<pk>[0-9]+)/$', ProdutoDetail.as_view(), name="produto_detail")
]