from django.conf import settings
from django.db import models

from django.utils import timezone

#this line defines our model
#class is keyword and post is the name of the model
#models.Model means that post is a django model,it will be saved in database
class Post(models.Model):
    #now we will define properties of class post
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#this is a link to another model
    title = models.CharField(max_length=200)#it defines text with limited no.of char
    text = models.TextField()#it defines text with unlimited  char
    created_date = models.DateTimeField(default=timezone.now)#model.___ this is date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):#publish is the method name
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#__str__ we'll get a text(string)with post title
        return self.title
# Create your models here.
