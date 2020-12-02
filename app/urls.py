from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

app_name='app'

urlpatterns = [
    path('',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('landing/',views.landing, name='landing'),
    path('rates/',views.rates, name='rates'),

]