from django.http import HttpResponse
from django.views.generic import TemplateView


def helloworldfunction(request):
    returnedobject = HttpResponse("<h1>Hello World</h1>")
    return returnedobject


# Class based views  Viewの継承
class HelloWorldClass(TemplateView):
    template_name = "helloworld.html"
    # テンプレートファイルの指定
