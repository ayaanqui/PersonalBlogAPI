from django.db import models
from django.utils.text import slugify
from tags.models import Tag
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150*2, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    published = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    modified = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(blank=True, default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f"{ self.id }: { self.title }"
