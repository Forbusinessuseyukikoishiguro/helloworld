from django.contrib import admin
from django.urls import path
from .views import helloworldfunction

urlpatterns = [
    path("admin/", admin.site.urls),
    path("helloworld/", helloworldfunction),
]
