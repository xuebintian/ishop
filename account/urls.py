from django.conf.urls import url

from account import views

urlpatterns = [
    # html
    url(r'^$', views.index, name='index'),

    # ajax
    url(r'^api$', views.api, name='api'),
    url(r'^create_address$', views.create_address, name='create_address'),
    url(r'^update_address$', views.update_address, name='update_address'),
    url(r'^delete_address$', views.delete_address, name='delete_address'),

]