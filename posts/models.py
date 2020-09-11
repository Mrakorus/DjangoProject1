from django.db import models
import datetime
# from django.contrib.auth.models import User
# Create your models here


class Post(models.Model):

    # class Meta():
    #     ordering = ["postDateCreate"]

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

# class User
