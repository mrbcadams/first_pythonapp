from django.http import HttpResponse
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
from .models import Course
from .models import Category

def home(request):
    categories = Category.objects.prefetch_related('courses').all()
    return render(request, "core/index.html", {"categories": categories})

def contact_view(request):
    form = ContactForm()
    return render(request, 'core/sample_form.html', {'form': form})

def index(request):
    courses = Course.objects.all()
    return render(request, 'core/index.html', {'courses': courses})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'core/course_detail.html', {'course': course})


