from django.conf.urls import url
from django.views.generic import TemplateView

from safras.views import SafrasList, SafraDetail

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="safras/home.html")),
    # api
    url(r'^api/v1/$', SafrasList.as_view(), name="safras_list"),
    url(r'^api/v1/(?P<pk>[0-9]+)/$', SafraDetail.as_view(), name="safra_detail")
]