from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=27)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=70)
    category_slug=models.SlugField(max_length=100,null=True)
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail',kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        value = self.category
        self.category_slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)    
