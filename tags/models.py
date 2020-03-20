from django.db import models
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=60, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name