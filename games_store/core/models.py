from django.db import models

class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    page = models.URLField(blank=True)
    picture = models.URLField(blank=True)

    def __str__(self):
        return self.name