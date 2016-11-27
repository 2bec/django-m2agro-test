from django.conf.urls import url
from django.views.generic import TemplateView

from servicos.views import ServicosList, ServicoDetail

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="safras/home.html")),
    # api
    url(r'^api/v1/$', ServicosList.as_view(), name="servicos_list"),
    url(r'^api/v1/(?P<pk>[0-9]+)/$', ServicoDetail.as_view(), name="servico_detail"),
]