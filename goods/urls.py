from django.conf.urls import url

from goods import views

urlpatterns = [
    # html
    url(r'^$', views.index, name='index'),

    # ajax
    url(r'^api$', views.api, name='api'),
]