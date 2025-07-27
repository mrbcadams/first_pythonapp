from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    subtitle = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    original_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rating = models.FloatField(default=0)
    review_count = models.IntegerField(default=0)
    students_enrolled = models.IntegerField(default=0)
    total_weeks = models.IntegerField(default=4)
    total_lessons = models.IntegerField(default=12)
    total_hours = models.IntegerField(default=3)
    learning_outcomes = models.TextField()  # Store as comma-separated or JSON
    target_audience = models.TextField()  # Store as comma-separated or JSON

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
