from django.conf.urls import url
from django.views.generic import TemplateView

from servicos.views import ServicosList, ServicoDetail

urlpatterns = [
    # api
    url(r'^$', ServicosList.as_view(), name="servicos_list"),
    url(r'^(?P<pk>[0-9]+)/$', ServicoDetail.as_view(), name="servico_detail"),
]