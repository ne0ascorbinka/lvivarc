from django.db import models
from django.utils.text import slugify

# Create your models here.
class ArchitectureGroup(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=79)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title