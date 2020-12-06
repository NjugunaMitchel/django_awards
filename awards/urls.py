from django.contrib import admin
from django.contrib.auth import views
from django.conf.urls import url,include
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include('app.urls', namespace='app')),
    url('^accounts/register/',
        RegistrationView.as_view(success_url='/accounts/login'),
        name='django_registration_register'),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^logout/$',views.LogoutView.as_view(), {'next_page': 'settings.LOGOUT_REDIRECT_URL'}),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
