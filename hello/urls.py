from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Rajat Admin"
admin.site.site_title = "Rajat Admin Portal"
admin.site.index_title = "Welcome to Rajat Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
