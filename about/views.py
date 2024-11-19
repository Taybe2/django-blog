from django.shortcuts import render
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_detail(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm

    context = {
        "about": about,
        "collaborate_form": collaborate_form,
    }

    return render(
        request,
        "about/about.html",
        context,
    )