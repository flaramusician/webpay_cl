from django.conf.urls import patterns, include, url

from .views import HomeView, OrderView


urlpatterns = patterns('apps.tienda.views',

	#url(r'^$', 'index_view', name='vista_principal'),
	#url(r'^tienda/$','index_view',name= "visualizar_principal"),
	url(r'^$',HomeView.as_view() ),
	url(r'^order/$',OrderView.as_view() ),


	)
