from django.urls import path, include #include is used for including lists of URLS in the URLPattern and assigning the list to a specific URL

from rest_framework.routers import DefaultRouter

from profiles_api import views


#CONTENT SEQ 11th
router = DefaultRouter() # Step one for using a router. Assign a router to a variable.
router.register('helloviewset', views.HelloViewSet, basename='helloviewset')
# Step two use this to register specific view sets with our router pass it the name of our viewset, the viewset itself, basename for retrieving the urls in our router

#CONTENT SEQ 6th
urlpatterns = [
    path('helloView/', views.HelloApiView.as_view()), #as_views is a standard function used to convert our apiview class to be rendered by our urls
    path('', include(router.urls)),
                            
]