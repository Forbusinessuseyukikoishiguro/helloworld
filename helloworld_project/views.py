from django.http import HttpResponse


def helloworldfunction(request):
    returnedobject = HttpResponse("<h1>Hello World</h1>")
    return returnedobject
