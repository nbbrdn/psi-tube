from django.db import models


class Partner(models.Model):
    title = models.CharField(max_length=250)
    utm = models.CharField(max_length=20, db_index=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return str(self.title)
