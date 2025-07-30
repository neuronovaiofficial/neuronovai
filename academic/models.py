from django.db import models
from cloudinary.models import CloudinaryField  # 🔸 bunu ekle

# models.py

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 🆕 bu satırı ekle

    def __str__(self):
        return self.title

