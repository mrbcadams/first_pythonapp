from django.contrib import admin
from .models import Course, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'duration')
    list_filter = ("category",)
    search_fields = ('title', 'category')
# Register your models here.
