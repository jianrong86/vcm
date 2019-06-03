"""vcm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from vcmapp import views
# from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index/', views.release_ver_manage),
    url(r'^$', views.SoftwareView.as_view(), name='software-view'),
    # url(r'^new_items/', views.new_items),
    # url(r'^new_items_submit/', views.submit_items),
    url(r'^software_create', views.SoftwareCreate.as_view(), name="software-create"),
    url(r'^software_update', views.SoftwareUpdate.as_view(), name="software-update"),
    url(r'^software_list', views.SoftwareList.as_view(), name="software-list"),
    # url(r'^edit_items/(?P<id>[0-9]+)/$', views.edit_items),
    # url(r'^edit_items_save/(?P<id>[0-9]+)/$', views.update_items),

    # url(r'^submit_items/', views.submit_items),
    # url(r'^api/', include('vcmapp.urls', namespace='vcmapp')),
]
