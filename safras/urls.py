from django.conf.urls import url

from safras.views import SafrasList, SafraDetail

urlpatterns = [
    # api
    url(r'^$', SafrasList.as_view(), name="safras_list"),
    url(r'^(?P<pk>[0-9]+)/$', SafraDetail.as_view(), name="safra_detail")
]