from django.urls import path

from profiles_api import views

#CONTENT SEQ 6th

urlpatterns = [
    path('helloView/', views.HelloApiView.as_view()) #as_views is a standard function used to convert our apiview class to be rendered by our urls
                            
]