from django.shortcuts import render


# Create your views here.
def index(request):

    context = {
        "test": "hash",

               }  # tutaj dajemy zmienne z którego template może korzystać
    return render(request, "imageboard/index.html", context)
