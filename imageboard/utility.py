from .models import Post, Like, Dislike


def handle_likes(current_user, data):
    if current_user.is_authenticated and data.get("action_form_type") == "like":
        post_id = data.get("post_id")
        post = Post.objects.filter(id=post_id).first()
        action = data.get("like")
        is_positive = action == "+"
        like = Like.objects.filter(user=current_user, post=post).first()
        dislike = Dislike.objects.filter(user=current_user, post=post).first()

        if is_positive:
            target = like
            other = dislike
        else:
            target = dislike
            other = like

        if target is not None:
            target.delete()
        else:
            if is_positive:
                target = Like(user=current_user, post=post)
            else:
                target = Dislike(user=current_user, post=post)
            target.save()

        if other is not None:
            other.delete()
