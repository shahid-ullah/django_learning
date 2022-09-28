from django.db import models


class Post(models.Model):
    msg = models.CharField(max_length=200)

    def __str__(self):
        return self.msg
