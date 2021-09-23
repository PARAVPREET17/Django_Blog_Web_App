from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# from tinymce.models import HTMLField
from category.models import Category

choices={
    'General':'General',
    'Technology': 'Technology',
    'Education': 'Education',
    'Entertainment': 'Entertainment',
    'Politics': 'Politics',
    'Music': 'Music',
    'Acting': 'Acting',
    'Life skills': 'Life skills',

}


class Post(models.Model):
    image=models.ImageField(upload_to='profile_pics',null=True,blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail',kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
      

