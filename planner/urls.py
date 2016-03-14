from django.conf.urls import url

from . import views

app_name = 'planner'
urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^subject/(?P<pk>[0-9]+)$', views.SubjectView.as_view(), name='subject'),
]
