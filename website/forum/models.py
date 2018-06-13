from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Section(models.Model):
    section_title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.section_title

class Thread(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    thread_title = models.CharField(max_length=100)

    def __str__(self):
        return self.thread_title

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=300)
    time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return (self.author.get_username() + ':  ' + self.content)


