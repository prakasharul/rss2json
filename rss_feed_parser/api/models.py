from django.db import models


class RSS(models.Model):
    url = models.URLField()
    sort = models.IntegerField()
