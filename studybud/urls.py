
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Base app conbinging Base->urls.py
    path('', include('base.urls')),
     path("__reload__/", include("django_browser_reload.urls")),


]
