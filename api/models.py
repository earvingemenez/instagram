from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)


class Post(models.Model):

    tag = models.ForeignKey(Tag)

    def __str__(self):
        return "{}".format(self.tag)