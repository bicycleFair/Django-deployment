from django.conf.urls import url
from base_app import views

app_name = 'base_app'

urlpatterns=[
	url(r'^register/$', views.register, name='register'),
	url(r'^user_login/$', views.user_login,name='login')
]