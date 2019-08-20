from django.shortcuts import render


def mivista(request):
    return render(request,'osolemioapp/index.html')
