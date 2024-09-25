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


class ArchitectureObject(models.Model):
    title = models.CharField(max_length=79)
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    text = models.TextField()
    address = models.CharField(max_length=255)
    group = models.ForeignKey(ArchitectureGroup, related_name="arc_objects", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
