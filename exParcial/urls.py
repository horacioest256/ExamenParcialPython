from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('wikiApp/',include('wikiApp.urls'))
    path('',include('wikiApp.urls'))
]
