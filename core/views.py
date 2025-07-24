from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return HttpResponse("Hello from your first Django app!")

def contact_view(request):
    form = ContactForm()
    return render(request, 'core/sample_form.html', {'form': form})
