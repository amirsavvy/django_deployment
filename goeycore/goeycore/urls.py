"""goeycore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from goeymvcapp import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^frontend/', include('goeymvcapp.urls')),
    # Customer regiseration routes
    url(r'work-with-us-signup', views.cusotmer_registeration, name='get_signup'),
    url(r'signup', views.post_cusotmer_registeration, name='signup'),
    url(r'send-email-form', views.send_email_contact_form, name='send_email_form'),
    path('admin/', admin.site.urls),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'testing-page/', views.login_testing, name='testing')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
