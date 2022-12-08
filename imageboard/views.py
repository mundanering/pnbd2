from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Post
from .models import Comment
from .models import Like
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
        if current_user.is_authenticated:
            data = request.POST
            post_id = data.get("post_id")
            post = Post.objects.filter(id=post_id).first()
            action = data.get("like")
            is_negative = action == "-"
            like = Like.objects.filter(user=current_user, post=post).first()
            print(like)
            if like is not None:
                if like.is_negative == is_negative:
                    like.delete()
                else:
                    like.is_negative = is_negative
                    like.save()
            else:
                like = Like(user=current_user, post=post, is_negative=is_negative)
                like.save()

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
def submit_comment(request, post_id):
    if request.method == 'POST':
        # Validate the form data
        body = request.POST['body']
        if body:
            # Create a new Comment object with the form data
            comment = Comment(body=body, author=request.user, post_id=post_id)
            comment.save()
            # Redirect to the post page
            return redirect('post_view', post_id=post_id)
        else:
            # Handle invalid form data
            pass
    else:
        # Handle non-POST requests
        pass

def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post_id=post_id).order_by('timestamp')
    return render(request, 'post.html', {'post': post, 'comments': comments})