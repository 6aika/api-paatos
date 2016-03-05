from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^case/$', views.CaseList.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.CaseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
