from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings




class UserProfileManager(BaseUserManager):
    """Manager for UserProfile"""
    def create_user(self,email,name,password=None):
        """Create a new User Profile"""
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email = email,name = name)
        #Create A Hash Password.
        user.set_password(password)
        #save and choose the database
        user.save(using = self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """Create a Super User In Database"""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255,unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get Full NameOF USer"""
        return self.name
    
    def get_short_name(self):
        """GET Short Name"""
        return self.name
    
    def __str__(self):
        """Return String representaion of UserProfile"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return Model as String"""
        return self.status_text
    
