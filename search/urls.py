from django.conf.urls import url
from .views import ManagementView, SearchView


urlpatterns = [
    url(r'$', SearchView.as_view(), name="search"),
    url(r'^management/$', ManagementView.as_view(), name="management"),
]
