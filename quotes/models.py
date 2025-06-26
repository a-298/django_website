from django.db import models

class Quote(models.Model):
    quote = models.TextField()
    author = models.TextField()
    book = models.TextField()

    def __str__(self):
        return self.quote
