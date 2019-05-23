from django.conf.urls import url
from vcmapp import views_interface

urlpatterns = [
        url(r'^add_software/', views_interface.add_software, name='add_software'),
]