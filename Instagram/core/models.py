from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


# first model => Post model
class Post(models.Model):
    text = models.TextField(max_length=140)
    image = models.ImageField(upload_to='post_images')  # Base_dir -> media -> post_images
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True) # auto_now_add = True is for, when post is created then it will auto fill the time
    updated_on = models.DateTimeField(auto_now=True)


# second model => post_comments model
class Comment(models.Model):
    text = models.CharField(max_length=140)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # if user or admin or someone else dlt the post the the comment will automatically deleted.
    user = models.ForeignKey(User, on_delete= models.CASCADE)  # if someone dlt the user then the all the comment wil we deleted.
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


# third model => post_like model
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField()


# fourth model => follower model
