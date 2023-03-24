from django.db import models
from django.utils import timezone
from .managers import PublishedManager
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to="news/images")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category"
    )
    published_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Draft
    )

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"news": self.slug})

    class Meta:
        ordering = ["-published_time"]

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
