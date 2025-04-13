from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings #to import settings from our django project

# CONTENT SEQ: 2nd
class UserProfileManager(BaseUserManager):
    """Manager for user profiles that inherates from BaseUserManager parent class"""

    def createUser(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        #Normalizing an email address "makes the second half of the email all lowercase"
        email = self.normalize_email(email)
        #Create a new model that the userManager is representing. self.model by default is set to the model that the manager is for.
        user = self.model(email=email, name=name)
        
        #Making sure password is encrypted using the set_pass provided with abstractBaseUser. this can be reverse engineered.
        user.set_password(password)
        user.save(using=self._db) #optional to choose the DB using=
        
        return user
    
    #OverRides the createsuperadmin django function
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        #self is automattically passed in when you call from any class function.
        user = self.createUser(email, name, password)
        
        user.is_superuser = True #This is automatically created in the model by the premissionsMixin
        user.is_staff = True #its name is predifined in django
        user.save(using=self._db)
        
        return user
    
    
# CONTENT SEQ: 1st
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    #Create a manager so Django knows how to work with this custom user model in django CLI tools 'CreateSuperUser for ex.'
    objects = UserProfileManager()
    
    #OverRiding the default username field and replacing it with our email field the django admin and django auth system.
    USERNAME_FIELD = 'email' #Required by default
    REQUIRED_FIELDS = ['name']
    
    def getFullName(self):
        """Retrieve full name of a user"""
        return self.name
    
    def getShortName(self):
        """Retrieve short name of a user"""
        return self.name
    
    def __str__(self):
        """Return string representation of our user"""
        return self.email


# Content SEQ 12th after login and auth.
class ProfileFeedItem(models.Model):
    """Profile Status update"""
    userProfile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    statusText = models.CharField(max_length=255)
    createdOn = models.DateTimeField(auto_now_add=True)
    
    #what to do when we turn a model instance into a string
    def __str__(self):
        """Return the model as a string"""
        return self.statusText