from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cards/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

