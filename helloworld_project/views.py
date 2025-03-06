from django.http import HttpResponse


def helloworldfunction(request):

    return HttpResponse("<h1>Hello World</h1>")
