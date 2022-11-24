from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Post
from .forms import PostForm
from .forms import PostFormAdmin


def add_post(request):
	form= PostForm(request.POST or None)


def add_event(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = PostFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return test()
        else:
            form = PostForm(request.POST)
            if form.is_valid():
                # form.save()
                event = form.save(commit=False)
                event.manager = request.user  # logged in user
                event.save()
                return test()
    else:
        # Just Going To The Page, Not Submitting
        if request.user.is_superuser:
            form = PostFormAdmin
        else:
            form = PostForm

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'imageboard/add_post.html', {'form': form, 'submitted': submitted})

def test(request):
    """Render the template."""
    # Tutaj dajemy zmienne, z którego template może korzystać
    content = {
        "test": "hash",
        "image_link": "https://asset-eu.unileversolutions.com/content/dam/unilever/lipton_international/poland/pack_design/5997264159313-1588506-png.png.ulenscale.490x490.png"
        }
    return render(request, "imageboard/test.html", content)
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "kill me"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create a calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)
    # Get current year
    now = datetime.now()
    current_year = now.year

    # Query the posts Model For Dates
    post_list = Post.objects.filter(
        date_posted__year = year,
        date_posted__month = month_number
        )

    # Get current time
    time = now.strftime('%I:%M %p')
    return render(request,
        'imageboard/home.html', {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time":time,
        "post_list": post_list,
            })



