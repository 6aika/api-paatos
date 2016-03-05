# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'case', views.CaseViewSet)
router.register(r'organization', views.OrganizationViewSet)
router.register(r'action', views.ActionViewSet)
urlpatterns = router.urls

# urlpatterns = [
    # url(r'^case/$', views.CaseList.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.CaseDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += router.urls
