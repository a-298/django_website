from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    post = models.TextField()
    category = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    is_posted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
