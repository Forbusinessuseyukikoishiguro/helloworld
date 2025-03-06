from django.http import HttpResponse


def helloworldfunction(request):

    return HttpResponse("Hello World")
