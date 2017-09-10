from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test/', views.handle_notification, name='handle_notification'),
 ]