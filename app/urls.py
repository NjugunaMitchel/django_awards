from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views

app_name='app'

urlpatterns = [
    
    url('rateform',views.rateform, name='rateform'),
    url(r'^rates/$',views.rates, name='rates'),
    url('^$',views.landing, name='landing'),
    url(r'^newproject/$',views.newproject, name='newproject'),

]