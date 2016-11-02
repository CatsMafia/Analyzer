from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'',views.helloWorld,name='helloWorld'),
    url(r'/calc',views.calculate,name= 'calculate')
]
