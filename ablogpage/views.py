from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from django.urls import reverse_lazy 
from .models import Post
from .forms import Postform # new
# Create your views here.
# def home(request):
#     return render(request,'home.html',{})
class home(ListView):
    model = Post
    template_name='home.html'

class add_post(CreateView):
    model= Post
    form_class= Postform
    template_name='add_post.html'


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'home.html', {'form': form, 'img_obj': img_obj})
    else:
        form = Postform()
    return render(request, 'home.html', {'form': form})