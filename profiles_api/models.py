from django.db import models

# Standard when overriding / customizing default django user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# modal -> table in a database effectively..


# Custom manager for user profile
class UserProfileManager(BaseUserManager):
    """Manager for UserProfiles"""

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """create a new user profile"""
        if not email:  # i.e. empty string or null
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, **extra_fields)

        # Ensures that password is hashed, and not exposed -> encryption
        user.set_password(password)
        # Specifying where you are going to save these users
        user.save(using=self.db)

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save a new superuser with given details"""

        # self auto passed in already
        user = self.create_user(
            email, first_name, last_name, password, is_superuser=True, is_staff=True)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Docstring -> describe what the class does, good practice
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Allow us to deactivate users in the future
    is_active = models.BooleanField(default=True)
    # Used to determine if they have access to django admin etc.
    is_staff = models.BooleanField(default=False)

    # Specify model manager - knows how to create and control users using django TBC
    # So for example when you want to do createsuperuser --> you need to tell django how to do this
    # Because you have gone down the custom route
    objects = UserProfileManager()

    # Override username field to be email instead of user name -> django default
    USERNAME_FIELD = 'email'

    # Required fields
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # custom functions now for model
    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.first_name

    # String representation of model -> return when we convert user profile to a string in python
    def __str__(self):
        """Return string representation of our user --> on django admin basically"""
        return self.email


class Feed(models.Model):
    """Profile status update"""

    # linking one model to another -> foreign keys
    # reference settings so you can just change in settings, as opposed to hard coding
    # on delete tells you what happens if user profile is deleted
    # cascade means you cascade the change down i.e. delete the feed as well
    created_at = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    description = models.CharField(max_length=300)

    def __str__(self):
        """Return the model as a string -> basically what you see on django admin"""

        return self.title
