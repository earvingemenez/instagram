from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('search.urls')),
    url(r'^accounts/', include('allauth.urls')),
]

urlpatterns +=[
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
]