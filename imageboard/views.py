from django.shortcuts import render
from .models import Post


# Create your views here.
def test(request):
    context = {
        "test": "hash",
        "image_link": "https://asset-eu.unileversolutions.com/content/dam/unilever/lipton_international/poland/pack_design/5997264159313-1588506-png.png.ulenscale.490x490.png"
        }  # tutaj dajemy zmienne, z którego template może korzystać
    return render(request, "imageboard/test.html", context)
