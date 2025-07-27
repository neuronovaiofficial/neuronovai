from django.db import models
from cloudinary.models import CloudinaryField  # 🔸 bunu ekle

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)  # 🔸 burası değişti
    link = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
