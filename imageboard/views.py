from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .utility import handle_likes
from .models import Post, Like, Dislike
from django.views.generic import CreateView


def test(request):
    """Render the template."""
    # Tutaj dajemy zmienne, z którego template może korzystać
    content = {
        "test": "hash",
        "image_link": "https://asset-eu.unileversolutions.com/content/dam/unilever/lipton_international/poland/pack_design/5997264159313-1588506-png.png.ulenscale.490x490.png"
    }
    return render(request, "imageboard/test.html", content)


class addpostform(CreateView):
    template_name = "imageboard/addpost.html"
    model = Post
    fields = ("title", "contents", "image_link")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    if request.method == "POST":
        current_user = request.user
        data = request.POST
        if current_user.is_authenticated:
            if data.get("action_form_type") == "like":
                handle_likes(current_user, data)

        return redirect("home");

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
        date_posted__year=year,
        date_posted__month=month_number
    )

    # Get current time
    time = now.strftime('%I:%M %p')
    return render(request,
                  'imageboard/home.html', {
                      "year": year,
                      "month": month,
                      "month_number": month_number,
                      "cal": cal,
                      "current_year": current_year,
                      "time": time,
                      "post_list": post_list,
                  })
