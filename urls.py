from django.contrib import admin
# adding the include module to facilitate linking to other urls in apps
from django.urls import path, include

#urlpatterns for defining paths - it is a list
urlpatterns = [
    # this path is for the admin panel. ip/admin. separated by commas

    path('admin/', admin.site.urls),
    # maps to users app urls, empty url ,maps when defualt is opened  
    path("", include("users.urls") )
]
 