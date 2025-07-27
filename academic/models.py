from django.db import models
from cloudinary.models import CloudinaryField  # 🔸 bunu ekle

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')  # 🔸 bu satırı değiştirdik
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
