from django.db import models
import datetime
# from django.contrib.auth.models import User
# Create your models here

# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# from django.contrib.auth.models import User, AbstractUser
#
#
# class User(AbstractUser):
#     is_staff = True
#
#     class Meta(AbstractUser.Meta):
#         swappable = 'AUTH_USER_MODEL'


class Post(models.Model):

    class Meta():
        ordering = ["postDateCreate"]

    postTitle = models.CharField('postTitle', max_length=200)
    postAuthor = models.CharField('authorName', max_length=50)
    postText = models.TextField('postText')
    postDateCreate = models.DateTimeField('dateOfCreate', auto_now_add=True)
    postDatePublication = models.DateTimeField('dateOfPub', blank=True, null=True)
    postDateLastRefresh = models.DateTimeField('dateOfRefresh', auto_now=True)
    published = models.BooleanField('published', default=False)
    image = models.ImageField('image', blank=True, null=True, upload_to='posts/')

    def save(self, *args, **kwargs):

        if self.published and self.postDatePublication is None:
            self.postDatePublication = datetime.datetime.now()
        elif not self.published and self.postDatePublication is not None:
            self.pub_date = None
        super().save(*args, **kwargs)

    def showPartOfText(self, how=300):
        return self.postText[:how]

    def __str__(self):
        return self.postTitle

# class User
