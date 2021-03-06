from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import CustomUserManager

GENDER_CHOICES = [
    ('M', 'male'),
    ('F', 'female'),
    ('None', 'prefer not to say'),
]
# Create your models here.

class User(AbstractUser):
    # creating field for profile in existing model User
    picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    full_name = models.CharField(max_length=150,
                                 help_text='Help people discover your account by using the name you\'re known by: either your fullname, nickname or business name.') # by default null and blank are false for username and email
    email = models.EmailField(unique=True, help_text='Enter your email carefully.')


    # optional field
    website = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, help_text='Phone number should contain 10 digits.')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    is_private_account = models.BooleanField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True, help_text='mention something interesting about yourself.')

    # Removing first and the last name from the user model.
    first_name = None
    last_name = None

    # which field will be use for username we can use either email or username.
    # if we not provide the USERNAME_FIELD it will take "username" by default
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username']

    # Accessing Custom User Manager,we define this CustomUserManager in managers.py file into user app.
    objects = CustomUserManager()

    def __str__(self):
        return self.email
