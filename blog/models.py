from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('jobs', 'Latest Jobs'),
        ('admit', 'Admit Card'),
        ('result', 'Results'),
    ]

    title = models.CharField(max_length=200)
    content = RichTextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title