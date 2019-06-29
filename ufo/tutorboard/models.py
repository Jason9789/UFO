from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TutorRequest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

class TutorApply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title

class TutorComment(models.Model):
    blog = models.ForeignKey('TutorRequest',on_delete=models.CASCADE, related_name='tutorComments')
    comment_author = models.CharField(max_length = 10)
    comment_contents = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

class TuteeComment(models.Model):
    blog = models.ForeignKey('TutorApply',on_delete=models.CASCADE, related_name='tuteeComments')
    comment_author = models.CharField(max_length = 10)
    comment_contents = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
