from django.contrib import admin
from django.urls import path
from .views import helloworldfunction, HelloWorldClass

urlpatterns = [
    path("admin/", admin.site.urls),
    path("helloworld/", helloworldfunction),
    path("helloworld2/",  HelloWorldClass.as_view()),
    # クラスベースビューを関数ベースビューに変換
    # as_view()を使うことで、クラスベースビューを関数ベースビューに変換している!
]
