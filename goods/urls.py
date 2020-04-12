from django.conf.urls import url

from goods import views

urlpatterns = [
    # html

    # ajax
    url(r'^root_category$', views.root_category, name='root_category'),
    url(r'^sub_category$', views.sub_category, name='sub_category'),
]