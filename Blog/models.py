from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content1 = models.TextField(default="lorem ipsum dolor sit amet")
    content2 = models.TextField()
    image_recipe = models.ImageField(upload_to='profile_pics', blank=True)
    image1 = models.ImageField(upload_to='profile_pics', blank=True)
    image2 = models.ImageField(upload_to='profile_pics', blank=True)
    recipe_time = models.IntegerField(blank=True, default=0)
    liked = models.ManyToManyField(User, blank=True, related_name='liked')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        self.liked.all().count()

    def get_absolute_url(self):
        return reverse("Blog-detail", kwargs={'pk': self.pk})

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    like_choices = (
        ('Like', 'Like'),
        ('Unlike', 'Unlike')
    )
    value = models.CharField(choices=like_choices, default='Like', max_length = 10)
    

    def __str__(self):
        return str(self.post)
