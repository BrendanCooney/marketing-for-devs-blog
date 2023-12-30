from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from cloudinary.models import CloudinaryField

STATUS = ((0,"Draft"), (1,"Published"))

# Create your models here.

class Tools(models.Model):
    name = models.CharField(max_length=200, unique = True)
    link = models.URLField(max_length=200, unique = True)
    slug = models.SlugField(max_length=200, unique = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tool_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def average_rating(self) -> float:
        return Rating.objects.filter(tools=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.name}: {self.average_rating()}"


   
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tools = models.ForeignKey(Tools, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.tools.name}: {self.rating}"