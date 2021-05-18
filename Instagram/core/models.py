from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


# first model => Post model
class Post(models.Model):
    # id = models.AutoField(primary_key = True) django auto generate this for every model
    text = models.TextField(max_length=140, blank=True, null=True) # null = None / blank = ''
    image = models.ImageField(upload_to='post_images')  # Base_dir -> media -> post_images
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    posted_on = models.DateTimeField(auto_now_add=True) # auto_now_add = True is for, when post is created then it will auto fill the time
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self): # String representation
        return str(self.pk)


# second model => post_comments model
class Comment(models.Model):
    text = models.CharField(max_length=140)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # if user or admin or someone else dlt the post the the comment will automatically deleted.
    user = models.ForeignKey(User, on_delete= models.CASCADE)  # if someone dlt the user then the all the comment wil we deleted.
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self): # String representation
        return self.text


# third model => post_like model
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True) # this is sure when like object is created it's mean someone like the post
    liked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self): # String representation
        return str(self.is_like)


# fourth model => follower model
class Follow(models.Model):
    user = models.ForeignKey(User, related_name='follow_user',  # Reverse Access Error
                             on_delete=models.CASCADE) # user_id
    follower = models.ForeignKey(User, related_name='follow_follower',  # Reverse Access Error
                                 on_delete=models.CASCADE) # follower_if
    is_follow = models.BooleanField(default=True)
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self): # String representation
        return f"{self.user} --> {self.follower}"   # if we want to represent multiple field