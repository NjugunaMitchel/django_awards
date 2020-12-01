from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

app_name='clone'

urlpatterns = [
    path('',views.signin, name='signin'),
    path('login',views.login, name='login'),

]